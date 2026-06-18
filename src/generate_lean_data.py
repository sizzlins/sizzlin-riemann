import json
import os
import math
from fractions import Fraction

def main():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "coefficients.json")
    lean_path = os.path.join(base_dir, "..", "proof", "CoefficientsData.lean")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    lean_array_items = []
    for num, den in data:
        # Lean 4 representation of Rat, can be written as num / den
        lean_array_items.append(f"({num} : Rat) / {den}")
        
    lean_array_str = ", ".join(lean_array_items)
    
    # Calculate a conservative lower bound for C / ln(1000). Assuming C=1, 1/ln(1000) ~ 0.14476
    # Let's say 14 / 100
    
    content = f"""import Mathlib.Data.Rat.Basic

/-- Auto-generated array of 1000 continuous fraction coefficients from PyTorch --/
def vasyunin_json_array : Array Rat := #[{lean_array_str}]
"""
    with open(lean_path, 'w') as f:
        f.write(content)
        
    print(f"Successfully generated CoefficientsData.lean with {len(data)} items.")

if __name__ == "__main__":
    main()
