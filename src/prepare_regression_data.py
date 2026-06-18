import json
import csv
import os

def main():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "coefficients.json")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    full_csv = os.path.join(base_dir, "riemann_data_full.csv")
    core_csv = os.path.join(base_dir, "riemann_data_core.csv")
    
    # Write full 1000 points
    with open(full_csv, 'w', newline='') as f_full:
        writer = csv.writer(f_full)
        writer.writerow(['x', 'y'])
        for i, (num, den) in enumerate(data):
            k = i + 1
            a_k = num / den
            writer.writerow([k, a_k])
            
    # Write core 100 points
    with open(core_csv, 'w', newline='') as f_core:
        writer = csv.writer(f_core)
        writer.writerow(['x', 'y'])
        for i, (num, den) in enumerate(data[:100]):
            k = i + 1
            a_k = num / den
            writer.writerow([k, a_k])

    print(f"Generated {full_csv} (1000 points)")
    print(f"Generated {core_csv} (100 points)")

if __name__ == "__main__":
    main()
