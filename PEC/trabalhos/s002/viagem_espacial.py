# Usuário coloca o valor da distância
distancia=input().strip()
# Classificação da informação (inteiro, string ou real)
distancia=int(distancia)
# Usuário coloca o valor da velocidade
velocidade=input().strip()
# Classificação da informação (inteiro, string ou real)
velocidade=int(velocidade)
# Dia recebe 24 horas
dia=24
# Cálculo do tempo distância dividida inteiramente pela velocidade
tempo=(distancia // velocidade)
# Cálculo do número de dias dividindo o tempo levado por 24h encontrando número de dias
dias=(tempo // dia)
# Cálculo das horas que sobraram
horas=(tempo-((tempo//dia)*dia))
# Impressão do resultado
print(dias , 'dias e'  , horas , 'horas')
 

