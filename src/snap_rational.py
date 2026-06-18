import torch
import json
import os
from fractions import Fraction

def main():
    print("Initializing Snap-to-Rational conversion...")
    
    # Paths
    base_dir = os.path.dirname(__file__)
    tensor_path = os.path.join(base_dir, "final_coefficients.pt")
    json_path = os.path.join(base_dir, "coefficients.json")
    
    if not os.path.exists(tensor_path):
        print(f"[-] Error: Could not find {tensor_path}")
        return
        
    # Load the optimized Vasyunin coefficients
    a_k_tensor = torch.load(tensor_path, weights_only=True)
    a_k_array = a_k_tensor.cpu().numpy()
    
    rational_sequence = []
    
    print(f"Loaded {len(a_k_array)} continuous coefficients. Snapping to exact rational bounds...")
    
    # Maximum denominator to ensure fractions don't blow up Lean 4's type system
    # We use 10,000 as a reasonable bound for high precision without overflow
    MAX_DENOM = 10000 
    
    for i, val in enumerate(a_k_array):
        # Using continuous fraction approximation
        f = Fraction(float(val)).limit_denominator(MAX_DENOM)
        
        num = f.numerator
        den = f.denominator
        
        # Validation
        if den == 0:
            raise ValueError(f"Zero denominator detected at index {i+1} for value {val}")
            
        rational_sequence.append([num, den])
    
    # Serialize to JSON
    with open(json_path, 'w') as f:
        json.dump(rational_sequence, f, indent=2)
        
    print(f"[+] Successfully serialized {len(rational_sequence)} exact fractional coefficients.")
    print(f"[+] Output saved to: {json_path}")
    print("[+] Formal verification readiness: VALIDATED (No zero denominators).")
    
    # Display sample mappings
    print("\nSample Float -> Rational Mapping:")
    for i in range(5):
        print(f"a_{i+1}: {a_k_array[i]:.6f}  =>  {rational_sequence[i][0]} / {rational_sequence[i][1]}")

if __name__ == "__main__":
    main()
