import requests
from bs4 import BeautifulSoup
import json
import re

def clean_text(text):
    # Remove BOM and non-ASCII characters
    return re.sub(r'[^\x00-\x7F]+', '', text).strip()

url = "https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&distance=100"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Force UTF-8 decoding
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
results = soup.select("li.result-item")

facilities = []

for result in results:
    try:
        name = clean_text(result.select_one("h2.title").get_text(strip=True))
    except:
        name = ""

    try:
        address1 = clean_text(result.select_one("p.address1").get_text(strip=True))
    except:
        address1 = ""
    try:
        address2 = clean_text(result.select_one("p.address2").get_text(strip=True))
    except:
        address2 = ""
    try:
        address3 = clean_text(result.select_one("p.address3").get_text(strip=True))
    except:
        address3 = ""

    try:
        materials_html = result.select_one(".result-materials")

        matched_elements = materials_html.select("span.matched.material.no-link")
        materials_category = [clean_text(el.get_text(strip=True)) for el in matched_elements]

        accepted_elements = materials_html.select("span.material.no-link:not(.matched)")
        materials_accepted = [clean_text(el.get_text(strip=True)) for el in accepted_elements]
    except:
        materials_category = []
        materials_accepted = []

    facilities.append({
        "business_name": name,
        "last_update_date": "30-07-2025",
        "street_address1": address1,
        "street_address2": address2,
        "street_address3": address3,
        "materials_category": materials_category,
        "materials_accepted": materials_accepted
    })

# Save to JSON
with open("scraped_results_clean.json", "w", encoding="utf-8") as f:
    json.dump(facilities, f, indent=2, ensure_ascii=False)

print("✅ Cleaned data saved to scraped_results_clean.json")
