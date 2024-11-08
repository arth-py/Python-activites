'''Escreva um programa que leia um conjunto 100 números
inteiros e exiba o valor médio dos mesmos (com duas casas decimais).'''


def media():
    soma = 0
    for i in range(0, 100):
        i = int(input())
        soma += i
    media = soma / 100
    return media

def main():
    print(f'{media():0.2f}')
    
    
if __name__ == '__main__':
    main()
