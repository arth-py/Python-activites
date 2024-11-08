'''Escreva um programa que leia dois valores inteiros (x e y)
e mostre todos os números primos entre x e y.'''
def main():
    x = int(input())
    y = int(input())
    divisores= 0
    for algarismo in range(x,y+1): # Define o intervalor no qual os números vão ser analisados
        for numero in range(1,algarismo+1): # Analisa individualmente cada número se ele é primo
            if algarismo % numero == 0: # Define a condição para o caso do número ser divisível
                divisores +=1

        if divisores == 2: # Define a condição para o número ser primo e logo ser impresso
            print(f'{algarismo}')
        divisores = 0 # zerando o número de divisores para que a operação possa ser repetida sem erros

            
        
if __name__ == '__main__':
    main()
