import os
import json

# 1. ORODHA YA MAFOLDA NA CATEGORY ZAKE
# Weka majina ya mafolda yako na category unayotaka itokeze kwenye search
folders_to_scan = [
    {"path": "doc.html", "category": "Cases"},
    {"path": "e-books.html", "category": "Books"},
    {"path": "laws.html", "category": "Statute"},
]

output_json_file = "laws.json"
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
        print(f"⚠️ Taarifa: Folda la '{folder_path}' halijapatikana (Script imeliruka).")

# 3. HIFADHI MATOKEO YOTE KWENYE LAWS.JSON
with open(output_json_file, "w", encoding="utf-8") as f:
    json.dump(laws_list, f, indent=2, ensure_ascii=False)

print(f"✅ Umefanikiwa! Jumla ya mafaili {len(laws_list)} kutoka kwenye mafolda yote yameifadhiwa kwenye '{output_json_file}'.")