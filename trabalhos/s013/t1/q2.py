def analise(lista,valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador +=1
    return contador
        
    


def main():
    lista = []
    while True:
        numero = int(input('Digite Números ( 0 = fim ):'))
        if numero == 0:
            break
        lista.append(numero)
    valor = int(input('Digite um valor: '))
    print(f'{lista}\n{valor}\n{analise(lista,valor)}')
        

if __name__ == '__main__':
    main()
