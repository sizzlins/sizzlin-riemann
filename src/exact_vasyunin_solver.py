import numpy as np
import pandas as pd
import math
import os

def build_and_solve(N):
    print(f"Building exact Nyman-Beurling Sawtooth matrix for N={N}...")
    M = np.zeros((N, N))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            g = math.gcd(i, j)
            M[i-1, j-1] = (g**2) / (12 * i * j) + 0.25

    L = np.full((N,), 0.5)

    print("Solving linear system M * a = L...")
    a_exact = np.linalg.solve(M, L)
    
    # Detrend: y = k * a_k
    k_vals = np.arange(1, N + 1)
    y_detrended = k_vals * a_exact
    
    df = pd.DataFrame({
        'N': [N]*N,
        'k': k_vals,
        'y_detrended': y_detrended
    })
    
    output_path = os.path.join(os.path.dirname(__file__), 'detrended_results.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved {N} perfectly exact detrended values to {output_path}")

if __name__ == "__main__":
    build_and_solve(100)
