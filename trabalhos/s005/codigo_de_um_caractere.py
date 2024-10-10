# Define a função 'caractere' retornando o código do caractere recebido
def caractere(exemplo):
    return ord(exemplo)
# Define a função main
def main():
# A variável 'exemplo' recebe um valor definido pelo usuário
    exemplo = input('Insira o caractere a ser inspecionado : ')
# Convoca a função 'caractere'
    print(f'O código desse caractere é : {caractere(exemplo)}')
# Define a função 'main'
if __name__ == '__main__':
    main()
