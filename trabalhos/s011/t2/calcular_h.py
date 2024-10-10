def main():
    n=int(input())
    h = 0 # Definindo 'h'
    n+=1 # Conserta o número para que o intervalo fique contenha o valor
    for numero in range(1,n): # Repetição de 1 ao número definido pelo usuário
        h+= 1/numero # 'H' recebe o numero sobre 1/ o número referente
    print(f'{h:.4f}')
if __name__ == '__main__':
    main()
