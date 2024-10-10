# Define a função ano, retornando o valor dividido exatamente por 2
def ano(x):
    return x//2
# Define a função main
def main():
# A variável 'ano_terreste', convertida para inteiro, recebe o valor definido pelo usuário    
    ano_terrestre = int(input('Insira a quantidade de anos terrestres: '))
# Imprime o retorno da função 'ano'
    print(f'A quantidade de anos terrestres em anos do planeta de Zob é : {ano(ano_terrestre)}')
# Fecha a função 'main'
if __name__ == '__main__':
    main()
