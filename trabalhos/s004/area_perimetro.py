# A função 'area_e_perimetro' retorna as variaveis definidas 'area' e 'perimetro'
def area_e_perimetro(l):
    area = l**2
    perimetro = l*4
    return area, perimetro

# A variável 'lado' , convertida para real, recebe o valor definido pelo usuário
lado = float(input('Insira o valor do lado do quadrado em m² para saber sua área e perímetro: ').strip())
# As variáveis 'area' e 'perimetro' recebema  função 'area_e_perimetro' 
area, perimetro = area_e_perimetro(lado)
# Imprime o valor da área do quadrado
print(f' A área desse quadrado é {area:10.4f}m²')
# Imprime o valor do perímetro do quadrado
print(f' O perímetro desse quadrado é{perimetro:10.4f}m²')
