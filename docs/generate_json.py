import os
import json
# 1. ORODHA YA MAFOLDA YA CATEGORY ZAKE
folders_to_scan = [
    {
        "path": "docs/doc.html",
        "category": "Cases",
    },  # Badilisha iwe folda husika ya Cases kama ni saraka
    {
        "path": "docs/e-books.html",
        "category": "Books",
    },
    {
        "path": "docs/laws.html",
        "category": "Statute",
    },
    {
        "path": "docs/L.report.html",
        "category": "Law Reports",
    },  # Badilisha iwe folda husika ya L.report
]

output_json_file = "docs/laws.json"
laws_list = []
id_counter = 1

# 2. PITIA KILA FOLDA MOJA BAADA YA JINGINE
for folder_info in folders_to_scan:
    folder_path = folder_info["path"]
    category_name = folder_info["category"]

    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf"):
                title = os.path.splitext(filename)[0]
                file_link = f"{folder_path}/{filename}"
               
                item = {
                    "id": id_counter,
                    "title": title,
                    "category": category_name,
                    "link": file_link
                }
               
                laws_list.append(item)
                id_counter += 1
    else:
        print(f"Warning: File of '{folder_path}' not found (Script fail).")

# 3. HIFADHI MATOKEO YOTE KWENYE LAWS.JSON
with open(output_json_file, "w", encoding="utf-8") as f:
    json.dump(laws_list, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {len(laws_list)} items from the specified folders and saved to '{output_json_file}'.")