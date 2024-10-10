# Função para conferir se o número é par
def par_impar(x):
    return x % 2 == 0
def main():
    ListNum = []
    ListProd = []
    contador = 0
    # Repetição na qual o usuário insere 100 números inteiros, adicionados a lista
    for i in range(100):
        numero = int(input())
        ListNum.append(numero)
    # Ordena a lista
    ListNum.sort()
    # Repetição dentro da lista com condição para caso o índice do número seja par, multiplicando-o por 3
    # Caso o índice seja par multiplica o número por três
    # Caso o índice seja impar multiplia o número po 5
    for n in ListNum:
        if par_impar(contador):
            n *= 3
            ListProd.append(n)
        else:
            n *= 5
            ListProd.append(n)
        contador+=1   
    print(f'{ListProd}')

    
if __name__ =='__main__':
    main()
