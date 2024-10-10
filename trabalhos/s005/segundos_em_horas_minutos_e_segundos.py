# Define a função 'horas' retornando o valor da duracao dividido exatamente por 3600
def horas(duracao):
    horas = duracao // 3600
    return horas
# Define a função 'minutos' retornando o valor da duração em minutos
def minutos(duracao):
    minutos = ((duracao % 3600) // 60)
    return minutos
# Define a função 'segundos' retornando os segundos restantes da duração
def segundos(duracao):
    segundos = ((duracao % 3600) % 60)
    return segundos
# Define a função 'main'
def main():
# A variável 'duracao', convertida para inteiro, recebe o valor definido pelo usuário
    duracao = int(input('Insira os segundos totais a serem convertidos : ').strip())
# Imprime o valor das horas, minutos e segundos convertidos. 
    print(f'Convertidos, os segundos são : {horas(duracao)}h:{minutos(duracao)}min:{segundos(duracao)}s ')
# Fecha a função main
if __name__ == '__main__':
    main()
