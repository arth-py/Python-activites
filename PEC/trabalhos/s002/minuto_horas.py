# A variável minutos, definida com inteiro, recebe o valor pelo usuário
minutos=int(input())
# Imprime as horas e os minutos que sobraram
print(("%dh%dmin") % (minutos//60 , minutos%60))
