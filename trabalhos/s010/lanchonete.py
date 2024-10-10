def lanchonete():
    total=0
    # Repetição indeterminada para imprimir o menu
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")
        # 'opcao' recebe a string definida pelo usuário
        opcao = str(input().strip())
        # 'opcao' é transformada em forma maiúscula
        opcao = opcao.upper()
        # Condições para a escolha do usuário, 'total' recebe total + o respectivo valor
        if opcao == 'H':
            total += 5.50
        if opcao == 'C':
            total += 6.80
        if opcao == 'M':
            total += 4.50
        if opcao == 'A':
            total += 7.00
        if opcao == 'Q':
            total += 4.00
        if opcao == 'X':
            return total
def main():
    print(f'{lanchonete():.2f}')
            
if __name__ =='__main__':
    main()
