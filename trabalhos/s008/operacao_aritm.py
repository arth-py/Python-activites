'''Escreva um programa que leia dois valores e uma das
seguintes operações, codificadas dessa forma, será executada:

1 – Adição

2 – Subtração

3 – Multiplicação

4 – Divisão

Calcule e escreva o resultado dessa operação sobre os dois valores lidos.'''

def dois_valores(valor1,valor2,operacao):
    if operacao == 1:
        return  valor1 + valor2
    elif operacao == 2:
        return valor1 - valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        return valor1 / valor2
def main():
    valor1 = float(input('Insira o primeiro número:\n'))
    valor2 = float(input('Insira o segundo número:\n'))
    operacao = int(input('Escolha um número entre 1-4:\n'))
    print(f'{dois_valores(valor1,valor2,operacao)}')
if __name__ == '__main__':
    main()
