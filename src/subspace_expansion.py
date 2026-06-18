import math
import numpy as np
import time
from sympy import divisor_count

# --- REUSED EXACT ALGEBRAIC GENERATOR ---
# using cotangent Vasyunin sums from baez_duarte_exact_algebraic.py
def V(h, k):
    if k == 1: return 0.0
    s = 0.0
    for r in range(1, k):
        try:
            val = 1.0 / math.tan(math.pi * r * h / k)
        except ZeroDivisionError:
            val = 0.0
        s += (r / float(k)) * val
    return s

def exact_M_jk(j, k):
    g = math.gcd(j, k)
    term1 = 0.5 * math.log(j * k / (g**2))
    term2 = math.log(2 * math.pi) - 0.5772156649015328606
    term3 = (math.pi / 2.0) * (V(k//g, j//g) + V(j//g, k//g))
    return (g / float(j * k)) * (term1 + term2 + term3)

def exact_L_k(k):
    return (1.0 / k) * (math.log(k) + 1.0 - 0.5772156649015328606)

def build_system(N):
    M = np.zeros((N, N), dtype=np.float64)
    L = np.zeros(N, dtype=np.float64)
    for j in range(1, N + 1):
        L[j-1] = exact_L_k(j)
        for k in range(j, N + 1):
            val = exact_M_jk(j, k)
            M[j-1, k-1] = val
            M[k-1, j-1] = val
    return M, L

# --- 4D GALERKIN SUBSPACE PROJECTION ---
def project_4d(N):
    print(f"\n--- 4D Subspace Projection N={N} ---")
    t0 = time.time()

    M, L = build_system(N)

    k = np.arange(1, N + 1, dtype=np.float64)
    v1 = 1.0 / (k**2)                                                      # base core
    v2 = np.array([float(divisor_count(i)) for i in range(1, N+1)]) / (k**2) # prime-gap DNA
    v3 = 1.0 / k                                                            # mass compensator
    v4 = np.log(k) / k                                                      # logarithmic tail

    V_mat = np.column_stack((v1, v2, v3, v4))

    # Galerkin: (V^T M V) c = V^T L
    M_sub = V_mat.T @ M @ V_mat
    L_sub = V_mat.T @ L

    c = np.linalg.solve(M_sub, L_sub)

    a_proj = V_mat @ c
    E_N = a_proj.T @ M @ a_proj
    norm_sq = a_proj.T @ a_proj
    rayleigh = E_N / norm_sq

    # also compute full distance d_N^2 = a^T M a - 2 a^T L + ||chi||^2
    # using ||chi||^2 = 1 (standard Baez-Duarte normalization)
    d2 = E_N - 2.0 * np.dot(a_proj, L) + 1.0

    t_end = time.time() - t0

    print(f"Optimal Constants        : c1={c[0]:.6f}, c2={c[1]:.6f}, c3={c[2]:.6f}, c4={c[3]:.6f}")
    print(f"Projected Energy (E_N)   : {E_N:.8e}")
    print(f"Distance d_N^2           : {d2:.8e}")
    print(f"Rayleigh Quotient        : {rayleigh:.8e}")
    print(f"Execution Time           : {t_end:.2f} s")

def main():
    print("=== PHASE 8: 4D SUBSPACE EXPANSION ===")
    print("Basis: [1/k^2, d(k)/k^2, 1/k, ln(k)/k]")
    for N in [100, 250, 500, 1000]:
        project_4d(N)

if __name__ == "__main__":
    main()
