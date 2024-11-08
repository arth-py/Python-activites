# Define a função 'o_maior' retornando a maior variável inteira entre as 5 recebidas
def o_maior(a,b,c,d,e):
    return max(a,b,c,d,e)
# Define a função 'o_menor' retornando a menor variável inteira entre as 5 recebidas
def o_menor(a,b,c,d,e):
    return min(a,b,c,d,e)
# Define a função 'media' retornando a média entre as 5 variáveis recebidas
def media(a,b,c,d,e):
    media = (a + b + c + d + e) / 5
    return media
# Define a função main
def main():
# A variável 'a', convertida para inteiro, recebe o valor definido pelo usuário
    a = int(input('Insira o valor do 1º número : '))
# A variável 'b', convertida para inteiro, recebe o valor definido pelo usuário
    b = int(input('Insira o valor do 2º número : '))
# A variável 'c', convertida para inteiro, recebe o valor definido pelo usuário
    c = int(input('Insira o valor do 3º número : '))
# A variável 'd', convertida para inteiro, recebe o valor definido pelo usuário
    d = int(input('Insira o valor do 4º número : '))
# A variável 'e', convertida para inteiro, recebe o valor definido pelo usuário
    e = int(input('Insira o valor do 5º número : '))
# Imprime o retorno da função 'o_maior'
    print( f'O maior número entre os 5 recebidos é : {o_maior(a,b,c,d,e)}')
# Imprime o retorno da função 'o_menor'
    print( f'O menor número entre os 5 recebidos é : {o_menor(a,b,c,d,e)}')
# Imprime o retorno da função 'media'
    print( f'A média entre os 5 números é : {media(a,b,c,d,e)}')
# Fecha a função 'main'
if __name__ == '__main__':
    main()
