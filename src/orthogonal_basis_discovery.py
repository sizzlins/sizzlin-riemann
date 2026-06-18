import math
import numpy as np
import time
from sympy import divisor_count, mobius, totient, primefactors

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

# --- NUMBER-THEORETIC DICTIONARY ---
def mangoldt(n):
    if n <= 1: return 0.0
    factors = primefactors(n)
    if len(factors) == 1: return float(np.log(factors[0]))
    return 0.0

def build_dictionary(N):
    """Build a dictionary of candidate basis vectors. Each is an N-vector."""
    k = np.arange(1, N + 1, dtype=np.float64)
    d_k = np.array([float(divisor_count(i)) for i in range(1, N+1)])
    mu_k = np.array([float(mobius(i)) for i in range(1, N+1)])
    phi_k = np.array([float(totient(i)) for i in range(1, N+1)])
    lam_k = np.array([mangoldt(i) for i in range(1, N+1)])

    vectors = {
        "1/k":         1.0 / k,
        "1/k^2":       1.0 / k**2,
        "ln(k)/k":     np.log(k) / k,              # ln(1)=0, ok
        "ln(k)/k^2":   np.log(k) / k**2,
        "ln(k)^2/k":   np.log(k)**2 / k,
        "d(k)/k":      d_k / k,
        "d(k)/k^2":    d_k / k**2,
        "phi(k)/k^2":  phi_k / k**2,
        "mu(k)/k":     mu_k / k,
        "Lambda(k)/k": lam_k / k,
        "1/k^1.5":     1.0 / k**1.5,
        "d(k)/k^1.5":  d_k / k**1.5,
    }
    # fix ln(1)=0 edge: already 0, no issue
    return vectors

def orthogonal_projection(N):
    print(f"\n--- Orthogonal Basis Discovery N={N} ---")
    t0 = time.time()

    M, L = build_system(N)
    dictionary = build_dictionary(N)

    # Stack all candidates into a matrix
    names = list(dictionary.keys())
    raw = np.column_stack([dictionary[n] for n in names])

    # QR orthogonalization (numerically stable, always valid)
    Q, R = np.linalg.qr(raw)
    # Q has orthonormal columns. Rank = number of linearly independent vectors.
    rank = np.sum(np.abs(np.diag(R)) > 1e-10)
    Q = Q[:, :rank]  # trim to rank

    print(f"Dictionary size: {len(names)}, Effective rank: {rank}")

    # Galerkin projection in the orthonormal basis
    M_sub = Q.T @ M @ Q
    L_sub = Q.T @ L

    c = np.linalg.solve(M_sub, L_sub)

    a_proj = Q @ c
    E_N = a_proj.T @ M @ a_proj
    d2 = E_N - 2.0 * np.dot(a_proj, L) + 1.0

    # Also compute: what's the best possible d2 from the FULL system?
    # (for comparison, using regularized pseudoinverse)
    try:
        a_full = np.linalg.lstsq(M, L, rcond=1e-10)[0]
        E_full = a_full.T @ M @ a_full
        d2_full = E_full - 2.0 * np.dot(a_full, L) + 1.0
    except:
        d2_full = float('nan')

    t_end = time.time() - t0

    print(f"Projected Energy (E_N)   : {E_N:.8e}")
    print(f"Distance d_N^2 (ours)    : {d2:.8e}")
    print(f"Distance d_N^2 (full)    : {d2_full:.8e}")
    print(f"Execution Time           : {t_end:.2f} s")

    # Show which dictionary vectors contribute most
    # Map Q back to original basis: c_orig = R_inv @ c, but simpler to just show Q weights
    # Actually: a_proj = Q @ c = raw @ R_inv @ c, so original weights = R_inv @ c
    try:
        R_sq = R[:rank, :rank]
        c_orig = np.linalg.solve(R_sq, c)
        print(f"\nOriginal basis weights:")
        for i, name in enumerate(names[:rank]):
            print(f"  {name:15s} : {c_orig[i]:+.6f}")
    except:
        print("  (could not recover original weights)")

def main():
    print("=== PHASE 9: ORTHOGONAL BASIS DISCOVERY ===")
    print("NOTE: Using Euclidean QR (not M-inner product) because M is indefinite.")
    for N in [100, 250, 500]:
        orthogonal_projection(N)

if __name__ == "__main__":
    main()
