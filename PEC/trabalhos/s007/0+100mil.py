'''Escreva um programa que leia um número     inteiro.
Mostre a soma dos dígitos para os números entre 0 (zero)
e 100 mil ou -1 para outros valores. Por      exemplo:
Em 16.759 a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31
é o valor retornado; Em 136.759 o valor lido é maior que
100 mil e deve retornar -1; Em -100 o valor lido é negativo e
deve retornar -1.
'''
def soma_digitos(x):
    c_milhar = x // 100000 % 10
    d_milhar = x // 10000 % 10
    u_milhar = x // 1000 % 10
    centena = x // 100 % 10
    dezena = x // 10 % 10
    unidade = x % 10
    if x < 100000 and x > 0:
        return c_milhar + d_milhar + u_milhar + centena + dezena + unidade
    else:
        return -1
def main():
    numero = int(input('Insira um número entre 0 e 100000 para imprimir a soma dos seus dígitos : '))
    print(f'A soma dos dígitos de {numero} é : {soma_digitos(numero)}')
if __name__ == '__main__':
    main()
