# A variável dividendo recebe o valor pelo usuário
dividendo=input()
# A variável dividendo é definida com número real
dividendo=float(dividendo)
# A variável divisor recebe o valor pelo usuário
divisor=input()
# A variável divisor é definida com número real
divisor=float(divisor)
# A variável quociente recebe o valor da divisão exata entre dividendo e divisor
quociente=(dividendo // divisor)
# A variável resto recebe o valor do resto do cálculo entre dividendo e divisor
resto=(dividendo % divisor)
# Imprime o valor do quociente com 4 casas decimais
print( "%.4f" % quociente)
# Imprime o valor do resto com 4 casas decimais
print( "%.4f" % resto)
