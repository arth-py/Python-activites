'''Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno
. Apresente a média das três notas, mas, se a terceira nota for
superior a 8, o aluno deve ganhar mais um ponto 
na média. Além disso, se a média final, em função do ponto extra,
ficar acima de 10 ela deve ser ajustada para 10'''
def media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    if media > 10:
        return 10
    else:
        if media + 1 > 10:
            return 10
        elif n3 > 8:
            return media + 1
        else:
            return media
def main():
    n1 = float(input('Insira a 1º nota :'))
    n2 = float(input('Insira a 2º nota :'))
    n3 = float(input('Insira a 3º nota :'))
    print (f'A média é {media(n1,n2,n3):0.2f}')
if __name__ == '__main__':
    main()
