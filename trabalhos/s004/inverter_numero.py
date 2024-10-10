# Define a função 'inverter' com retorno da variável 'numero_invertido'
def inverter(numero):
    unidade = numero % 10
    numero = numero // 10
    dezena = numero % 10
    numero = numero // 10
    centena = numero % 10
    numero = numero // 10
    milhar = numero % 10
    numero_invertido = (unidade*1000)+(dezena*100)+(centena*10)+milhar
    return numero_invertido
# Define a função main
def main():
# A variável 'n', convertida para inteiro, recebe o valor definido pelo usuário
    n = int(input('Insira o número a ser invertido: '))
# Imprime a variável 'n' ,  convertida pela função 'inverter'
    print(f'O número {n} invertido é {inverter(n)}')
# Fecha a função 'main'
if __name__ == '__main__':
    main()
    
