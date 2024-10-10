# A função 'horas' é definida e retorna os minutos divididos exatamente por 60
def horas(minutos): 
    return minutos//60
# A função 'minutos_restantes' é definida e retorna o módulo(resto) de minutos por 60
def minutos_restantes(minutos):
    return minutos%60
# Define a função 'main'
def main():
# A variável 'minutos_totais', convertida para inteiro, recebe o valor definido pelo usuário
    minutos_totais=int(input('Insira os minutos totais para que eles sejam convertidos: ').strip())
# A variável 'h' recebe o retorno de função 'horas'
    h = horas(minutos_totais)
# A variável 'm' recebe o retorno da função 'minutos_restantes'
    m = minutos_restantes(minutos_totais)
# Imprime as variáveis 'h' e 'm'
    print(f'Os minutos convertidos resultam em {h}:{m}')
# Fecha a função 'main'
if __name__ == '__main__':
    main()


