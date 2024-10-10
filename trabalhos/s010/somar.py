'''Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos.
Observação: A condição de saída do laço será a leitura do valor 0 (flag).'''
# Define a função Somar
def somar():
    soma=0
    # Define a repetição indeterminada
    while True:
        opcao = int(input())
        soma += opcao
        # Define a condição para que a repetição termine
        if opcao == 0:
            break
    return soma
def main():
    print(f'{somar()}')
        

if __name__ =='__main__':
    main()
