def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
    diaNiver = int(input())
    mesNiver = int(input())
    cidades = carrega_cidades()
    meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO' ,
             'JUNHO' ,'JULHO' ,'AGOSTO' ,'SETEMBRO' ,'OUTUBRO' ,'NOVEMBRO' ,'DEZEMBRO']
    mesList = mesNiver - 1
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {diaNiver} DE {meses[mesList]}:')
    for linha in cidades:
        if linha[3] == diaNiver:
            if linha[4] == mesNiver:
                print(f'{linha[2]}({linha[0]})')
if __name__ == '__main__':
    main()
