import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingWarmRestarts
import math

# Restrict CPU threads to respect 75% limit (assuming an average 8-core CPU)
torch.set_num_threads(6)

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

# Precompute primes up to 1000 (there are 168 of them)
PRIMES_UNDER_1000 = sieve_of_eratosthenes(1000)
NUM_PRIMES = len(PRIMES_UNDER_1000)

def get_prime_factorization_tensor(k, num_primes=NUM_PRIMES):
    """
    Decomposes integer k into a vector of prime exponents.
    For example, 12 -> [2, 1, 0, 0, ...] (since 12 = 2^2 * 3^1)
    """
    exponents = torch.zeros(num_primes, dtype=torch.float32)
    if k <= 1:
        return exponents
    
    temp_k = k
    for i, p in enumerate(PRIMES_UNDER_1000):
        if p * p > temp_k:
            if temp_k > 1:
                try:
                    idx = PRIMES_UNDER_1000.index(temp_k)
                    exponents[idx] += 1
                except ValueError:
                    pass
            break
        while temp_k % p == 0:
            exponents[i] += 1
            temp_k //= p
    return exponents

class GaussianNoise(nn.Module):
    def __init__(self, std=0.05):
        super().__init__()
        self.std = std

    def forward(self, x):
        if self.training and self.std > 0:
            noise = torch.randn_like(x) * self.std
            return x + noise
        return x

class NumberTheoreticTransformer(nn.Module):
    def __init__(self, in_features=NUM_PRIMES, d_model=32, nhead=4, num_layers=2, dropout=0.2):
        super(NumberTheoreticTransformer, self).__init__()
        
        # Maps the 168-dim prime exponent vector to the Transformer hidden dimension
        self.prime_embedding = nn.Linear(in_features, d_model)
        
        # Inject Gaussian Noise directly into the embeddings to escape local minima
        self.noise = GaussianNoise(std=0.05)
        
        # Transformer Encoder to capture multiplicative rules across the prime sequence
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, 
            nhead=nhead, 
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # Output projection back to a scalar coefficient
        self.output_proj = nn.Linear(d_model, 1)
        
    def forward(self, k_prime_tensor):
        # k_prime_tensor shape: (batch_size, num_primes)
        # Add sequence dimension for Transformer: (batch_size, 1, num_primes)
        x = k_prime_tensor.unsqueeze(1)
        
        x = self.prime_embedding(x)
        x = self.noise(x)
        
        x = self.transformer(x)
        
        # Pool the sequence output back to batch dimension
        x = x.squeeze(1)
        return self.output_proj(x)

def indicator_chi(t):
    return (t > 0) & (t < 1)

def compute_l2_loss(a_k, N, t_samples):
    batch_size = t_samples.shape[0]
    chi_val = indicator_chi(t_samples).float()
    
    approximation = torch.zeros(batch_size, device=t_samples.device)
    
    for k in range(1, N + 1):
        t_over_k = t_samples / float(k)
        frac_part = t_over_k - torch.floor(t_over_k)
        approximation += a_k[k-1] * frac_part

    t_clipped = torch.clamp(t_samples, min=1e-5)
    integrand = ((chi_val - approximation) ** 2) / (t_clipped ** 2)
    
    return torch.mean(integrand)

def train_vasyunin_drl(N=1000, epochs=500, samples=10000):
    print(f"Initializing Vasyunin DRL Environment for N={N}...")
    
    model = NumberTheoreticTransformer(in_features=NUM_PRIMES)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    # Rhythmic learning rate pulses
    scheduler = CosineAnnealingWarmRestarts(optimizer, T_0=50, T_mult=2)
    
    print("\n[Architecture]")
    print(model)
    
    # Precompute prime factorizations for all k in [1, N]
    print(f"\nPrecomputing prime factorizations for {N} coefficients...")
    k_prime_tensors = torch.stack([get_prime_factorization_tensor(k) for k in range(1, N + 1)])
    
    t_samples = torch.rand(samples) * N 
    
    print("\n[Training Logs]")
    for epoch in range(1, epochs + 1):
        model.train()
        optimizer.zero_grad()
        
        # Forward pass all k vectors
        a_k_preds = model(k_prime_tensors).squeeze()
        
        loss = compute_l2_loss(a_k_preds, N, t_samples)
        
        loss.backward()
        
        # Prevent gradient explosion
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        
        optimizer.step()
        scheduler.step()
        
        if epoch % 50 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d}/{epochs} | d_N^2 Loss: {loss.item():.6f} | LR: {scheduler.get_last_lr()[0]:.6f}")

    print("\n[+] DRL Baseline complete.")

if __name__ == "__main__":
    # We use a smaller N and epoch count here by default for quick validation
    train_vasyunin_drl(N=50, epochs=100, samples=5000)
