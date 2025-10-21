#Pedir para o usuário o valor a converter
realBrasileiro = float(input("Digite o valor em R$: "))
#Pedir para o usuário a taxa de conversão
taxaConversao = float(input("Digite a taxa de conversao: "))
#Fazer o cálculo: Dólar Canandense = Real *Taxa
dolarCanadense = realBrasileiro * taxaConversao
#Mostrar Dólar Canadense
print("CAD: ",dolarCanadense)
