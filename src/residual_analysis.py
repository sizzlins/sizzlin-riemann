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

def log_dft_sweep(r_N, k_array, y_vals, label):
    """Compute |sum r_k * k^(iy)| for each y."""
    log_k = np.log(k_array)
    spectrum = np.zeros(len(y_vals))
    for i, y in enumerate(y_vals):
        phase = y * log_k
        real_part = np.sum(r_N * np.cos(phase))
        imag_part = np.sum(r_N * np.sin(phase))
        spectrum[i] = math.sqrt(real_part**2 + imag_part**2)
    return spectrum

def find_and_print_peaks(y_vals, spectrum, label):
    import scipy.signal
    peaks, props = scipy.signal.find_peaks(spectrum, height=np.mean(spectrum) * 1.2, distance=30)
    
    print(f"\n--- {label} ---")
    if len(peaks) == 0:
        print("No significant peaks found above threshold.")
        return
    
    peak_y = y_vals[peaks]
    peak_amps = spectrum[peaks]
    sorted_idx = np.argsort(peak_amps)[::-1]
    
    for i in sorted_idx[:8]:
        print(f"  y = {peak_y[i]:8.4f}  (Amplitude: {peak_amps[i]:.6f})")

def main():
    print("=== PHASE 15: WINDOWED FREQUENCY CORRECTION ===")
    N = 1000
    t0 = time.time()
    M, L = build_system(N)

    # 1. Rebuild Hybrid Vector
    k_array = np.arange(1, N + 1, dtype=np.float64)
    v1 = 1.0 / (k_array**2)
    v2 = 1.0 / k_array
    
    v3 = np.zeros(N, dtype=np.float64)
    log_N = math.log(N)
    for k in range(1, N + 1):
        mu_k = mobius(k)
        if mu_k != 0:
            v3[k-1] = (mu_k / float(k)) * (1.0 - math.log(k) / log_N)

    V_mat = np.column_stack((v1, v2, v3))
    c = np.linalg.solve(V_mat.T @ M @ V_mat, V_mat.T @ L)
    a_hybrid = V_mat @ c

    # 2. Extract Residual Vector
    r_N = L - M @ a_hybrid
    
    print(f"\nResidual norm: {np.linalg.norm(r_N):.6f}")
    print(f"Residual max : {np.max(np.abs(r_N)):.6f}")

    # 3. Sweep range covering the first 3 known Riemann zeros
    y_vals = np.linspace(5, 35, 3000)
    
    # --- A: RAW (Rectangular Window / No Window) ---
    spec_raw = log_dft_sweep(r_N, k_array, y_vals, "Raw")
    find_and_print_peaks(y_vals, spec_raw, "RAW (No Window)")
    
    # --- B: BLACKMAN WINDOW ---
    window_blackman = np.blackman(N)
    r_blackman = r_N * window_blackman
    spec_blackman = log_dft_sweep(r_blackman, k_array, y_vals, "Blackman")
    find_and_print_peaks(y_vals, spec_blackman, "BLACKMAN WINDOW")
    
    # --- C: HANN WINDOW (for comparison) ---
    window_hann = np.hanning(N)
    r_hann = r_N * window_hann
    spec_hann = log_dft_sweep(r_hann, k_array, y_vals, "Hann")
    find_and_print_peaks(y_vals, spec_hann, "HANN WINDOW")
    
    print(f"\nKnown Riemann Zeros: 14.1347, 21.0220, 25.0108, 30.4249")
    print(f"Execution Time: {time.time() - t0:.2f} s")

if __name__ == "__main__":
    main()
