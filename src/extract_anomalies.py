import os

def extract_findings():
    files = ["conversation 1.txt", "conversation 2.txt"]
    keywords = [
        "finding", "revelation", "anomaly", "we proved", "this proves",
        "failure mode", "discovery", "autopsy", "limit", "artifact", 
        "shattered", "conclusion", "critical finding", "verdict", "phenomenon"
    ]
    
    extracted = []
    
    for filename in files:
        filepath = os.path.join("C:/Users/LOQ/PycharmProjects/sizzlin-riemann", filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            
        current_paragraph = []
        start_line = 1
        
        for i, line in enumerate(lines):
            line_num = i + 1
            if line.strip() == "":
                if current_paragraph:
                    p = "".join(current_paragraph).strip()
                    p_lower = p.lower()
                    if any(k in p_lower for k in keywords) and len(p.split()) > 15:
                        extracted.append(f"--- SOURCE: {filename} (Line {start_line}) ---\n{p}\n")
                    current_paragraph = []
                start_line = line_num + 1
            else:
                current_paragraph.append(line)
                
        # Catch the last paragraph if file doesn't end with newline
        if current_paragraph:
            p = "".join(current_paragraph).strip()
            p_lower = p.lower()
            if any(k in p_lower for k in keywords) and len(p.split()) > 15:
                extracted.append(f"--- SOURCE: {filename} (Line {start_line}) ---\n{p}\n")
                    
    out_path = "C:/Users/LOQ/PycharmProjects/sizzlin-riemann/extracted_anomalies.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(extracted))
        
    print(f"Extracted {len(extracted)} potential findings to extracted_anomalies.txt")

if __name__ == "__main__":
    extract_findings()
