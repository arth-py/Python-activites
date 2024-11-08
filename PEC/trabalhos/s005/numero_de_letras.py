# Define uma função responsável por contar os caracteres
def numero(numero):
    return len(numero)
# Define a função 'main'
def main():
# A variável 'x', convertida para string, recebe a variável definida pelo usuário
    x = str(input('Insira a frase a ser inspecionada : ').strip())
# Imprime o retorno da função 'numero'
    print (f'O número de caracteres na frase é : {numero(x)}')
# Fecha a função main
if __name__ == '__main__':
    main()
    
