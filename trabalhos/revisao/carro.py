'''O custo ao consumidor, de um carro novo, é a
soma do [custo de fábrica] com a [percentagem do distribuidor] e dos
impostos (aplicados ao custo de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos
de 45%, escrever um algoritmo para ler o
custo de fábrica de um carro e escrever o custo final ao consumidor.'''
#distribuidor 28% - custo de fabrica
#impostos 45% - custo de fabrica
#input custo fabrica
#saida : custo final
def impostos(preco):
    preco_consumidor = (0.28 * preco) + (0.45 * preco) + preco
    return preco_consumidor
    
def main():
    preco_carro = float(input().strip())
    print(f'R$ {impostos(preco_carro):.2f}')
    
if __name__=='__main__':
    main()
