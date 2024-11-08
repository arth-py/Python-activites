def preco_carro(preco):
    mes=0
    poupanca=10000
    while True:
        mes+=1 # Recebe e conta os meses
        poupanca+=poupanca*(0.7/100) # Calcula e recebe o crescimento da poupança no mês
        preco+=preco*(0.4/100) # Calcula e recebe o crescimento do preço
        if preco <= poupanca: # Quando o preço for menor que a poupança a repetição termina
            break
    print(f'{mes}')
        
    
def main():
    preco=int(input())
    preco_carro(preco)

if __name__ == '__main__':
    main()
