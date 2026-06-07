import mpmath
import sys
import time

# Set high precision for mpmath
mpmath.mp.dps = 50

def nicolas_criterion_stream(limit_k):
    """
    Evaluates the Nicolas Criterion: N_k / phi(N_k) > e^gamma * ln(ln(N_k))
    To avoid memory blowouts, we do not compute N_k directly.
    Instead:
    N_k / phi(N_k) = Product_{i=1}^k (1 - 1/p_i)^{-1}
    ln(N_k) = Sum_{i=1}^k ln(p_i)
    
    We stream the primes and keep running totals.
    """
    print(f"Starting Nicolas Criterion evaluation up to {limit_k} primes...")
    
    gamma = mpmath.mp.euler
    exp_gamma = mpmath.exp(gamma)
    
    # Running variables
    product_ratio = mpmath.mpf(1.0)
    ln_Nk = mpmath.mpf(0.0)
    
    start_time = time.time()
    
    # Sieve of Eratosthenes generator
    def prime_generator():
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    primes = prime_generator()
    
    for k in range(1, limit_k + 1):
        p = next(primes)
        mp_p = mpmath.mpf(p)
        
        # Update running values
        product_ratio *= (mpmath.mpf(1.0) / (mpmath.mpf(1.0) - mpmath.mpf(1.0)/mp_p))
        ln_Nk += mpmath.log(mp_p)
        
        if k > 1:
            rhs = exp_gamma * mpmath.log(ln_Nk)
            
            # The criterion says LHS > RHS for all k. 
            # If LHS <= RHS, we found a violation!
            if product_ratio <= rhs:
                print(f"\n[!] VIOLATION FOUND at k={k}, prime={p}")
                print(f"LHS = {product_ratio}")
                print(f"RHS = {rhs}")
                return
            
        if k % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"Processed {k} primes... Current p={p}. Elapsed: {elapsed:.2f}s")
            
    print(f"\n[+] Baseline test completed successfully. No violations found up to {limit_k} primes.")
    print(f"Final LHS: {product_ratio}")
    print(f"Final RHS: {rhs}")

if __name__ == "__main__":
    # Baseline test with 100,000 primes
    nicolas_criterion_stream(100000)
