# A variável 'anos' definida pelo usuário, é convertida para inteiro
anos=int(input('Insira sua idade em anos: ').strip())
# A variável 'meses' definida pelo usuário, é convertida para inteiro
meses=int(input('Insira seus meses: ').strip())
# A variável 'dias' definida pelo usuário, é convertida para inteiro
dias=int(input('Insira seus dias: ').strip())
# A variável 'anos_em_dias' recebe a variável 'anos' multiplicada por 365
anos_em_dias=anos*365
# A variável 'meses_em_dias' recebe a variável 'meses' multiplicada por 30
meses_em_dias=meses*30
# Imprime a somatória da quantidade de anos, meses e dias, em dias
print(f'Sua idade em dias é : {anos_em_dias + meses_em_dias + dias } dias')
