print("--- Menu --- ")
print("1 - Diesel")
print("2 - Gasolina")
print("3 - Sair")
op = input("Digite o tipo de combustivel: ")

'''
Diesel
Até 25 litros, 5% de desconto
Acima de 25, 7,5% de desconto
Gasolina
Até 25 litros, 7% de desconto
Acima de 25 litros, 9% de desconto
'''
gasolina = 3
diesel = 2

if op== "1":
    print("escolheu 1")
    litros = float(input("Digite a qtd em litros: "))
    if litros<= 25:
        valor = litros*diesel
        desconto = valor*0.05

    else:
        valor = litros * diesel
        desconto = valor * 0.075


elif op=="2":
    print("escolheu 2")
    litros = float(input("Digite a qtd em litros: "))
    if litros<= 25:
        valor = litros*gasolina
        desconto = valor*0.07

    else:
        valor = litros * gasolina
        desconto = valor * 0.09


elif op=="3":
    print("sair")
else:
    print("opcao invalida")

valorFinal = valor - desconto
print("Valor a ser pago: R$ ", valorFinal)

