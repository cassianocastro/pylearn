lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

maior = lista[0]
menor = lista[0]
pares = []
ocorrencias_item_1 = 0
media              = 0
soma_negativos     = 0

for index in range (0, len(lista)):
    if (maior < lista[index]):
        maior = lista[index]
    if (menor > lista[index]):
        menor = lista[index]
    if (lista[index] % 2 == 0):
        pares.append (lista[index])
    if (lista[index] == lista[0]):
        ocorrencias_item_1 += 1
    if (lista[index] < 0):
        soma_negativos = soma_negativos + lista[index]

    media = media + lista[index]

media = media / len (lista)

print("Maior valor: " + str(maior))
print("Menor valor: " + str(menor))
print("Lista de números pares: " + str(pares))
print("Número do ocorrencias do item 1: " + str(ocorrencias_item_1))
print("Média dos números: " + str(media))
print("Soma do números negativos: " + str(soma_negativos))

def velocidade_media(espaco, tempo):
    velocidade = espaco / tempo
    print("Velocidade media: {} m/s".format(velocidade))

def dados(nome, idade = None):
    print("Nome: {}".format(nome))

    if (idade is not None):
        print("Idade: {}".format(idade))
    else:
        print("Idade não informada.")

def velocidade(espaco, tempo):
    velocidade = espaco / tempo

    return velocidade

resultado = velocidade(100, 20)
print(resultado)

aceleracao = velocidade(100, 20) / 20
print(aceleracao)

def dados_pessoais(nome, idade = None):
    if (idade is not None):
        return "Nome: {} \nIdade: {}".format(nome, idade)
    else:
        return "Nome: {} \nIdade não informada.".format(nome)

def calculadora(x, y):
    return x + y, x - y

print(calculadora(1, 2))
print(type(calculadora(1, 2)))

def calculadora1(x, y):
    return { "Soma": x + y, "Subtracao": x - y }

resultados = calculadora1(1, 2)

for key in resultados:
    print("{}: {}".format(key, resultados[key]))
# soma: 3
# subtracao: -1

def teste(arg, *args):
    print("Primeiro argumento normal: {}".format(arg))

    for arg in args:
        print("Outro argumento: {}".format(arg))

teste("Python", "is", "very", "cool")

# lista = ["is", "very", "cool"]
# teste("Python", *lista)
# tupla = ("is", "very", "cool")
# teste("Python", *tupla)