'''A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair na sua frente.
A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto.
Faça um programa que leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até
que a lebre alcance a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.'''
def corrida(Mtartaruga):
    Mlebre=0 
    minutos=0
    while True:
        Mtartaruga+=1 # Aumenta a distância percorrida pela tartaruga em 1
        minutos+=1 # Aumenta a contagem do tempo
        Mlebre+=10 # Aumenta a distância percorrida pela lebre em 10
        if Mlebre >= Mtartaruga: # Define a condição para fim da repetição para quando a lebre ultrapassar a tartaruga
            break
    print(f'{minutos}')
    
def main():
    Mtartaruga=int(input().strip())
    corrida(Mtartaruga)

if __name__ =='__main__':
    main()
