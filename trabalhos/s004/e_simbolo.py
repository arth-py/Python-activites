# Define a função 'x' para retornar True
def x():
    return True
# A variável 'x' recebe o valor definido pelo usuário
x = input('Insira um símbolo para ser inspecionado: ').strip()
# Define os possíveis valores de x para retorno True
print (x == '!' or x=='@' or x=='#' or x=='$' or x=='%' or x=='&' or x=='*' or x=='(' or x==')' or x=='+' or x=='=' or x=='_' or x=='-' or x=='"' or x=='/' or x=='<' or x=='>' or x==':')
