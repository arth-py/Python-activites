'''Escreva um algoritmo/programa que
receba o valor do quilo de um produtoe a quantidade
de quilos consumida desse produto. Calcule e exiba
o valor final a ser pago'''
#Receber valor/kg
#Receber kg
#exibir o valor final

def preco(valor,kg):
    valor_a_pagar = valor * kg
    return f'{valor_a_pagar:.2f}'
    
def main():
    valor = float(input().strip())
    kg = float(input().strip())
    print(f'{preco(valor,kg)}')
    

    
if __name__=='__main__':
    main()
