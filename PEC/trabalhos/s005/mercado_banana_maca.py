# Define a função 'preco_maca' que retorna o preço da maçã multiplicado por 3
def preco_maca(x):
    preco_total_da_maca = x * 3
    return preco_total_da_maca
# Define a função 'preco_banana' que retorna o preço da banana multiplicado por 2
def preco_banana(y):
    preco_total_da_banana = y * 2
    return preco_total_da_banana
# Define a função main
def main():
# A variável 'preco_m', convertida para real, recebe o valor definido pelo usuário
    preco_m = float(input('Insira o preço da maçã: '))
# A variável 'preco_b', convertida para real, recebe o valor definido pelo usuário
    preco_b = float(input('Insira o preço da banana: '))
# A variável 'preco_total' recebe a somatória do preço da maçã e da banana
    preco_total = preco_maca(preco_m) + preco_banana(preco_b)
# Imprime o preço com 2 casas decimais de proximidade
    print(f'O preço total é : R$ {preco_total:0.2f}')
# Fecha a função 'main'   
if __name__ == '__main__':
    main()
