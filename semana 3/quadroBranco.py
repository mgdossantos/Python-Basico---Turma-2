# contador = 0
#
# while contador <5 :
#     print(contador)
#     contador = contador +1
#
# # teste de senha
# senha="python123"
# senhaDigitada = input("Digite a senha: ")
# while senhaDigitada!=senha:
#     senhaDigitada = input("Tente novamente: ")
#
# print("sai do loop")

lista = "Titulo da Lista"
atualizacao = input ("Digite um nome:")
while atualizacao != "fim" :
  lista = lista + "\n" + atualizacao
  atualizacao = input ("Digite um nome:")

print(lista)