import json
import csv
import os
import math

def moebius(n):
    if n == 1:
        return 1
    p = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p += 1
            n //= i
            if n % i == 0:
                return 0
    if n > 1:
        p += 1
    return 1 if p % 2 == 0 else -1

def omega(n):
    if n == 1:
        return 0
    count = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 1:
        count += 1
    return count

def main():
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "coefficients.json")
    
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    csv_path = os.path.join(base_dir, "riemann_data_custom.csv")
    
    with open(csv_path, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['x', 'mu', 'lnx', 'omega', 'y'])
        for i, (num, den) in enumerate(data[:100]):
            k = i + 1
            mu_k = moebius(k)
            lnx_k = math.log(k) if k > 0 else 0
            om_k = omega(k)
            a_k = num / den
            writer.writerow([k, mu_k, lnx_k, om_k, a_k])

    print(f"Generated {csv_path} (100 points, multivariate)")

if __name__ == "__main__":
    main()
