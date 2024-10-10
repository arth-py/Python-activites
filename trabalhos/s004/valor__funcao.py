# Define a função 'calcular', e retorna a resposta de função 
def calcular(a,b,c):
    return (2 * a + 5 * b - c)

# Define a função main, ou seja, a que virá a se repetir
def main():
# A variável 'a' recebe, convertida para inteiro, o valor definido pelo usuário
    a = int(input('Insira o valor de a : ').strip())
# A variável 'b' recebe, convertida para inteiro, o valor definido pelo usuário
    b = int(input('Insira o valor de b : ').strip())
# A variável 'c' recebe, convertida para inteiro, o valor definido pelo usuário
    c = int(input('Insira o valor de c : ').strip())
# A variável 'valor' recbe o retorno da função calcular, com as variáveis definidas pelo usuário
    valor = calcular(a,b,c)
# Imprime o resultado da função 'calcular'
    print(f'O resultado da função (2 * {a} + 5 * {b} - {c}) é = {valor}')
# Fecha a função 'main'
if __name__ == '__main__':
     main()
    


