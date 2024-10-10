def main():
    lista = []
    for i in range(10):
        lista.append(int(input()))
    maior = max(lista)
    posicao = lista.index(maior)
    print(f'{lista}\n{maior}\n{posicao}')

if __name__ == '__main__':
    main()
