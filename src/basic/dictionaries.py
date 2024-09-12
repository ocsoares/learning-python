car = {
  "brand": "Gol",
  "year": 2005,
  "isAvailable": True
}

print("car brand: ", car["brand"])
print("car year: ", car["year"])
print("car isAvailable: ", car["isAvailable"])

listDictionariesCar = [
  {"brand": "Chevrolet", "year": 2010, "isAvailable": False},
  {"brand": "Camaro", "year": 2012, "isAvailable": True},
  {"brand": "Passant", "year": 2019, "isAvailable": False}
]

print("listDictionariesCar: ", listDictionariesCar)
print("listDictionariesCar Array 0 brand: ", listDictionariesCar[0]["brand"])
print("listDictionariesCar Array 1 year: ", listDictionariesCar[1]["year"])
print("listDictionariesCar Array 2 brand: ",
      listDictionariesCar[2]["isAvailable"])

emptyDictionary = []
emptyDictionary.append(
  {"brand": "Porshe", "year": 2014, "isAvailable": True})
print("emptyDictionary: ", emptyDictionary)
