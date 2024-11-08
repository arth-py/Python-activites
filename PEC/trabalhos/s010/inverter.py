# Função para inverter os números
def algarismos(opcao):
    # Variável 'algarismo' recebe lista
    algarismo=[]
    # Repetição enquanto 'opcao' seja divisível por 10
    while opcao % 10 == 0:
        # Operação divide exatamente 'opcao' por 10
        opcao //= 10
        # Condição para o fim da repetição quando 'opcao' for divida por 10 e resultar em zero
        if (opcao //10) == 0:
            break
    # Repetição  
    while True:
        # 'numero' recebe o resto de 'opcao' por 10
        numero = opcao % 10
        # 'opcao' recebe opcao dividido por 10
        opcao //= 10
        # Adiciona 'numero' à lista 'algarismo'
        algarismo.append(numero)
        # Define a condição para o fim da função quando 'opcao' for 0
        if opcao == 0:
            break
    # Repetição determinada para imprimir os números que estão na lista 'algarismo'
    for n in algarismo:
        print(n,end='')
    
def main():
    # 'opcao' recebe o inteiro digitado pelo usuário
    opcao= int(input())
    # chama a função 'algarismos'
    algarismos(opcao)
if __name__=='__main__':
    main()
