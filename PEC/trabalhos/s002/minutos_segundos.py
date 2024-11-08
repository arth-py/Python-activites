# Usuário coloca a quantidade de segundos total
segundos=int(input())
# Divisão exata sem considerar o resto dos segundos por 60 encontrando os minutos
print( "%d" % (segundos//60))
# Cálculo do resto encontrando os segundos que sobraram
print( "%d" % (segundos%60))
