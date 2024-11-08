'''Foram anotados nomes, idades e alturas de 30 alunos.
Faça um programa que determine quais alunos com mais de
13 anos possuem altura inferior à média de altura dos alunos.'''
def calcular_media(lista):
    return sum(lista)/len(lista)

def main():
    nomes = []
    idades = []
    alturas = []
    for aluno in range(30):
        nomes.append(input())
        idades.append(int(input()))
        alturas.append(float(input()))
    # A função round arredonda o valor de média para duas casas decimais
    # media_arredondada = "{:.2f}".format(media)
    media = round(calcular_media(alturas),2)
    
    print(f'MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for i in range(30):
        if idades[i] > 13:
            if alturas[i] < media:
                print(f'{nomes[i]}')
    

if __name__ == '__main__':
    main()
