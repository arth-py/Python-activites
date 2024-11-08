'''Escreva um programa que
leia uma quantidade indefinida de
números inteiros  positivos terminada pelo
número 0 (zero). Ao final, o programa deve mostrar
o maior e o menor de todos os números lidos (excluindo
o zero).

'''
def n_maior_menor():
    # 'n_maior' recebe valor 0
    n_maior = 0
    # 'n_menor' recebe valor 100000000000000000
    n_menor = 100000000000000000
    # Repetição indeterminada
    while True:
        # 'opcao' recebe o inteiro definido pelo usuário
        opcao= int(input())
        # Condição para terminar a repetição
        if opcao == 0: break
        # Condição para definir 'n_maior'
        if opcao > n_maior:
            n_maior = opcao
        # Condição para definir 'n_maior'
        if opcao < n_menor:
            n_menor = opcao
    print(f'{n_maior}\n{n_menor}')

def main():
    n_maior_menor()
if __name__ == '__main__':
    main()
