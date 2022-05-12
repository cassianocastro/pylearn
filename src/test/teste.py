#! /usr/bin/env python3.10

class MathOperation:

	"""A breve resume for MathOperation class.

	Description of the class.
	"""

	signal = "+"

	def sum(self) -> None:
		valor1 = input("Primeiro valor: ")
		valor2 = input("Segundo valor: ")
		soma   = int(valor1) + int(valor2)

		print(f"A soma dos valores é {soma}.")


if __name__ == "__main__":
	import sys

	print(sys.path)

	MathOperation().sum()

	foo = 1
	assert foo == 1