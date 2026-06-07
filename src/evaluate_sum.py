import json
import os
import math
from fractions import Fraction

def main():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "coefficients.json")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    a = [Fraction(num, den) for num, den in data]
    n = len(a)
    
    total_sum = Fraction(0, 1)
    for i in range(n):
        for j in range(n):
            idx_i = i + 1
            idx_j = j + 1
            gcd_val = math.gcd(idx_i, idx_j)
            M_val = Fraction(gcd_val * gcd_val, 2 * idx_i * idx_j)
            total_sum += a[i] * a[j] * M_val
            
    bound = Fraction(1, 230)
    print(f"Total Sum: {float(total_sum)} (Fraction: {total_sum})")
    print(f"Bound: {float(bound)} (Fraction: {bound})")
    if total_sum < bound:
        print("Sum IS strictly less than the structural bound.")
    else:
        print("Sum EXCEEDS the structural bound!")

if __name__ == "__main__":
    main()
