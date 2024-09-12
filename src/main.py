print("Learn PYTHON !")

printInt = 10
print("testInt:", printInt)

ifInt = 20
otherInfInt = 30

if ifInt >= 20:
  print("MAIOR ou igual a 20")
else:
  print("MENOR")

nullValue = None
if not nullValue:
  print("nullValue NÃO existe !")

# Usar "and" ao invés de "&", o "&" é só com BINÁRIOS
if (ifInt > 87 and otherInfInt > 18):
  print("MAIOR q 15 e 18")
elif (ifInt >= 20 and otherInfInt >= 25):
  print("MAIOR e igual a 20, e a 25 !")
