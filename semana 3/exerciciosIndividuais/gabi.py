'''
Crie um programa que ajude a contar quantos materiais
 recicláveis foram coletados durante o dia.
O programa deve perguntar o tipo de material
 (papel, plástico, vidro, metal...).
A digitação deve continuar até o usuário digitar
“fim”.
No final, o programa mostra:
o total de itens coletados, e
uma mensagem de incentivo à sustentabilidade.

'''
op=0
papel= 0
plastico = 0
while op!="5":
    print("-- Menu --")
    print("1 - papel")
    print("2 - plastico")
    print("3 - vidro")
    print("4 - metal")
    print("5 - sair")
    op=input("Qual o tipo de material que voce estah depositando? ")
    #print(op)
    if op=="1":
        papel=papel+1
    if op=="2":
        plastico=plastico+1