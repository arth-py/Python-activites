'''Um time de basquete possui 12 jogadores. Deseja-se um programa
que, dado o nome e a altura dos jogadores, determine: a. o nome e
a altura do jogador mais alto; b. a média de altura do time; c. os
jogadores com altura superior à média, listando o nome e a altura de cada um.'''

def calcula_media(Lista1):
    return sum(Lista1)/len(Lista1)

def main():
    ListaNomes = []
    ListaAltura = []
    for i in range(12):
        ListaNomes.append(input())
        ListaAltura.append(float(input()))

    media = calcula_media(ListaAltura)
    MaiorAltura = max(ListaAltura)
    print(f'JOGADOR MAIS ALTO DO TIME')
    print(f'{ListaNomes[ListaAltura.index(MaiorAltura)]}')
    print(f'{MaiorAltura:.2f}')
    print(f'ALTURA MÉDIA DO TIME')
    print(f'{media:.2f}')
    print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for atleta in range(12):
        if ListaAltura[atleta] > media:
            print(f'{ListaNomes[atleta]}')
            print(f'{ListaAltura[atleta]:.2f}')
                           
if __name__ == '__main__':
    main()
