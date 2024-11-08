'''Escreva um programa que leia uma quantidade indefinida de números
inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar
a média aritmética de todos os números lidos (excluindo o zero).
'''
# Define a função media
def media(opcao):
    # Definiçãode variáveis
    soma=0
    elementos=1
    soma+=opcao
    # Repetição com condição de que opcao seja diferente de 0 para repetir
    while opcao != 0:
        # Usuário define 'opcao'
        opcao= int(input())
        soma += opcao
        elementos+=1
    # Elementos recebe elementos - 1 para que ao calcular a média seja removido o elemento de 0 
    elementos-=1
    
    media = soma/elementos
    return media  

def main():
    opcao= float(input())
    print(f'{media(opcao):.2f}')


if __name__=='__main__':
    main()
