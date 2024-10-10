def comprimento(lista):
    comprimento = 0
    for a in lista:
        comprimento+=1
    return comprimento

def inverter(lista):
    listainversa = []
    for b in lista:
        listainversa.insert(0,b)
    return listainversa

def minimo(lista):
    menor = 10000000
    for c in lista:
        if c < menor:
            menor = c
    return menor

def maximo(lista):
    maior = 0
    for d in lista:
        if d > maior:
            maior = d
    return maior

def soma(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma
    

def main():
    lista = []
    while True:
        num = int(input('Digite números (0 = fim) :'))
        if num == 0:
            break
        lista.append(num)
    print(f'\nLista Digitada :{lista}\nTamanho da Lista:{comprimento(lista)}\nLista invertida:{inverter(lista)}\nMenor número:{minimo(lista)}\nMaior número da lista:{maximo(lista)}\nSoma dos valores:{soma(lista)}')
    

if __name__ == '__main__':
    main()
