'''Considere uma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F)
como um valor em duas partes: temperatura e escala. Por exemplo: 32,5 graus
Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é representado
como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais
alta. Caso as temperaturas sejam de escalas diferentes,
a função deve fazer  aconversão antes de compará-las.
Faça a leitura de duas temperaturas, com (temperatura, escala), e mostre qual
é a maior. Use upper() e colchetes [] para garantir a leitura correta,
por exemplo: escala = input('Escala : ').upper()[0]
'''
# Função para converter a temperatura que tiver em Farenheit para Celcius


def maior(temp1,escala1,temp2,escala2):
    if escala1 == escala2:
        tupla1 = (temp1,escala1)
        tupla2 = (temp2,escala2)
        tupla = (tupla1,tupla2)
        return max(tupla)

    elif escala1 == 'F' and escala2 == 'C':
        c1 = (temp1 - 32) * (5/9)
        tupla1 = (temp1,escala1)
        tupla2 = (temp2,escala2)
        if c1 > temp2:
            return tupla1
        else:
            return tupla2

    elif escala1 == 'C' and escala2 == 'F':
        c2 = (temp2 - 32) * (5/9)
        tupla1 = (temp1,escala1)
        tupla2 = (temp2,escala2)
        if c2 > temp1:
            return tupla2
        else:
            return tupla1
        
def main():

    ''' Recebendo as informações do usuário,
        primeiro ele digita o número depois a escala'''
    # Logo após receber os dados, convertemos para poder compará-los       
    temp1 = float(input())
    escala1 = input().upper()[0]
    temp2 = float(input())
    escala2 = input().upper()[0]

    print(f'{maior(temp1,escala1,temp2,escala2)}')
    

if __name__ == '__main__':
    main()
