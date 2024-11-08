'''Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a) "Telefonou para a vítima ?"

b) "Esteve no local do crime ?"

c) "Mora perto da vítima ?"

d) "Devia para a vítima ?"

e) "Já trabalhou com a vítima ?"

Considere “S” para sim ou “N” para  não. 
O programa deve emitir uma classificação
sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 
2 questões ela deve ser classificada como
"Suspeito", entre 3 ou 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário,
ele será classificado como "Inocente".
'''
def sim_ou_nao(p1,p2,p3,p4,p5):
    if p1[0].upper() == 'S':
        p1 = 1
    elif p1[0].upper() == 'N':
        p1 = 0   
    if p2[0].upper() == 'S':
        p2 = 1
    elif p2[0].upper() == 'N':
        p2 = 0
    if p3[0].upper() == 'S':
        p3 = 1
    elif p3[0].upper() == 'N':
        p3 = 0
    if p4[0].upper() == 'S':
        p4 = 1
    elif p4[0].upper() == 'N':
        p4 = 0
    if p5[0].upper() == 'S':
        p5 = 1
    elif p5[0].upper() == 'N':
        p5 = 0
    return p1 + p2 + p3 + p4 + p5

def crime(p1,p2,p3,p4,p5):

    nivel = sim_ou_nao(p1,p2,p3,p4,p5)

    
    if nivel == 5:
        return 'Assassino'
    elif nivel == 3 or nivel == 4:
        return 'Cúmplice'
    elif nivel == 2: 
        return 'Suspeito'
    else:
        return 'Inocente'
    
def main():
    pergunta1=input("Telefonou para a vítima ?\n")
    pergunta2=input("Esteve no local do crime ?\n")
    pergunta3=input("Mora perto da vítima ?\n")
    pergunta4=input("Devia para a vítima ?\n")
    pergunta5=input("Já trabalhou com a vítima ?\n")
    print(f'Você é {crime(pergunta1,pergunta2,pergunta3,pergunta4,pergunta5)}')
if __name__ == '__main__':
    main()

