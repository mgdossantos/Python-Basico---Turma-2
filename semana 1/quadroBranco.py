#Comando de saida de dados
print
print("Ola Mundo Python!!!")
print("Marcela dos Santos")
print("Tutoria Python Basico \nTurma 2")

#input
nome=input("Digite seu nome: ")
sobrenome = input("Digite o sobrenome: ")
print("Seja bem-vindo ",nome,"!!")
print(nome," ", sobrenome)


anoNascimento=input("Digite o ano do seu nascimento: ")
#Toda vez que voce precisa pedir informacao/digite alg
# precisa usar input
#sempre o input recebe como valor uma variavel do tipo
# texto (String)
anoAtual = 2025
idade = anoAtual -int(anoNascimento)
print(idade, "anos!!")
