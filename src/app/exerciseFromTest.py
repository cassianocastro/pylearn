def getNumberOfBits(bits: list):
	qtdeBits = 0

	for bit in bits:
		if bit == 1:
			qtdeBits += 1

	return qtdeBits

def toBinary(number: int):
    restos: list = []

    while number >= 2:
        restos.append( number % 2 )
        number //= 2

    restos.append( number )
    #print(restos, end = " ")
    return restos

def main():
    try:
        number = int(input("Digite um número inteiro: "))
    except Exception as e:
        print("Entrada inválida!! O argumento passado não é um número.")
    else:
        binary = toBinary(number)
        print(f"Número de Bits \"1\": {getNumberOfBits(binary)}")

if __name__ == '__main__':
    main()