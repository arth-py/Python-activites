# Função que retorna a porcentagem adicional
def adicional(valor,porcentagem):
    return (valor*(porcentagem/100)) + valor
# Função que retorna o desconto sobre o valor
def descontado(valor,porcentagem):
    return  valor - (valor*(porcentagem/100)) 


def main():
# Define o valor, convertido para real, pelo usuário
    v = float(input('Insira o valor do preço : '))
# Define a porcentagem, convertiada para real, pelo usuário
    p = float(input('Insir o valor da porcentagem : '))
# A variável 'valor_total' recebe a função 'adicional' definida pelas variáveis 'v' e 'p'
    valor_total = adicional(v,p)
# A variável 'valor_descontado' recebe a função 'descontado' definida pelas variáveis 'v' e 'p'
    valor_descontado = descontado(v,p)
# Imprime o valor com a porcentagem adicional
    print(f'O valor com a porcentagem adicional : {valor_total:.2f}')
# Imprime o valor do preço com desconto
    print(f'O valor com o preço descontado é : {valor_descontado:.2f}')
# Fecha a função main
if __name__ == '__main__':
    main()


    




