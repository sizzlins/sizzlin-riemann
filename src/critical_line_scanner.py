import math
import mpmath
import time

def compute_hybrid_A(N, s, c1, c2, c3):
    """
    Computes A_N(s) = sum_{k=1}^N a_k * k^s
    where a_k = c1/k^2 + c2/k + c3 * (mu(k)/k) * (1 - ln(k)/ln(N))
    using mpmath for arbitrary precision.
    """
    A = mpmath.mpc(0, 0)
    log_N = math.log(N)
    
    # We need moebius values. mpmath doesn't have a direct mobius function, 
    # so we'll use sympy's mobius.
    from sympy import mobius
    
    for k in range(1, N + 1):
        # Calculate a_k
        geom1 = c1 / (k**2)
        geom2 = c2 / k
        
        mu_k = mobius(k)
        if mu_k != 0:
            taper = 1.0 - (math.log(k) / log_N)
            mollifier = c3 * (mu_k / k) * taper
        else:
            mollifier = 0.0
            
        a_k = geom1 + geom2 + mollifier
        
        # Add a_k * k^s to the sum
        term = a_k * mpmath.power(k, s)
        A += term
        
    return A

def main():
    print("=== PHASE 14: THE CRITICAL LINE SWEEP ===")
    t0 = time.time()
    
    # Set precision
    mpmath.mp.dps = 25
    
    # N=1000 hybrid constants from Phase 12
    N = 1000
    c1 = 1.065012
    c2 = 0.004867
    c3 = -1.449563
    
    print(f"Sweeping s = 0.5 + iy  for y in [0, 30] ...\n")
    print(f"{'y':<10} | {'|zeta(s)|':<15} | {'|1 + zeta(s) * A_N(s)|':<20}")
    print("-" * 50)
    
    import numpy as np
    y_vals = np.linspace(0.1, 30.0, 60)
    
    for y in y_vals:
        s = mpmath.mpc(0.5, y)
        
        # 1. Evaluate zeta(s)
        z = mpmath.zeta(s)
        mag_z = mpmath.absmax(z)
        
        # 2. Evaluate Zeta Bridge: 1 + zeta(s)*A_N(s)
        A = compute_hybrid_A(N, s, c1, c2, c3)
        bridge = 1.0 + z * A
        mag_bridge = mpmath.absmax(bridge)
        
        print(f"{y:<10.4f} | {float(mag_z):<15.6f} | {float(mag_bridge):<20.6f}")
        
    print(f"\nExecution Time: {time.time() - t0:.2f} s")

if __name__ == "__main__":
    main()
