"""
Phase 5: Multi-N exact solver and convergence analysis.
Generates exact Nyman-Beurling optimal coefficients for multiple N values,
then analyzes d_N^2 convergence and coefficient structure.
"""
import numpy as np
import pandas as pd
import sympy as sp
from sympy import mobius
import math
import os

def build_and_solve(N):
    """Build exact Gram matrix and solve for optimal a_k."""
    M = np.zeros((N, N))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            g = math.gcd(i, j)
            M[i-1, j-1] = (g**2) / (12 * i * j) + 0.25

    L = np.full((N,), 0.5)
    a_exact = np.linalg.solve(M, L)
    
    # d_N^2 = 1 - a^T L = 1 - sum(a_k)/2  (since Ma = L => a^T M a = a^T L)
    # Actually: d_N^2 = <chi,chi> - 2<chi, sum a_k f_k> + <sum, sum>
    #         = 1 - 2 * sum(a_k * 1/2) + a^T M a
    #         = 1 - sum(a_k) + a^T L  (since Ma = L)
    #         = 1 - sum(a_k) + sum(a_k)/2
    #         = 1 - sum(a_k)/2
    d_N_sq = 1.0 - np.sum(a_exact) / 2.0
    
    return a_exact, d_N_sq

def main():
    N_values = [10, 20, 30, 50, 75, 100, 150, 200, 300]
    
    all_rows = []
    convergence = []
    
    for N in N_values:
        print(f"Solving N={N}...", end=" ", flush=True)
        a_exact, d_N_sq = build_and_solve(N)
        print(f"d_N^2 = {d_N_sq:.8e}")
        
        convergence.append({'N': N, 'd_N_sq': d_N_sq, 'sum_a_k': np.sum(a_exact)})
        
        k_vals = np.arange(1, N + 1)
        for k, ak in zip(k_vals, a_exact):
            all_rows.append({'N': N, 'k': int(k), 'a_k': ak, 'y_detrended': ak * k})
    
    # Save all data
    df_all = pd.DataFrame(all_rows)
    output_path = os.path.join(os.path.dirname(__file__), 'multi_N_results.csv')
    df_all.to_csv(output_path, index=False)
    print(f"\nSaved multi-N results to {output_path}")
    
    # Convergence table
    print("\n" + "="*60)
    print("CONVERGENCE TABLE: d_N^2 vs N")
    print("="*60)
    print(f"{'N':>6s} {'d_N^2':>14s} {'sum(a_k)':>14s} {'log(d_N^2)':>14s}")
    print("-"*60)
    for row in convergence:
        ld = np.log10(row['d_N_sq']) if row['d_N_sq'] > 0 else float('-inf')
        print(f"{row['N']:6d} {row['d_N_sq']:14.8e} {row['sum_a_k']:14.8f} {ld:14.4f}")
    
    # Check convergence rate: does d_N^2 ~ C/N^alpha?
    Ns = np.array([r['N'] for r in convergence], dtype=float)
    ds = np.array([r['d_N_sq'] for r in convergence])
    mask = ds > 0
    if mask.sum() >= 2:
        log_N = np.log(Ns[mask])
        log_d = np.log(ds[mask])
        slope, intercept = np.polyfit(log_N, log_d, 1)
        print(f"\nPower law fit: d_N^2 ~ N^{slope:.4f}")
        print(f"  (If slope < 0, d_N^2 -> 0, consistent with RH being true)")
    
    # Analyze coefficient structure at largest N
    N_max = max(N_values)
    df_max = df_all[df_all['N'] == N_max].copy()
    k_arr = df_max['k'].values.astype(float)
    a_k = df_max['a_k'].values
    
    phi_arr = np.array([int(sp.totient(int(k))) for k in df_max['k']], dtype=float)
    moeb_arr = np.array([int(mobius(int(k))) for k in df_max['k']], dtype=float)
    
    print(f"\n{'='*60}")
    print(f"COEFFICIENT ANALYSIS at N={N_max}")
    print(f"{'='*60}")
    
    # Check convergence toward mu(k)/k
    # At large N, a_k should approach mu(k)/k (Balazard-Saias)
    mu_over_k = moeb_arr / k_arr
    
    # Count sign agreement
    sign_agree = np.sum(np.sign(a_k) == np.sign(mu_over_k))
    print(f"Sign agreement a_k vs mu(k)/k: {sign_agree}/{N_max}")
    print(f"a_k positive: {np.sum(a_k > 0)}, negative: {np.sum(a_k < 0)}, zero: {np.sum(np.abs(a_k) < 1e-15)}")
    
    # Correlation with key functions
    y_det = a_k * k_arr
    r_phi = np.corrcoef(y_det, phi_arr)[0,1]
    r_k = np.corrcoef(y_det, k_arr)[0,1]
    print(f"\ncorr(a_k*k, phi(k)): {r_phi:.6f}")
    print(f"corr(a_k*k, k):      {r_k:.6f}")
    print(f"phi(k) advantage:     {r_phi - r_k:.6f}")

if __name__ == "__main__":
    main()
