intList = [20, 30, 50, 200, 35, 83, 4]
print("intList: ", intList)
print("sum ALL LIST: ", sum(intList))
print(20 in intList)
print(24 in intList)

intList.sort()
print("intList SORTED ", intList)

# "sorted" para pegar o RETORNO em outra Variável !!
intListReverseSorted = sorted(intList, reverse=True)
print("intListReverseSorted: ", intListReverseSorted)

elementsList = [10, 32, "Qlq texto", 200, 345]
print("elementsList: ", elementsList)

print("elementsList[0]: ", elementsList[0])
print("elementsList[2]: ", elementsList[2])

elementsList[0] = "Alterado"
print("elementsList[0] ALTERADO: ", elementsList[0])

emptyList = []
emptyList.append("Colocado")
emptyList.append("Colocado2")
print("emptyList: ", emptyList)

print("len intList: ", len(intList))
print("min intList: ", min(intList))
print("max intList: ", max(intList))
