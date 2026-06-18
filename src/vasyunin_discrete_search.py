import json
import math
import random
from fractions import Fraction
import time
import os

def solve():
    N = 100
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "coefficients.json")
    out_path = os.path.join(base_dir, "discrete_coefficients.json")
    
    print(f"Starting Phase 12 Discrete Neurosymbolic Optimization for N={N}...")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    a = [Fraction(n, d) for n, d in data[:N]]
    
    # Precompute M exactly
    print("Precomputing exact GCD Matrix M_{i,j}...")
    M = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            u, v = i + 1, j + 1
            g = math.gcd(u, v)
            M[i][j] = Fraction(g * g, 2 * u * v)
            
    # Initial V vector: V_i = sum_j a_j M_i,j
    V = [Fraction(0) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            V[i] += a[j] * M[i][j]
            
    # Initial loss
    L = Fraction(0)
    for i in range(N):
        L += a[i] * V[i]
        
    initial_L = L
    print(f"\n[Baseline] Initial Exact Distance: {float(L):.8f}")
    
    # Verify constraint
    C = sum(a[i] / (i + 1) for i in range(N))
    print(f"[Constraint] Sum(a_k/k) Locked At: {float(C):.8f}")
    
    # Simulated Annealing Hyperparameters
    T = 1e-5
    T_min = 1e-10
    alpha = 0.99
    
    iters_per_temp = 1000
    best_L = L
    best_a = list(a)
    
    # Very fine, exact fractional perturbations
    step_sizes = [Fraction(1, 10000), Fraction(1, 50000), Fraction(1, 100000), Fraction(5, 100000)]
    
    accepted = 0
    total = 0
    
    start_time = time.time()
    print("\nInitiating Unchained Discrete Search...")
    
    generation = 0
    while T > T_min:
        generation += 1
        for _ in range(iters_per_temp):
            total += 1
            
            # Pick u and v for perturbation
            u_idx = random.randint(0, N - 1)
            v_idx = random.randint(0, N - 1)
            while u_idx == v_idx:
                v_idx = random.randint(0, N - 1)
                
            u = u_idx + 1
            v = v_idx + 1
            
            # delta is the step in the fractional space
            delta = random.choice([-1, 1]) * random.choice(step_sizes)
            
            # Constraint: delta_u / u + delta_v / v = 0
            # Ensures Sum(a_k / k) remains EXACTLY constant C
            delta_u = u * delta
            delta_v = -v * delta
            
            # Calculate EXACT Delta Loss
            dL = 2 * delta_u * V[u_idx] + 2 * delta_v * V[v_idx] + \
                 delta_u * delta_u * M[u_idx][u_idx] + \
                 delta_v * delta_v * M[v_idx][v_idx] + \
                 2 * delta_u * delta_v * M[u_idx][v_idx]
                 
            dL_float = float(dL)
            
            # Annealing Acceptance
            if dL_float < 0 or (T > 0 and random.random() < math.exp(-dL_float / T)):
                L += dL
                a[u_idx] += delta_u
                a[v_idx] += delta_v
                
                # Update V dynamically in O(N) instead of O(N^2)
                for i in range(N):
                    V[i] += delta_u * M[i][u_idx] + delta_v * M[i][v_idx]
                    
                accepted += 1
                
                if L < best_L:
                    best_L = L
                    best_a = list(a)
                    
        T *= alpha
        
        if generation % 25 == 0:
            print(f" Gen {generation} | Temp: {T:.2e} | Best L: {float(best_L):.8f} (Accepted: {accepted}/{total})")
        
    print("\n--- Discrete Optimization Complete ---")
    print(f"Time Elapsed: {time.time() - start_time:.2f}s")
    print(f"Final Exact L: {float(best_L):.8f}")
    
    if best_L < initial_L:
         print(f"-> SUCCESS: Dropped exact distance by {float(initial_L - best_L):.8e}")
    else:
         print("-> No improvement found.")
         
    # Final constraint verify
    final_C = sum(best_a[i] / (i + 1) for i in range(N))
    print(f"Final Constraint Verification: {float(final_C):.8f} == {float(C):.8f}")
    
    # Save best
    with open(out_path, 'w') as f:
        json.dump([[x.numerator, x.denominator] for x in best_a], f)
        
    print(f"Optimized discrete coefficients saved to {out_path}.")

if __name__ == '__main__':
    solve()
