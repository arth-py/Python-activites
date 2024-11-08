def somar(t1,escala1,t2,escala2):
    if escala1 == escala2:
        t = t1 + t2
        tupla = (t,escala1)
        return tupla
    elif escala2 == 'F' and escala1 == 'C':
        t1 = (t1 * (9/5)) + 32
        t = round(t1 + t2, 4)
        tupla = (t,escala2)
        return tupla
    
    elif escala2 == 'C' and escala1 == 'F':
        t1 = (t1 - 32) * (5/9)
        t = round(t1 + t2, 4)
        tupla = (t , escala2)
        return tupla
def main():

    ''' Recebendo as informações do usuário,
        primeiro ele digita o número depois a escala'''
    # Logo após receber os dados, convertemos para poder compará-los       
    t1 = float(input())
    escala1 = input().upper()[0]
    t2 = float(input())
    escala2 = input().upper()[0]

    
    print(f'{somar(t1,escala1,t2,escala2)}')
    

if __name__ == '__main__':
    main()
