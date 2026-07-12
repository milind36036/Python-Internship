import json

car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2024,
    "color": "Black"
}

# Write JSON
with open("car.json", "w") as file:
    json.dump(car, file, indent=4)

# Read JSON
with open("car.json", "r") as file:
    data = json.load(file)

print(data)