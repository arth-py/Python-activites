# A variável “preço” recebe, convertido para real, a leitura do preço que é feita pelo teclado.
preço=float(input())
# Imprime na tela o valor com desconto de 10% e duas casas decimais
print( "%.2f" % (preço * 0.90))
