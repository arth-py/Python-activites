'''Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano
no mês de março. Pedro também tem uma dívida no cartão de crédito com uma taxa de
juros de 15% ao mês. Considerando que a situação se refere ao mês de outubro do
ano de 2016, faça um programa leia o valor do salário e o valor da dívida e calcula,
simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com
o cartão de crédito será superior ao seu próprio salário.
Represente os meses como inteiros de 1 a 12.
Dica: Controle essas quatro variáveis:
“dívida” que aumenta todo mês; “salário” que aumenta apenas se o número do mês for 3 (março);
“mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12; “ano” que só é incrementado quando o mês retornar a 1.'''
# outubro do ano de 2016
# Função para retornar o valor da divida com juros
def dever(valor_divida):
    valor_divida = valor_divida*(0.15)
    return valor_divida
# Função para retornar o valor do aumento
def aumento(valor_salario):
    valor_salario = valor_salario*(0.05)
    return valor_salario
# Define a função 'divida_salario'
def divida_salario(salario,divida):
    # Define as variáveis
    ano = 2016
    mes = 10
    preco_devido = divida
    dinheiro = salario
    # Define a repetição indeterminada
    while True:
        mes += 1
        # Define a condição para quando o mês for igual a 13, ele recebe 1 e o ano +1
        if mes == 13:
            ano += 1
            mes = 1
        # Define a condição para quando o mês for igual a 3, o dinheiro recebe dinheiro + o retorno da função 'aumento'
        if mes == 3:
            dinheiro += aumento(dinheiro)
        # 'preco_devido' recebe o preco_devido + o retorno da função dever 
        preco_devido += dever(preco_devido)
        # Define a condição para quando o 'preco_devido' for maior que 'salario' a repetição encerrar
        if preco_devido > dinheiro:
            return f'{mes}/{ano}'

            

def main():
    salario = int(input())
    divida = int(input())
    print(divida_salario(salario,divida))
    
if __name__ == '__main__':
    main()
