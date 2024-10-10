def main():
    numero = int(input()) 
    divisores= 0 # Contador para o número de divisores
    for i in range(1,numero+1): # Repetição no intervalo de 1 ao número corrigido com +1
        if numero % i == 0: # Define a condição para caso o número seja divisível por um número
            divisores += 1 # Adiciona um divisor ao contador
    if divisores == 2: # Define a condição para definir se é primo ou não
        print(True)
    else:
        print(False)
        
if __name__ =='__main__':
    main()
