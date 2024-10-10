def negativo(lista):
    negativos = 0
    for num in lista:
        if num < 0:
            negativos += 1
    return negativos

def soma_positivos(lista):
    soma = 0
    for num in lista:
        if num > 0:
            soma += num
    return soma

def main():
    lista = []
    for i in range(10):
        lista.append(int(input()))
    print(f'{lista}\n{negativo(lista)}\n{soma_positivos(lista)}')
        

if __name__ == '__main__':
    main()
