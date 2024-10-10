'''Escreva um programa que leia dois valores que correspondem à base e a altura
de um retângulo. O programa deve inicialmente verificar se os valores formam um
retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e
caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área
(base vezes a altura) do retângulo. Separe esses valores com um hífen.'''

def quadrado_ou_retangulo(base,altura):
    if base == altura:
        return 'QUADRADO'
    elif base != altura:
        return f'{2*base + 2*altura} - {base*altura}'

def main():
    base = int(input('Insira o valor da base:\n'))
    altura = int(input('Insira o valor da altura:\n'))
    print(f'O perímetro - base da figura é : \n{quadrado_ou_retangulo(base,altura)}')

if __name__ == '__main__':
    main()
    
