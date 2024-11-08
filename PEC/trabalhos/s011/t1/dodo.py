'''O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África.
A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de animais
nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.

# 6% dos animais dos animais vivos no começo do ano morreram
# o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.
# O programa encerra sua execução quanto a população total cai para menos de 10% da população original.

Escreva um programa que leia a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de
1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira do números, separados
    por vírgula). O programa encerra sua execução quanto a população total cai para menos de 10% da população original.'''

def main():
    populacao = int(input())
    ano=1599
    P_original = populacao # Salvando a população original
    
    while True:
        ano+=1
        mortos =(6/100)*populacao # calcula e guarda a quantidade de mortos
        nascimentos = (1/100)*populacao # cakcula a quantidade de nascimentos
        populacao -= mortos # Atualiza a quantidade da população removendo os mortos
        populacao += nascimentos # Atualiza a quantidade da população adicionando os nascidos
        print(f'{ano},{nascimentos:.0f},{mortos:.0f},{populacao:.0f}')
        if populacao < (10/100)*P_original: # Define a condição para fim da repetição
            break

if __name__ == '__main__':
    main()
