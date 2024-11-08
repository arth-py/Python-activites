# A variável "h" recebe, convertida para inteiro, um número definido pelo usuário.
h=int(input().strip())
# A variável "m" recebe, convertida para inteiro, um número definido pelo usuário.
m=int(input().strip())
# A variável "s" recebe, convertida para inteiro, um número definido pelo usuário.
s=int(input().strip())
# A variável "horas" recebe a variável "h" multiplicada por 3600
horas=h*3600
# A variável "minutos" recebe a variável "m" multiplicada por 60
minutos=m*60
# Imprime a soma, em segundos, das variáveis definidas
print(horas+minutos+s)
