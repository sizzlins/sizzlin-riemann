"""
2-Term Ansatz Projection: phi(k)/k + sigma_1(k)/k subspace test.
Does restricting a_k to the 2-term form preserve d_N^2 -> 0?
"""
import numpy as np
import math
import sympy as sp

def build_gram_matrix(N):
    M = np.zeros((N, N))
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            g = math.gcd(i, j)
            M[i-1, j-1] = (g**2) / (12 * i * j) + 0.25
    return M

def compute_projection(N, basis_funcs):
    """
    Given basis functions that define a_k = sum_j C_j * f_j(k),
    project the full N-dim optimization onto the len(basis_funcs)-dim subspace.
    
    basis_funcs: list of functions, each takes k (1-indexed) and returns f_j(k)
    
    The Ansatz is: a_k = sum_j C_j * f_j(k)
    So a = V @ C where V[k,j] = f_j(k+1)
    
    The energy: d_N^2 = 1 - 2*a^T*L + a^T*M*a
                      = 1 - 2*(V@C)^T*L + (V@C)^T*M*(V@C)
                      = 1 - 2*C^T*(V^T*L) + C^T*(V^T*M*V)*C
    
    Minimizing over C: (V^T*M*V)*C = V^T*L
    """
    M = build_gram_matrix(N)
    L = np.full((N,), 0.5)
    
    # Build V matrix
    n_basis = len(basis_funcs)
    V = np.zeros((N, n_basis))
    for j, f in enumerate(basis_funcs):
        for k in range(1, N + 1):
            V[k-1, j] = f(k)
    
    # Projected system
    VtMV = V.T @ M @ V
    VtL = V.T @ L
    
    # Solve for optimal C
    C = np.linalg.solve(VtMV, VtL)
    
    # Reconstruct a_k
    a_restricted = V @ C
    
    # Compute d_N^2
    d_N_sq = 1.0 - 2.0 * a_restricted @ L + a_restricted @ M @ a_restricted
    
    # Also compute full (unrestricted) for comparison
    a_full = np.linalg.solve(M, L)
    d_N_sq_full = 1.0 - 2.0 * a_full @ L + a_full @ M @ a_full
    
    return C, a_restricted, d_N_sq, a_full, d_N_sq_full

def main():
    # Precompute phi and sigma_1 caches
    phi_cache = {}
    sigma1_cache = {}
    
    def get_phi(k):
        if k not in phi_cache:
            phi_cache[k] = int(sp.totient(k))
        return phi_cache[k]
    
    def get_sigma1(k):
        if k not in sigma1_cache:
            sigma1_cache[k] = int(sp.divisor_sigma(k, 1))
        return sigma1_cache[k]
    
    # === TEST 1: 2-Term Ansatz ===
    # a_k = C1 * phi(k)/k + C2 * sigma_1(k)/k
    basis_2 = [
        lambda k: get_phi(k) / k,
        lambda k: get_sigma1(k) / k,
    ]
    
    print("=" * 70)
    print("2-TERM ANSATZ: a_k = C1 * phi(k)/k + C2 * sigma_1(k)/k")
    print("=" * 70)
    
    for N in [10, 20, 50, 100, 150, 200, 300]:
        C, a_res, d_res, a_full, d_full = compute_projection(N, basis_2)
        ratio = d_res / d_full if d_full > 0 else float('inf')
        print(f"  N={N:4d}: d_N^2(restricted)={d_res:.8e}, d_N^2(full)={d_full:.8e}, "
              f"ratio={ratio:.4f}, C1={C[0]:.6f}, C2={C[1]:.6f}")
    
    # === TEST 2: 3-Term Ansatz (add mu(k)/k) ===
    moeb_cache = {}
    def get_moeb(k):
        if k not in moeb_cache:
            moeb_cache[k] = int(sp.mobius(k))
        return moeb_cache[k]
    
    basis_3 = [
        lambda k: get_phi(k) / k,
        lambda k: get_sigma1(k) / k,
        lambda k: get_moeb(k) / k,
    ]
    
    print()
    print("=" * 70)
    print("3-TERM ANSATZ: a_k = C1*phi/k + C2*sigma_1/k + C3*mu/k")
    print("=" * 70)
    
    for N in [10, 20, 50, 100, 150, 200, 300]:
        C, a_res, d_res, a_full, d_full = compute_projection(N, basis_3)
        ratio = d_res / d_full if d_full > 0 else float('inf')
        print(f"  N={N:4d}: d_N^2(restricted)={d_res:.8e}, d_N^2(full)={d_full:.8e}, "
              f"ratio={ratio:.4f}, C=({C[0]:.6f}, {C[1]:.6f}, {C[2]:.6f})")
    
    # === TEST 3: Single-term Ansatze for comparison ===
    print()
    print("=" * 70)
    print("SINGLE-TERM COMPARISONS")
    print("=" * 70)
    
    for name, basis in [
        ("phi/k", [lambda k: get_phi(k) / k]),
        ("sigma_1/k", [lambda k: get_sigma1(k) / k]),
        ("mu/k", [lambda k: get_moeb(k) / k]),
        ("1/k", [lambda k: 1.0 / k]),
        ("phi/k^2", [lambda k: get_phi(k) / k**2]),
    ]:
        print(f"\n  --- a_k = C * {name} ---")
        for N in [10, 50, 100, 300]:
            C, a_res, d_res, a_full, d_full = compute_projection(N, basis)
            ratio = d_res / d_full if d_full > 0 else float('inf')
            print(f"    N={N:4d}: d_N^2={d_res:.8e} (full={d_full:.8e}, ratio={ratio:.4f}, C={C[0]:.6f})")
    
    # === TEST 4: Convergence rate of 2-term and 3-term ===
    print()
    print("=" * 70)
    print("CONVERGENCE RATE ANALYSIS")
    print("=" * 70)
    
    Ns_2t = []
    ds_2t = []
    ds_3t = []
    ds_full = []
    
    for N in [10, 20, 30, 50, 75, 100, 150, 200, 300]:
        _, _, d2, _, df = compute_projection(N, basis_2)
        _, _, d3, _, _ = compute_projection(N, basis_3)
        Ns_2t.append(N)
        ds_2t.append(d2)
        ds_3t.append(d3)
        ds_full.append(df)
    
    Ns_arr = np.array(Ns_2t, dtype=float)
    
    for label, ds in [("Full", ds_full), ("2-Term", ds_2t), ("3-Term", ds_3t)]:
        ds_arr = np.array(ds)
        mask = ds_arr > 0
        if mask.sum() >= 2:
            slope, intercept = np.polyfit(np.log(Ns_arr[mask]), np.log(ds_arr[mask]), 1)
            print(f"  {label:8s}: d_N^2 ~ {np.exp(intercept):.4f} * N^{slope:.4f}")

if __name__ == "__main__":
    main()
