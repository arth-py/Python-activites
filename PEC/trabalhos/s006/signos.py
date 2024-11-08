def signos(x,y):
    if y == 1 and x >= 20 or y == 2 and x <= 18 :
        return 'Aquário'
    elif y == 2 and x >= 19 or y == 3 and x <= 20 :
        return 'Peixes'
    elif y == 3 and x >= 21 or y == 4 and x <= 19 :
        return 'Áries'
    elif y == 4 and x >= 20 or y == 5 and x <= 20 :
        return 'Touro'
    elif y == 5 and x >= 21 or y == 6 and x <= 21 :
        return 'Gêmeos'
    elif y == 6 and x >= 22 or y == 7 and x <= 22 :
        return 'Câncer'
    elif y == 7 and x >= 23 or y == 8 and x <= 22 :
        return 'Leão'
    elif y == 8 and x >= 23 or y == 9 and x <= 22 :
        return 'Virgem'
    elif y == 9 and x >= 23 or y == 10 and x <= 22 :
        return 'Libra'
    elif y == 10 and x >= 23 or y == 11 and x <= 21 :
        return 'Escorpião'
    elif y == 11 and x >= 22 or y == 12 and x <= 21 :
        return 'Sagitário'
    elif y == 12 and x >= 22 or y == 1 and x <= 19 :
        return 'Capricórnio'
def main():
    dia = int(input('Insira o dia (1 - 31): '))
    mes = int(input('Insira o mês (1 - 12): '))
    print (f'Seu signo é : {signos(dia,mes)}')
if __name__ == '__main__':
    main()
