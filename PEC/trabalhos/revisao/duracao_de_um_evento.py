'''Faça um programa que leia o tempo de duração
de um evento em uma fábrica expresso em segundos.
Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).
'''
#PROFESSOR ESSA AQUI EU E O SILAS TRANSCENDEMOS!! MUITO BOM!!
def horas_max(horas):
    if horas < 10:
        horas = str(horas)
        return '0' + horas
    else:
        return horas

def minutos_max(minutos):
    if minutos < 10:
        minutos = str(minutos)
        return '0' + minutos
    else:
        return minutos

def segundos_max(segundos):
    if segundos < 10:
        segundos = str(segundos)
        return '0' + segundos
    else:
        return segundos
      

def tempo(temp):
    horas = temp // 3600
    minutos = (temp % 3600) // 60
    segundos = (temp % 3600) % 60
    return f'{horas_max(horas)}:{minutos_max(minutos)}:{segundos_max(segundos)}'
    

def main():
    segundos_totais = int(input())
    print(f'{tempo(segundos_totais)}')
    
    
if __name__=='__main__':
    main()
