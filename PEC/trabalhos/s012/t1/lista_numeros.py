def main():
    soma = 0
    multiplicacao = 1
    ListNumeros = []
    # Repetição na qual o usuário insere 10 números, que serão somados, adicionados a uma lista e multiplicados entre si
    for i in range(10):
        numero = int(input())
        soma += numero
        multiplicacao *= numero
        ListNumeros.append(numero)


    print(f'{ListNumeros}\n{soma}\n{multiplicacao}')
if __name__ == '__main__':
    main()
