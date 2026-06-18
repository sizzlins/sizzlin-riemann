import numpy as np
from scipy.stats import linregress

# Raw data from Phase 6 sweep
N_vals = np.array([100, 250, 500, 1000], dtype=float)
c1_vals = np.array([-2.432487, -2.697262, -2.892284, -3.049978])
c2_vals = np.array([2.611015, 2.957218, 3.199252, 3.391324])
E_vals = np.array([1.11677474e+00, 1.30900055e+00, 1.43503282e+00, 1.53268839e+00])

log_N = np.log(N_vals)

# Log-linear regression: c(N) = alpha * log(N) + beta
res_c1 = linregress(log_N, c1_vals)
res_c2 = linregress(log_N, c2_vals)
res_E = linregress(log_N, E_vals)

print("=== PHASE 7: MASTER EQUATION PARAMETERIZATION ===\n")

print(f"c1(N) = {res_c1.slope:.6f} * ln(N) + ({res_c1.intercept:.6f})")
print(f"  R² = {res_c1.rvalue**2:.8f}")

print(f"\nc2(N) = {res_c2.slope:.6f} * ln(N) + ({res_c2.intercept:.6f})")
print(f"  R² = {res_c2.rvalue**2:.8f}")

print(f"\nE_N   = {res_E.slope:.6f} * ln(N) + ({res_E.intercept:.6f})")
print(f"  R² = {res_E.rvalue**2:.8f}")

print("\n--- MASTER EQUATION ---")
print(f"a_k(N) = [({res_c1.slope:.4f} ln N + ({res_c1.intercept:.4f})) "
      f"+ ({res_c2.slope:.4f} ln N + ({res_c2.intercept:.4f})) * d(k)] / k^2")

# Verify: reconstruct c1, c2 from fit and compare
print("\n--- FIT VERIFICATION ---")
for i, N in enumerate(N_vals):
    c1_fit = res_c1.slope * np.log(N) + res_c1.intercept
    c2_fit = res_c2.slope * np.log(N) + res_c2.intercept
    print(f"N={int(N):5d}  c1_actual={c1_vals[i]:.6f}  c1_fit={c1_fit:.6f}  "
          f"c2_actual={c2_vals[i]:.6f}  c2_fit={c2_fit:.6f}")
