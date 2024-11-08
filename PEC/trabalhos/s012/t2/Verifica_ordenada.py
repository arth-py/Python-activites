# Essa função retorna True para as listas já ordenadas 
def esta_ordenado(lista): 
    return lista == sorted(lista)


def main():
    
    Nrepet=int(input())
    ListNum = []
    for i in range(Nrepet):
        num = input()
    # Esse bloco obriga o usuário a inserir apenas dígitos, caso contrário, ele volta para o bloco de inserir o dado
        try:
            num = float(num)
        except ValueError:
            pass
        ListNum.append(num)
    # Condição para gerar uma impressão caso a lista esteja ordenada ou não
    if esta_ordenado(ListNum):
        print(f'LISTA ORDENADA')
    else:
        print(f'LISTA NÃO ORDENADA')
    
if __name__ == '__main__':
    main()
