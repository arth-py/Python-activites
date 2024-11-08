'''Escreva um programa que leia um conjunto de 100 números inteiros
positivos e determine o maior deles.'''
def maximo():
    maior = 0
    for c in range(0,100):
        n = int(input('Insira um número:'))
        if n >= maior:
            maior = n
    print(f'O maior número é... {maior}')
           
def main():
    maximo()
if __name__ =='__main__':
    main()
