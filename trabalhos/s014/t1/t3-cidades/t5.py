def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Quando baixado, o arquivo veio com as colunas separadas por ',', converter dps
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado
'''CIDADES COM MAIS DE 50000 HABITANTES E ANIVERSÁRIO EM ABRIL:'''
''' Penedo(AL) tem 59020 habitantes e faz aniversário em 12 de abril'''

def main():
    mes = int(input())
    populacao = int(input())
    cidades = carrega_cidades()
    meses = ['janeiro', 'fevereiro', 'março', 'abril',
             'maio' , 'junho' ,'julho' ,'agosto' ,
             'setembro' ,'outubro' ,'novembro' ,'dezembro']
    
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {meses[mes-1].upper()}:')
    for linha in cidades:
        if linha[5] > populacao and linha[4]== mes:
            print(f'{linha[2]}({linha[0]}) tem {linha[5]} habitantes e faz aniversário em {linha[3]} de {meses[mes-1]}.')
if __name__ == '__main__':
    main()
