import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingWarmRestarts
import matplotlib.pyplot as plt
import os
import math

# Restrict CPU threads to respect system limits
torch.set_num_threads(6)

def get_primes_up_to(max_val):
    sieve = [True] * (max_val + 1)
    for p in range(2, int(math.sqrt(max_val)) + 1):
        if sieve[p]:
            for i in range(p * p, max_val + 1, p):
                sieve[i] = False
    return [p for p in range(2, max_val + 1) if sieve[p]]

class NumberTheoreticTransformer(nn.Module):
    def __init__(self, N, d_model=32, nhead=4, num_layers=2):
        super(NumberTheoreticTransformer, self).__init__()
        self.N = N
        self.primes = get_primes_up_to(N)
        self.num_primes = len(self.primes)
        
        # Precompute prime factorizations for 1 to N
        factorizations = torch.zeros(N, self.num_primes)
        for i in range(1, N + 1):
            temp = i
            for j, p in enumerate(self.primes):
                count = 0
                while temp % p == 0:
                    count += 1
                    temp //= p
                factorizations[i-1, j] = count
                if temp == 1:
                    break
        
        # We store the factorizations as a buffer so it moves with the model device
        self.register_buffer('factorizations', factorizations)
        
        # Embed the prime exponent vector into d_model dimensions
        self.prime_embedding = nn.Linear(self.num_primes, d_model)
        
        # Transformer Encoder
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead, dropout=0.2, batch_first=True)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # Output projection to single coefficient a_k
        self.output_proj = nn.Linear(d_model, 1)

    def forward(self):
        # factorizations: [N, num_primes]
        x = self.prime_embedding(self.factorizations) # [N, d_model]
        
        if self.training:
            x = x + torch.randn_like(x) * 0.05
            
        # Add a batch dimension for transformer: [1, N, d_model]
        x = x.unsqueeze(0)
        
        # Transformer context awareness
        x = self.transformer(x) # [1, N, d_model]
        
        # Project down
        a_k = self.output_proj(x).squeeze() # [N]
        return a_k

def indicator_chi(t):
    # chi_{(0,1)}(t)
    return (t > 0) & (t < 1)

def compute_l2_loss_vectorized(a_k, N, t_samples):
    batch_size = t_samples.shape[0]
    
    chi_val = indicator_chi(t_samples).float()
    
    k_tensor = torch.arange(1, N + 1, device=t_samples.device, dtype=torch.float32).unsqueeze(0) # [1, N]
    t_samples_view = t_samples.unsqueeze(1) # [batch_size, 1]
    
    # Broadcast division: [batch_size, N]
    t_over_k = t_samples_view / k_tensor
    frac_part = t_over_k - torch.floor(t_over_k)
    
    # Dot product with a_k
    approximation = torch.matmul(frac_part, a_k) # [batch_size]

    t_clipped = torch.clamp(t_samples, min=1e-5)
    integrand = ((chi_val - approximation) ** 2) / (t_clipped ** 2)
    
    return torch.mean(integrand)

def train_number_theoretic_transformer(N=1000, epochs=500, samples=10000, log_dir="D:/sizzlin-riemann/logs/"):
    os.makedirs(log_dir, exist_ok=True)
    plot_path = os.path.join(log_dir, "loss_curve.png")
    
    print(f"Initializing Phase 5.2 Network Resuscitation for N={N}...")
    
    model = NumberTheoreticTransformer(N=N)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    scheduler = CosineAnnealingWarmRestarts(optimizer, T_0=50, T_mult=2)
    
    print("\n[Architecture]")
    print(model)
    
    t_samples = torch.rand(samples) * N 
    
    losses = []
    
    print(f"\n[Training Logs - Saving plots to {plot_path}]")
    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()
        
        # Predict all a_k coefficients (entangled)
        a_k_preds = model()
        
        loss = compute_l2_loss_vectorized(a_k_preds, N, t_samples)
        
        loss.backward()
        if epoch <= 10:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        
        current_loss = loss.item()
        losses.append(current_loss)
        scheduler.step()
        
        if epoch % 10 == 0 or epoch == 1:
            print(f"Epoch {epoch:03d}/{epochs} | d_N^2 Loss: {current_loss:.6f} | LR: {optimizer.param_groups[0]['lr']:.6f}")
            
            # Save real-time plot
            plt.figure(figsize=(8, 5))
            plt.plot(range(1, epoch + 1), losses, label="d_N^2 Loss (L2 Distance)", color="blue")
            plt.title("Vasyunin Coefficient DRL Optimization (Transformer)")
            plt.xlabel("Epoch")
            plt.ylabel("d_N^2 Loss")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(plot_path)
            plt.close()

    # Save the final coefficients for the Lean 4 handshake
    model.eval()
    with torch.no_grad():
        final_a_k = model()
        torch.save(final_a_k, os.path.join(os.path.dirname(__file__), "final_coefficients.pt"))
    print("\n[+] Phase 5.2 Training complete. Coefficients saved to final_coefficients.pt.")

if __name__ == "__main__":
    train_number_theoretic_transformer(N=1000, epochs=500, samples=10000)
