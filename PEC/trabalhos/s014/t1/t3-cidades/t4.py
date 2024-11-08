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

'''  IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639 '''
def main():
    valor = int(input())
    cidades = carrega_cidades()
    print(f'CIDADES COM MAIS DE {valor} HABITANTES:')
    for linha in cidades:
        if linha[5] > valor:
            print(f'IBGE: {linha[1]} - {linha[2]}({linha[0]}) - POPULAÇÃO: {linha[5]}')
if __name__ == '__main__':
    main()
