# Raio recebe o valor real e permite ao usuário colocar o valor
raio = float(input())
# pi recebe o valor 3.141592
pi=3.141592
# Comando para imprimir o comprimento da circuferência com 6 casas decimais
print(("%.6f") % (2*pi*raio))
# Comando para imprimir o volume da circuferência com 6 casas decimais
print(("%.6f") % (pi*raio**2))
# Comando para imprimir o comprimento da esfera com 6 casas decimais
print(("%.6f") % (4*pi*raio**2))
# Comando para imprimir  volume da esfera com 6 casas decimais
print(("%.6f") % ((4*pi*raio**3)/3))
