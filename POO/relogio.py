'''1. Exercitando o processo de abstração, modele uma classe Relógio_Digital_Simples com seus estados e
comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus
atributos e execute os métodos criados. Recomendação: criar estados que possam ter seus valores alterados
por seus métodos.'''
# Criação da classe Relógio
class Relogio():
# Criação do Construtor que recebe as instâncias dos objetos
    def __init__(self,horas,minutos):
        self.horas = horas
        self.minutos = minutos

# Função main com 2 objetos
def main():
    hora1 = Relogio(9,34)
    hora2 = Relogio(11,56)
    print(f'0{hora1.horas}:{hora1.minutos}')
    print(f'{hora2.horas}:{hora2.minutos}')
if __name__ == '__main__':
    main()
