def senhor_e_senhora(y,x):
    if x == 1:
        print(f'Ilmo Sr. {y}')
    else:
        if x ==2:
          print(f'Ilma Sra. {y}')
        else:
            print(f'Ilmo Sr. {y} ')
    

def main():
    nome = input('Insira o nome do usuário: ').strip()
    x = int(input('Insira um número 2 - feminino e 1 - masculino: ').strip())
    senhor_e_senhora(nome,x)
    
if __name__ == '__main__':
    main()
