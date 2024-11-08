def main():
    n = int(input())
    
    algarismo1=0 # Define o algarismo 1
    algarismo2=1 # Define o algarismo 2
    n-=2 # Remove de 'n' duas unidades, desconsiderando os 2 primeiros números
    print(f'{algarismo1}, {algarismo2}',end=', ') # Imprime os 2 primeiros números
    for i in range(n): # Define repetição com a quantidade definida pelo usuário
        algarismo3 = algarismo1 + algarismo2 #calcula o 3º número
        if i < n-1: # Define a condição para que o algarismo seja imprimido somente se sua posição for menor que n-1
            print(f'{algarismo3}', end = ', ')
        elif i == n-1: # Define a condiçao para que o algarismo seja imprimido somente se sua posição for igual a n-1
            print(f'{algarismo3}')
        algarismo1 = algarismo2 # para dar continuidade à sequência fibonacci, o algarismo1 recebe seu posterior
        algarismo2 = algarismo3 # para dar continuidade à sequência fibonacci, o algarismo2 recebe seu posterior
        
        
    
if __name__ =='__main__':
    main()
