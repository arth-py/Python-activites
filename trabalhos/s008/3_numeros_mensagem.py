'''Escreva um programa que leia 3 (três) números inteiros
e escreva uma das mensagens abaixo,
de acordo com os valores lidos:'''

def numero(x,y,z):
    if x == y and x == z:
        return 'Todos os valores são iguais'
    elif x != y and y != z and x != z:
        return 'Todos os valores são diferentes'
    elif x == y and x != z or x == z and x != y or y == z and y != x:
        return 'Existem dois valores iguais e um diferente'

def main():
    primeiro = int(input('Digite o primeiro número'))
    segundo = int(input('Digite o segundo número'))
    terceiro = int(input('Digite o terceiro número'))
    print(f'{numero(primeiro,segundo,terceiro)}')
if __name__ == '__main__':
    main()

