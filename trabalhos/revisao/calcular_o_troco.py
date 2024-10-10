'''Escreva um algoritmo/programa que receba
valor do preço de produto e o valor pago pelo cliente.
Calcule e exiba o valor do troco a ser dado.'''

def valor(preco,valor_recebido):
    if valor_recebido < preco:
        return 'Pagamento Insuficiente'
    else:
        troco = valor_recebido - preco
        return f'{troco:.2f}'
    
def main():
    preco = float(input())
    valor_recebido = float(input())
    print(f'{valor(preco,valor_recebido)}')
    
if __name__=='__main__':
    main()
