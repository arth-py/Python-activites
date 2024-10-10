'''O índice de massa corporal (IMC)
é uma medida internacional usada para calcular se uma pessoa está
no peso ideal. O IMC é determinado pela divisão da massa do indivíduo
pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros
. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa,
e depois, mostra uma das seguintes mensagens:

< 18,5 	Abaixo do peso
< 25 	Peso normal
< 30 	Sobrepeso
< 35 	Obeso leve
< 40 	Obeso moderado
>=40 	Obeso mórbido'''

def indice(massa,altura):
    IMC = (massa)/(altura**2)
    if IMC < 18.5:
        print (f'{IMC}\nAbaixo do peso')
    elif IMC < 25 and IMC > 18.5:
        print (f'{IMC}\nPeso normal')
    elif IMC < 30 and IMC > 25:
        print (f'{IMC}\nSobrepeso')
    elif IMC < 35 and IMC > 30:
        print (f'{IMC}\nObeso leve')
    elif IMC < 40 and IMC > 35:
        print (f'{IMC}\nObeso moderado')
    elif IMC >= 40:
        print (f'{IMC}\nObeso mórbido')

def main():
    m=float(input('Insira o mês : '))
    a=float(input('Insira o ano : '))
    indice(m,a)
if __name__ == '__main__':
    main()



