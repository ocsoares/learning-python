manyNumbers = 102854945
print("manyNumbers: ", manyNumbers)

formatedManyNumbers = 102_854_945  # "_" é só VISUAL, n altera NADA
print("formatedManyNumbers: ", formatedManyNumbers)

print("hello" + " world")

name = "Pedro"
age = 25
country = "Brasil"
print(f"Info about Pedro, name: {name}, age: {age}, country: {country}")

# print("age: " + age)  # ERROR
print("age: " + str(age))
print("age: ", age)

anyText = "Apenas UMA FRase QUALquer !"
print("anyText LOWER: ", anyText.lower())
print("anyText UPPER: ", anyText.upper())
print("anyText find: ", anyText.find("FRas"))

fraseAtEnd = anyText[11:]  # A partir de "FRase" até o FINAL
print("fraseAtEnd: ", fraseAtEnd)

fraseUntilBeginning = anyText[:11]  # Da "FRase" até o COMEÇO
print("fraseUntilBeginning: ", fraseUntilBeginning)

changedText = anyText.replace("UMA", "ALTERADOOO")
print("changedText: ", changedText)

personName = "Thiago Alvarez Carvalho"
print("personName CAPITALIZE: ",
      personName.capitalize())  # APENAS a 1 Letra da primeira Palavra
print("personName TITLE: ", personName.title())  # Capitaliza TODAS as PALAVRAS
