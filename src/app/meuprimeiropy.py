nome  = input("Digite seu nome: ")
idade = input("Digite uma idade: ")

print("\nO nome digitado foi {}, seguido pela idade de {}.".format(nome, idade))

PI = 3.141592

while True:
	resposta_convertida = int(input("Qual o valor de PI? "))

	if resposta_convertida == PI:
		print("Você acertou...Parabéns\n{:.2f}".format(PI))
		break
	elif resposta_convertida < PI:
		print("O número PI é maior que o valor digitado!!")
	elif resposta_convertida > PI:
		print("O número PI é menor que o valor digitado!!")

rodada = 1

for rodada in range(1, 10, 2):
    print(rodada)

for rodada in [ 1, 2, 3, 4, 5 ]:
	print(rodada)


numero_secreto = 42
total_de_tentativas = 3

nivel = input(
    "Escolha o nível em que deseja jogar:"
    "\n1 - Facil | 2 - Intermediario | 3 - Dificil"
    "\nOpção? "
)

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa nº {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número: ")
    print("Você digitou o número ", chute)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!!!Parabéns")
        break
    elif (maior):
        print("Você errou. Seu chute foi maior que o número secreto")
    elif (menor):
        print("Você errou. Seu chute foi menor que o número secreto")

print("Fim do jogo.")