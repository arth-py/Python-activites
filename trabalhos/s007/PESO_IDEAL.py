def peso_ideal(altura,sexo):
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7
def main():
    altura = float(input('Insira a altura em metros : ' ))
    sexo = int(input('Insira o gênero, 1 - homem, 2 - mulher : '))
    print(f'{peso_ideal(altura,sexo):0.2f}')
if __name__ =='__main__':
    main()
    
