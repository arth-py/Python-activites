# Converte a variável 'Celsius' para real, recebendo o valor definido pelo usuário
celsius=float(input('Insira a temperatura a ser convertida, em Celsius :  ').strip())
# A variável 'fahrenheit' recebe o valor de celsius calculado pela fórmula
fahrenheit = ((celsius*(9/5))+32)
# Imprime o valor em Fahrenheit
print(f' A temperatura {celsius} Cº em fahrenheit é {fahrenheit: .2f} Fº')
