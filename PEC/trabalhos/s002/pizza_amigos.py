# Usuário coloca número de fatias
fatias=input()
# Classificação da informação gravada
fatias=int(fatias)
# Usuário coloca número de amigos
amigos=input()
# Classificação da informação gravada
amigos=int(amigos)
# Divisão inteira de fatias por amigos
print(fatias//amigos)
# Fatias que sobraram
print(fatias-((fatias//amigos)*amigos))
