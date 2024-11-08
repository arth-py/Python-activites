def main():
    produto = 1 
    n = int(input())
    for numero in range(1,n): # Repetição começando em 1 e terminando em 'n-1'
        produto *= n # Adiciona o valor de produto*n ao produto
        n-=1 # Remove uma unidade de 'n' para que o próximo valor lido seja menor
    print(f'{produto}') # Imprime o fatorial

if __name__ =='__main__':
    main()
