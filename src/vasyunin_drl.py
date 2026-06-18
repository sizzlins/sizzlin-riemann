import torch
import torch.nn as nn
import torch.optim as optim
import math
import sys

# Restrict CPU threads to respect 75% limit (assuming an average 8-core CPU)
torch.set_num_threads(6)

class VasyuninCoefficientNet(nn.Module):
    def __init__(self, hidden_dim=32):
        super(VasyuninCoefficientNet, self).__init__()
        # A simple MLP to map from k -> a_k
        self.net = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )
        
    def forward(self, k_tensor):
        return self.net(k_tensor)

def indicator_chi(t):
    # chi_{(0,1)}(t)
    return (t > 0) & (t < 1)

def compute_l2_loss(a_k, N, t_samples):
    """
    Computes the L2 distance d_N^2 using Monte Carlo integration.
    loss = mean_t [ (chi(t) - sum_k a_k {t/k})^2 / t^2 ]
    """
    batch_size = t_samples.shape[0]
    
    chi_val = indicator_chi(t_samples).float()
    
    approximation = torch.zeros(batch_size, device=t_samples.device)
    
    # Evaluate sum_{k=1}^N a_k {t/k}
    for k in range(1, N + 1):
        # Fractional part: t/k - floor(t/k)
        t_over_k = t_samples / float(k)
        frac_part = t_over_k - torch.floor(t_over_k)
        approximation += a_k[k-1] * frac_part

    # The weighting measure is dt / t^2
    # We clip t to avoid division by zero at t=0
    t_clipped = torch.clamp(t_samples, min=1e-5)
    integrand = ((chi_val - approximation) ** 2) / (t_clipped ** 2)
    
    # Monte Carlo integration mean
    return torch.mean(integrand)

def train_vasyunin_drl(N=50, epochs=10, samples=10000):
    print(f"Initializing Vasyunin DRL Environment for N={N}...")
    
    model = VasyuninCoefficientNet()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    print("\n[Architecture]")
    print(model)
    
    # Fixed evaluation grid for t to ensure stable gradients
    # We focus mostly on t in (0, N] since frac(t/k) becomes periodic and small for large t
    t_samples = torch.rand(samples) * N 
    
    k_inputs = torch.arange(1, N + 1, dtype=torch.float32).unsqueeze(1)
    # Normalize inputs to help NN convergence
    k_normalized = k_inputs / float(N)
    
    print("\n[Training Logs]")
    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()
        
        # Predict all a_k coefficients for current epoch
        a_k_preds = model(k_normalized).squeeze()
        
        loss = compute_l2_loss(a_k_preds, N, t_samples)
        
        loss.backward()
        optimizer.step()
        
        print(f"Epoch {epoch:02d}/{epochs} | d_N^2 Loss: {loss.item():.6f}")

    print("\n[+] DRL Baseline complete.")

if __name__ == "__main__":
    train_vasyunin_drl(N=50, epochs=10, samples=10000)
