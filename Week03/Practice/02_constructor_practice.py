class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Tata", "Nano", 2016)

print(car1.brand)
print(car1.model)
print(car1.year)