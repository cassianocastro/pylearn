#! /usr/bin/env python3.10

def getBits(numero):
	qtdeBits, quociente, resto = 0, 0, []

	quociente = numero // 2
	resto.append(numero % 2)

	while quociente >= 2:
		resto.append(quociente % 2)
		quociente //= 2

	resto.append(quociente)

	for i in resto:
		if i == 1:
			qtdeBits += 1

	return qtdeBits

def main():
	numero = int(input("Digite um número: "))

	print(f"Número de Bits \"1\": {getBits(numero)}")

#---------------------------------------

def inverter(palavra: str) -> str:
	return palavra[::-1]

def foo():
	palavra   = input("Digite uma palavra: ")
	invertida = inverter(palavra)
	print(invertida)

if __name__ == '__main__':
	foo()