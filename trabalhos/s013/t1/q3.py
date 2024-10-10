'''Dadas duas listas A e B contendo 20 elementos inteiros cada,
gerar e exibir uma lista C do mesmo
tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.'''

def soma(lista1,lista2):
    lista3 = []
    for a in range(20):
        lista3.append(lista1[a] + lista2[a])
    return lista3
        

def main():
    lista = []
    listb = []
    for i in range(20):
        lista.append(int(input()))
    for l in range(20):
        listb.append(int(input()))
    print(f'{lista}\n{listb}\n{soma(lista,listb)}')
        
    

if __name__ == '__main__':
    main()
