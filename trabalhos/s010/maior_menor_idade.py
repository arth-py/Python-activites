'''Escreva um programa que, para um número indeterminado de pessoas:

leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica
o fim dos dados (flag) e não deve ser considerada;
calcule e escreva o número de pessoas;
calcule e escreva a idade média do grupo;
calcule e escreva a menor idade e a maior idade.'''
# Função para retornar a média
def media(total,n):
    media = total / n
    return media
    

def idade_pessoas():
    # Definição de variáveis
    soma = 0
    idades=[]
    pessoas = 0
    # Definição da repetição
    while True:
        # 'idade' recebe o inteiro definido pelo usuário
        idade=int(input())
        # Condição para o fim da repetição
        if idade == 0:
            break
        # A lista 'idades', adiciona a variável idade
        idades.append(idade)
        pessoas += 1
        soma += idade
        # Invoca a função media_idades, com os respectivos parâmetros
    media_idades = media(soma,pessoas)
    # 'menor_idade' recebe o menor inteiro dentro da lista 'idades'
    menor_idade=min(idades)
    # 'maior_idade' recebe o maior inteiro dentro da lista 'idades'
    maior_idade=max(idades)
    return f'{pessoas}\n{media_idades:.2f}\n{menor_idade}\n{maior_idade}'

def main():
    print(idade_pessoas())
    
if __name__ == '__main__':
    main()
