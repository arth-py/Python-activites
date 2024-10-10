# Define a função 'preco_a_vista' retornando o preço com desconto a ser pagado
def preco_a_vista(preco):
    preco_com_desconto = (preco - (preco * 0.09))
    return preco_com_desconto
# Define a função 'preco_com_juros' retornando o preço com juros a ser pagado por mês
def preco_com_juros(preco):
    preco_total = ((preco + (preco*0.17))/10)
    return preco_total

def main():
# A variável 'preco' , convertida para real, receb o valor defiido pelo usuário
    preco = float(input('Insira o preço a ser analisado: '))
# Imprime o valor à vista
    print(f'O preço à vista é : R${preco_a_vista(preco):0.2f} ')
# Imprime o valor parcelado em 5 vezes
    print(f'O preço normal é : R${preco/5:0.2f}')
# Imprime o valor parcelado em 10 vezes com juros
    print(f'O preço parcelado em 10 vezes é : R${preco_com_juros(preco):0.2f} ')
# Fecha a função 'main'   
if __name__ =='__main__':
    main()
