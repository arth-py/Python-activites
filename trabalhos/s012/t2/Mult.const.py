def main():
    ListNum=[]
    ListProduto=[]
    # Repetição com teste no final
    # Uma lista receberá números enquanto o usuário não digitar zero
    while True:
        num=int(input())
        if num == 0:
            break
        ListNum.append(num)
    const=int(input())

    # Repetição para multiplicar cada elemento da lista pela constante definida pelo usuário
    # Adiciona o produto a uma lista
    for fator in ListNum:
        produto = fator*const
        ListProduto.append(produto)

    print(f'{ListProduto}')
    
if __name__ =='__main__':
    main()
