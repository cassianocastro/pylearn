palavra_secreta  = "banana"
letras_acertadas = ['_','_','_','_','_','_']
acertou          = False
enforcou         = False
erros            = 0

print(letras_acertadas)

while (not acertou and not enforcou):
    chute = input("Letra? ")

    if (chute in palavra_secreta):
        posicao = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
                print("Letra {} encontrada na posição {} da palavra secreta".format(letra, posicao))
            posicao += 1
    else:
        erros += 1

    acertou  = "_" not in letras_acertadas
    enforcou = erros == 6

    print(letras_acertadas)

if (acertou):
    print("Você ganhou!!")
else:
    print("Você perdeu...")
print("Fim do jogo")