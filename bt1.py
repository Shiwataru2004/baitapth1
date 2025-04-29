import requests
import csv

# Bước 1: Lấy dữ liệu JSON từ API
url = "https://www.pokemon.com/us/api/pokedex/kalos"
response = requests.get(url)
data = response.json()

# Bước 2: Ghi các trường mong muốn vào file CSV
csv_filename = "kalos_pokemon.csv"
fields = ["number", "height", "weight", "name", "type", "ThumbnailImage"]

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for pokemon in data:
        writer.writerow({
            "number": pokemon.get("number"),
            "height": pokemon.get("height"),
            "weight": pokemon.get("weight"),
            "name": pokemon.get("name"),
            "type": ', '.join(pokemon.get("type", [])),  # chuyển list thành chuỗi
            "ThumbnailImage": pokemon.get("ThumbnailImage")
        })

print(f"Dữ liệu đã được lưu vào {csv_filename}")

# Bước 3: Lọc ra các Pokémon có type là poison
print("\nCác Pokémon có hệ poison:")
with open(csv_filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        types = row["type"].lower().split(', ')
        if "poison" in types:
            print(f'{row["name"]} (Số: {row["number"]}, Type: {row["type"]})')