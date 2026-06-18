import math
from fractions import Fraction
import random
import time
import os

def precompute_M(N):
    M = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            g = math.gcd(i, j)
            # Exact integral of {ix}{jx} dx = gcd(i,j)^2 / (12ij) + 1/4
            M[(i, j)] = Fraction(g**2, 12 * i * j) + Fraction(1, 4)
    return M

def energy(a, M, N):
    # d_N^2 = 1 - 2 sum a_k L_k + sum a_i a_j M_{i,j}
    # L_k = 1/2
    E = Fraction(1, 1)
    
    linear_sum = Fraction(0, 1)
    for k in range(1, N + 1):
        linear_sum += a[k] * Fraction(1, 2)
    
    E -= 2 * linear_sum
    
    quad_sum = Fraction(0, 1)
    for i in range(1, N + 1):
        if a[i] == 0: continue
        for j in range(1, N + 1):
            if a[j] == 0: continue
            quad_sum += a[i] * a[j] * M[(i, j)]
            
    E += quad_sum
    return E

def anneal(N, iterations=1000, initial_temp=2.0, cooling_rate=0.999):
    M = precompute_M(N)
    
    # Initialize a_k
    a = {k: Fraction(0, 1) for k in range(1, N + 1)}
    a[1] = Fraction(1, 1)
    
    current_energy = energy(a, M, N)
    best_a = a.copy()
    best_energy = current_energy
    
    temp = initial_temp
    
    start_time = time.time()
    print(f"Starting discrete annealing for N={N} (Sawtooth Basis)")
    
    for i in range(iterations):
        idx1, idx2 = random.sample(range(1, N + 1), 2)
        
        # Mutation step keeping sum(a_k/k) constant
        den = random.randint(1, 50)
        s = Fraction(random.choice([-1, 1]), den)
        
        new_a = a.copy()
        new_a[idx1] += s * idx1
        new_a[idx2] -= s * idx2
        
        new_energy = energy(new_a, M, N)
        delta_e = new_energy - current_energy
        
        if delta_e < 0 or (temp > 0 and random.random() < math.exp(-float(delta_e) / temp)):
            a = new_a
            current_energy = new_energy
            if current_energy < best_energy:
                best_energy = current_energy
                best_a = a.copy()
                
        temp *= cooling_rate
        
        if (i+1) % (iterations // 5) == 0:
            print(f"Iter {i+1}/{iterations} | Temp: {temp:.4f} | Best Energy: {float(best_energy):.6f}")
            
    print(f"Finished N={N} in {time.time() - start_time:.2f}s")
    print(f"Best Energy: {best_energy} (~{float(best_energy):.6f})\n")
    return best_a

if __name__ == '__main__':
    best_10 = anneal(10, iterations=2000)
    print("N=10 Best a_k:", best_10)
    
    best_20 = anneal(20, iterations=5000)
    print("N=20 Best a_k:", best_20)
    
    output_path = os.path.join(os.path.dirname(__file__), 'discrete_results.csv')
    with open(output_path, 'w') as f:
        f.write("N,k,a_k\n")
        for k, v in best_10.items():
            f.write(f"10,{k},{float(v)}\n")
        for k, v in best_20.items():
            f.write(f"20,{k},{float(v)}\n")
    print(f"Saved results to {output_path}")
