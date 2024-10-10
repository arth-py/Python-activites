def confere(n,lista):
    tamanho = len(lista)+1
    if n in lista[0:tamanho]:
        pass
    else:
        lista.append(n)    

        
def main():
    lista = []
    for a in range(10):
        num1 = int(input())
        confere(num1,lista)
        
    for b in range(10):
        num2 = int(input())
        confere(num2,lista)
    print(f'{lista}')

if __name__ == '__main__':
    main()
