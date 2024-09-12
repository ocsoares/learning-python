# Usar TUPLAS para Valores FIXOS
name_age = ("Carlos", 32)
print("name_age", name_age)


# Retorna uma TUPLA -> Mesma coisa q uma LISTA, mas é IMUTÁVEL !
def return_many_values(any, other_any, another_any):
  return any, other_any, another_any


response = return_many_values("Qualquer coisa", 2030, [1, 2, 3])
print("response: ", response)
print("response 1: ", response[0])
print("response 2: ", response[1])
print("response 3: ", response[2])

# DESESTRUTURAÇÃO da TUPLA
first, second, third = response
print("first RESPONSE: ", first)
print("second RESPONSE: ", second)
print("third RESPONSE: ", third)
