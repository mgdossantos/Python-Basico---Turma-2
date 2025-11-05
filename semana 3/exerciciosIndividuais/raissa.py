'''
Faça um programa que ajude a controlar os
gastos do mês.
O programa deve perguntar quanto você gastou
em cada compra.
A digitação continua enquanto o valor for
diferente de 0.
No final, o programa deve mostrar:
O total gasto no mês;
A quantidade de compras realizadas;
A média de gastos;
Quantas compras ultrapassaram R$ 100

'''
gastoCompra=-1
total = 0
qtdCompras=0
comprasMaiores100=0
while gastoCompra!=0:
    gastoCompra = float(input("Quanto voce gastou?"))
    if gastoCompra!=0:
        qtdCompras = qtdCompras+1
        total = total + gastoCompra
    if gastoCompra > 100:
        #contando de 1 em 1 toda vez q o gasto for maior que 100
        comprasMaiores100 = comprasMaiores100 + 1



print(qtdCompras)