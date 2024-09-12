def sum_function(number: int, other_number: int):
  return number + other_number


print("sumFunction: ", sum_function(10, 25))

# Passando o NOME do PARÂMETRO Diretamente
print("sumFunction EXPLICIT: ", sum_function(30, other_number=102))


# Retorna uma TUPLA -> Mesma coisa q uma LISTA, mas é IMUTÁVEL !
def return_many_values(any, other_any, another_any):
  return any, other_any, another_any


response = return_many_values("Qualquer coisa", 2030, [1, 2, 3])
print("response: ", response)
print("response 1: ", response[0])
print("response 2: ", response[1])
print("response 3: ", response[2])
