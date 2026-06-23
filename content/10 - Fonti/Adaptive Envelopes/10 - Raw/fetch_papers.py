import urllib.request
import urllib.parse
import json
import os

# Create directory if it doesn't exist
out_dir = r"d:\Vaults\Research\Research\10 - Fonti\Adaptive Envelopes\10 - Raw"
os.makedirs(out_dir, exist_ok=True)

query = '("adaptive facade" OR "kinetic building envelope" OR "dynamic shading") AND ("machine learning" OR "predictive control" OR "IoT" OR "artificial intelligence") AND (PUB_YEAR:2024 OR PUB_YEAR:2025 OR PUB_YEAR:2026) AND OPEN_ACCESS:y'
encoded_query = urllib.parse.quote(query)
url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={encoded_query}&format=json&resultType=core"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
        results = data.get('resultList', {}).get('result', [])
        print(f"Found {len(results)} results")
        
        count = 0
        for r in results:
            if count >= 3:
                break
                
            pmcid = r.get('pmcid')
            if not pmcid:
                continue
                
            print(f"Downloading PMCID: {pmcid}")
            pdf_url = f"https://europepmc.org/articles/{pmcid}?pdf=render"
            out_file = os.path.join(out_dir, f"{pmcid}.pdf")
            
            try:
                urllib.request.urlretrieve(pdf_url, out_file)
                print(f"Saved to {out_file}")
                count += 1
            except Exception as e:
                print(f"Failed to download {pmcid}: {e}")

except Exception as e:
    print(f"API request failed: {e}")
