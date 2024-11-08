from random import *

print("Gerador de Cumprimentos")
print("-"*22)

adjetivos = ["maravilhoso","acima da média","excelente", 'incrível','habilidoso' ]
hobbies = ["andar de bicicleta","programar","fazer chá" , 'correr' , 'desenhar' ]

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento", nome , ":")

print(nome,"você é", choice(adjetivos),'em', choice(hobbies))
print('De nada!')

