import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta  = carrega_palavra_secreta()
    letras_acertadas = inicializar_letras(palavra_secreta)

    enforcou = False
    acertou  = False
    erros    = 0

    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou  = '_' not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu.")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    return chute

def inicializar_letras(palavra):
    return ['_' for letra in palavra]

def carrega_palavra_secreta():
    try:
        raise NameError("oi")

        arquivo  = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    except IOError:
        print("Não foi possível abrir o arquivo.")
    except NameError:
        print("Foi lançada uma exceção.")
        raise
    else:
        print("O arquivo tem {} palavras.".format(len(arquivo.readlines())))
    finally:
        arquivo.close()

    numero           = random.randrange(0, len(palavras))
    palavra_secreta  = palavras[numero].upper()

    return palavra_secreta

def imprime_mensagem_abertura():
    print("***Bem vindo ao jogo da Forca!***")