from turtle import *

speed(1)
shape('turtle')
pensize(6)
color('red')
lados=int(input('Insira os lados, por favor: '))
angulo=360/lados
for count in range(lados):
    forward(100)
    right(angulo)

done()
