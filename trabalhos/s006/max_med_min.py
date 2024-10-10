'''Escreva um programa que leia três números por parâmetro
e mostre na tela em ordem crescente.'''

def ordem_crescente(x,y,z):
    if   x > y and y > z :
        print (f'{z}\n{y}\n{x}')
    elif y > x and x > z :
        print (f'{z}\n{x}\n{y}')
    elif z > x and x > y :
        print (f'{y}\n{x}\n{z}')
    elif z > y and y > x:
        print (f'{x}\n{y}\n{z}')
    elif y > z and z > x:
        print (f'{x}\n{z}\n{y}')
    elif x > y and z > y:
        print (f'{y}\n{z}\n{x}')
def main():
    x=int(input('Digite o primeiro número : '))
    y=int(input('Digite o segundo número : '))
    z=int(input('Digite o terceiro número : '))
    ordem_crescente(x,y,z)
if __name__ == '__main__':
          main()
