import math
import numpy as np
import time
from sympy import mobius

# --- REUSED EXACT ALGEBRAIC GENERATOR ---
def V_sum(h, k):
    if k == 1: return 0.0
    s = 0.0
    for r in range(1, k):
        try: val = 1.0 / math.tan(math.pi * r * h / k)
        except ZeroDivisionError: val = 0.0
        s += (r / float(k)) * val
    return s

def exact_M_jk(j, k):
    g = math.gcd(j, k)
    term1 = 0.5 * math.log(j * k / (g**2))
    term2 = math.log(2 * math.pi) - 0.5772156649015328606
    term3 = (math.pi / 2.0) * (V_sum(k//g, j//g) + V_sum(j//g, k//g))
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

# --- MOLLIFIED MÖBIUS PROJECTION ---
def project_mollifier(N):
    print(f"\n--- Mollified Möbius Projection N={N} ---")
    t0 = time.time()

    M, L = build_system(N)

    # Construct the mollified basis vector v
    v = np.zeros(N, dtype=np.float64)
    log_N = math.log(N)
    for k in range(1, N + 1):
        mu_k = mobius(k)
        if mu_k == 0:
            v[k-1] = 0.0
        else:
            log_k = math.log(k)
            taper = 1.0 - (log_k / log_N)
            v[k-1] = (mu_k / float(k)) * taper

    # 1D Galerkin Projection: (v^T M v) C = v^T L
    M_v = np.dot(v, np.dot(M, v))
    L_v = np.dot(v, L)

    C = L_v / M_v
    
    a_proj = C * v
    E_N = np.dot(a_proj, np.dot(M, a_proj))
    
    # Distance: d_N^2 = E_N - 2 * a^T L + ||chi||^2
    # ||chi||^2 = 1
    d2 = E_N - 2.0 * np.dot(a_proj, L) + 1.0

    t_end = time.time() - t0

    print(f"Optimal Global Constant C : {C:.6f}")
    print(f"Projected Energy (E_N)    : {E_N:.8e}")
    print(f"Distance d_N^2            : {d2:.8e}")
    print(f"Execution Time            : {t_end:.2f} s")

def main():
    print("=== PHASE 11: LOGARITHMIC MOLLIFIER ===")
    print("Basis: a_k = C * (mu(k)/k) * [1 - ln(k)/ln(N)]")
    for N in [100, 250, 500, 1000]:
        project_mollifier(N)

if __name__ == "__main__":
    main()
