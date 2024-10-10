# Define a função arredonda, que retorna o valor recebido arredondado para zero casas decimais
def arredonda(x):
    return round(x)
# Define a função main
def main():
# A função 'numero' , convertida para real, recebe o valor definido pelo usuário
    numero = float(input().strip())
# Imprime o retorno da função 'arredonda'
    print(f'O número arredondado é : {arredonda(numero)}')
# Fecha a função main
if __name__ == '__main__':
    main()
