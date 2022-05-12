def power(base, expoente):
	if expoente == 0:
		return 1

	resultado = base

	for iterator in range(1, expoente):
		resultado *= base

	return resultado

def main():
	base     = int(input("Base: "))
	expoente = int(input("Expoente: "))

	print(f"O resultado é: {power(base, expoente)}")

if __name__ == "__main__":
	main()