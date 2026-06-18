import math
import numpy as np
import time
from sympy import divisor_count

# --- REUSED EXACT ALGEBRAIC GENERATOR ---
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

# --- GALERKIN SUBSPACE PROJECTION ---
def project_and_evaluate(N):
    print(f"\n--- Subspace Projection N={N} ---")
    t0 = time.time()
    
    # 1. Build Full System
    M, L = build_system(N)
    
    # 2. Build 2D Subspace Basis V
    k = np.arange(1, N + 1, dtype=np.float64)
    v1 = 1.0 / (k**2)
    v2 = np.array([float(divisor_count(i)) for i in range(1, N + 1)]) / (k**2)
    
    V_mat = np.column_stack((v1, v2))
    
    # 3. Galerkin Projection: (V^T M V) c = V^T L
    M_sub = V_mat.T @ M @ V_mat
    L_sub = V_mat.T @ L
    
    # 4. Solve for global constants c1, c2
    c = np.linalg.solve(M_sub, L_sub)
    c1, c2 = c[0], c[1]
    
    # 5. Evaluate Energy and Geometry
    a_proj = V_mat @ c
    E_N = a_proj.T @ M @ a_proj
    norm_sq = a_proj.T @ a_proj
    rayleigh = E_N / norm_sq
    
    t_end = time.time() - t0
    
    print(f"Optimal Global Constants : c1 = {c1:.6f}, c2 = {c2:.6f}")
    print(f"Projected Energy (E_N)   : {E_N:.8e}")
    print(f"Rayleigh Quotient        : {rayleigh:.8e}")
    print(f"Execution Time           : {t_end:.2f} s")

def main():
    print("=== PHASE 6: 2D SUBSPACE PROJECTION ===")
    Ns = [100, 250, 500, 1000]
    for N in Ns:
        project_and_evaluate(N)

if __name__ == "__main__":
    main()
