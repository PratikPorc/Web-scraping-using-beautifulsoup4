# ♻️ Earth911 Recycling Center Scraper

This project scrapes recycling center data from [Earth911.com](https://search.earth911.com/) using Python, `requests`, and `BeautifulSoup`. It extracts essential details such as:

- Business name  
- Address  
- Materials accepted  

The data is exported in **JSON format** for further analysis or reuse.

---

## 📌 Features

- 🔍 Search centers by material type and ZIP code  
- 📥 Extract business name, address, and materials accepted  
- 🧼 Clean and structured output  
- 💾 Exported as `scraped_results_clean.json`  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/earth911-materials-scraper.git
cd earth911-materials-scraper
````

### 2. Install dependencies

Make sure you have Python 3 installed.

```bash
pip install -r requirements.txt
```

### 3. Run the scraper

```bash
python main.py
```

This will save the results in a file called `scraped_results_clean.json`.

---

## 📂 Project Structure

```
.
├── main.py         # Main scraping script
├── scraped_results_clean.json        # Scraped data (auto-generated)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## 🧪 Example Output

```json
[
  {
    "business_name": "New York City Bulk Item Curbside Program",
    "last_update_date": "30-07-2025",
    "street_address1": "",
    "street_address2": "",
    "street_address3": "New York, NY 10001",
    "materials_category": [
      "Dehumidifiers",
      "Humidifiers"
    ],
    "materials_accepted": [
      "Air Conditioners",
      "Barbeque Grills",
      "Carpet",
      "Carpet Padding",
      "Dishwashers"
    ]
  }
]
```

---

## ⚠️ Notes

* This scraper works for **public, server-rendered content**. If Earth911 changes their site structure or hides data behind JavaScript, the scraper may need to be updated or switched to Selenium/Playwright.
* Respect the website's terms of service when scraping.

---

## 👨‍💻 Author

Made with ♥ by [Your Name](https://github.com/PratikPorc)
Feel free to contribute or open issues!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


