def estado_civil(x,nome1):
    if x[0] == '2' :
        return len(nome1)
    else:
        if x[0] == '1':
            nome2 = input().strip()
            return len(nome1 + nome2)
def main():
    nome1 = str(input('Indique o nome : ').strip())
    estado = str(input('Indique o estado civil : '))
    print(f'{estado_civil(estado,nome1)}')

if __name__ == '__main__':
    main()
