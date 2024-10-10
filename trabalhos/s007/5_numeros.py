'''Escreva um programa que leia 5 números inteiros, calcule e
mostre a média e escreva
os que são maiores que a média.
Considere duas casas decimais.'''

def num_media(n1,n2,n3,n4,n5):
   return (n1 + n2 +n3 + n4 + n5) / 5

def main():
    nota1= int(input('Insira o primeiro número : '))
    nota2= int(input('Insira o segundo número : '))
    nota3= int(input('Insira o terceiro número : '))
    nota4= int(input('Insira o quarto número : '))
    nota5= int(input('Insira o quinto número : '))
    media = num_media(nota1,nota2,nota3,nota4,nota5)

    print(f'{media:0.2f}')

    if nota1 > media:
        print(f'{nota1} é maior que a média({media})')
    if nota2 > media:
        print(f'{nota2} é maior que a média({media})')
    if nota3 > media:
        print(f'{nota3} é maior que a média({media})') 
    if nota4 > media:
        print(f'{nota4} é maior que a média({media})')
    if nota5 > media:
        print(f'{nota5} é maior que a média({media})')
          
if __name__ == '__main__':
    main()
    
    
