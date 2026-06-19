import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

queries = {
    1: 'all:"Nyman-Beurling" AND all:"Euler totient"',
    2: 'all:"Baez-Duarte" AND all:"asymptotic" AND all:"0.22"',
    3: 'all:"Riemann zeros" AND all:"11.86"',
    4: 'all:"Nyman-Beurling" AND all:"Galerkin"',
    5: 'all:"Vasyunin" AND all:"divisor function"',
    6: 'all:"Baez-Duarte" AND all:"negative eigenvalues"',
    7: 'all:"Baez-Duarte" AND all:"Gram-Schmidt"',
    8: 'all:"Nyman-Beurling" AND all:"Ansatz"',
    9: 'all:"Nyman-Beurling" AND all:"Dirichlet"',
    10: 'all:"symbolic regression" AND all:"Riemann"',
    11: 'all:"Nyman-Beurling" AND all:"rank one"',
    12: 'all:"Mellin transform" AND all:"fractional part" AND all:"bounded domain"',
    13: 'all:"Runge\'s phenomenon" AND all:"prime"',
    14: 'all:"Nyman-Beurling" AND all:"Totient"',
    15: 'all:"Beurling-Nyman" AND all:"neural network"',
    16: 'all:"multicollinearity" AND all:"number theory"',
    17: 'all:"Baez-Duarte" AND all:"negative"',
    18: 'all:"Baez-Duarte" AND all:"subspace"',
    19: 'all:"Baez-Duarte" AND all:"numerical integration"'
}

def search_arxiv(query):
    # urlencode
    q = urllib.parse.quote(query)
    url = f'http://export.arxiv.org/api/query?search_query={q}&start=0&max_results=5'
    try:
        data = urllib.request.urlopen(url).read()
        root = ET.fromstring(data)
        # Find entry tags
        entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        
        # If hits found, extract titles
        titles = []
        for entry in entries:
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            titles.append(title.strip().replace('\n', ' '))
        return len(entries), titles
    except Exception as e:
        print(f"Error querying {query}: {e}")
        return -1, []

print("--- ArXiv Literature Sweep ---")
for num, query in queries.items():
    count, titles = search_arxiv(query)
    print(f"Finding {num:02d} | Hits: {count} | Query: {query}")
    if count > 0:
        for t in titles[:2]:
            print(f"  -> {t}")
    time.sleep(1) # rate limit

print("Sweep Complete.")
