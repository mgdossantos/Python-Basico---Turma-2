'''
Faça um programa que pergunte a quantidade de notas que serão digitadas.
Depois, use um loop while para ler cada nota, somar todas e
calcular a média final.
No final, o programa deve informar:
a média do aluno, e
se ele foi Aprovado, Recuperação ou Reprovado.

'''
#entrada: qtd de notas, notas

#processamento:
#media= somatorio de todas as notas / qtd

#saida: media, situacao do aluno
#0-4.9
#5 - 6 rec
#6.1 - aprovado

qtdNotas = int(input("Digite a quantidade de notas: "))
cont=0
soma = 0
while cont<qtdNotas:
    nota = float(input("Digite a nota: "))
    soma = soma +nota
    cont=cont+1
    #print(qtdNotas,"-",cont,"-", soma)
media = soma / qtdNotas
print(media)