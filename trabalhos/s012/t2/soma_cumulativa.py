def main():
    somador = 0
    NumList = []
    NumSomados = []
    Nsoma = 0
    # Repetição com teste no final
    while True:
        num = int(input())
        # Condição de término para caso o usuário digite zero
        if num == 0:
            break
        NumList.append(num)
    # Repetição no alcance do tamanho da lista
    for i in range(len(NumList)):
        # Adiciona à uma nova lista a soma dos números no intervalo 0 até o número atual(i)
        NumSomados.append(sum(NumList[0:i+1]))
    print(f'{NumSomados}')
            

if __name__ == '__main__':
    main()
