# A variável 'n1' definida pelo usuário é convertida para real
n1=float(input('Insira a primeira nota: ').strip())
# A variável 'n2' definida pelo usuário é convertida para real
n2=float(input('Insira a segunda nota: ').strip())
# A variável 'n3' definida pelo usuário é convertida para real
n3=float(input('Insira a terceira nota: ').strip())
# A variável 'media_ponderada' recebe o cálculo da média ponderada
media_ponderada = (((n1*2)+(n2*3)+(n3*5))/10)
# Imprime o valor da média ponderada
print(f'A média ponderada das notas é : {media_ponderada}')
