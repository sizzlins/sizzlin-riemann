import numpy as np
import mpmath
import matplotlib.pyplot as plt

def zeta_magnitude(s_real, s_imag):
    """
    Computes the magnitude of the Riemann Zeta function at s = s_real + i*s_imag.
    Uses mpmath for arbitrary-precision arithmetic.
    """
    mpmath.mp.dps = 25  # Set decimal places for precision
    s = complex(s_real, s_imag)
    zeta_val = mpmath.zeta(s)
    return abs(zeta_val)

def antigravity_loss(s_real, s_imag, lambda_penalty=1.0):
    """
    Computes a loss function that includes a repulsive force away from Re(s) = 1/2.
    The agent will try to minimize this loss.
    
    Loss = |zeta(s)| - lambda * penalty(Re(s))
    """
    mag = zeta_magnitude(s_real, s_imag)
    # Simple antigravity: push away from 0.5
    penalty = (s_real - 0.5)**2
    return mag - lambda_penalty * penalty

if __name__ == "__main__":
    print("Riemann Zeta Optimization Environment Initialized.")
    # Example computation on the critical line
    t = 14.1347251417  # First non-trivial zero
    print(f"|Zeta(0.5 + {t}i)| = {zeta_magnitude(0.5, t)}")
