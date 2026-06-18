import numpy as np
import scipy.integrate as spi
import time

def generate_test_function(alpha, beta):
    """
    Generates a localized, highly oscillatory test function in the Sonin Space.
    g(x) must have compact support and its Mellin transform must vanish at +/- i/2.
    For this baseline, we use a Gaussian envelope multiplied by a highly oscillatory term.
    """
    def g(x):
        if x <= 0: return 0.0
        # Gaussian envelope centered at alpha, width beta, with oscillation
        envelope = np.exp(-((x - alpha)**2) / (2 * beta**2))
        oscillation = np.cos(100 * x) # high frequency oscillation
        return envelope * oscillation
    return g

def trace_formula_evaluation(g_func, integration_limit=10.0):
    """
    Numerically integrates the test function to evaluate Weil positivity.
    In reality, this involves the full Riemann-Weil explicit formula.
    For this baseline automated test, we evaluate the integral of |g(x)|^2
    to test the CPU bound and integration stability over highly oscillatory functions.
    """
    # Integrate |g(x)|^2 from 0 to integration_limit
    # Using a strict limit on subintervals to prevent CPU lockup as warned
    integral, error = spi.quad(lambda x: g_func(x)**2, 0.001, integration_limit, limit=500)
    return integral, error

if __name__ == "__main__":
    print("Initializing Sonin Space Test Function Generator...")
    start_time = time.time()
    
    alpha_param = 5.0
    beta_param = 0.5
    
    g = generate_test_function(alpha_param, beta_param)
    
    print("Integrating highly oscillatory test function...")
    val, err = trace_formula_evaluation(g, 10.0)
    
    elapsed = time.time() - start_time
    print(f"\n[+] Baseline Sonin Space integration complete in {elapsed:.2f}s")
    print(f"Integration Result: {val}")
    print(f"Estimated Error: {err}")
