'''Escreva um programa que leia um número n. Considere uma lista com n posições,
e então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa.
Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado
e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com
n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.

'''

def main():
    n=int(input())
    # Condição para caso o usuário digite zero, impedindo a execução do código
    if n == 0:
        print('[]')
        print('[]')
        print('SEM NOTAS')
        print('0')
        print('[]')
        return

    soma=0
    lista1 =[]
    Listnotas= []
    Listmedia=[]
    consoante = []
    vogais = 0
    letras=0
    
    # Cria uma lista com números na ordem inversa de inserção do usuário
    for a in range(n):
        numero = float(input())
        lista1.insert(0,numero)
    print(lista1)


    # Cria uma lista com notas e calcula elas a partir da própria lista com
    # sum(soma) len(número de componentes)
    for b in range(n):
        notas =float(input())
        Listnotas.append(notas)
    media = sum(Listnotas)/len(Listnotas)
    print(f'{Listnotas}\n{media:.1f}')
    # Repetição que calcula a quantidade de vogais digitadas pelo usuário
    #Além disso à um uma condicional, caso não seja vogal é adicionado a lista de consoantes
    for d in range(n):
        letra = str(input().strip())
        if letra in 'AaEeIiOoUu':
            vogais+=1
        else:
            consoante.append(letra)
    print(f'{vogais}')
    print(f'{consoante}')
            
    

if __name__ == '__main__':
    main()
    
