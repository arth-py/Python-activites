'''Escreva um programa Python que apresente o menu de opções abaixo:
OPÇÕES: 1 - SAUDAÇÃO 2 - BRONCA 3 - FELICITAÇÃO 0 - FIM

O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:

1 - Olá. Como vai? 2 - Vamos estudar mais. 3 - Meus Parabéns! 0 - Fim de serviço.

Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”.
Enquanto a opção for diferente de 0 (zero) deve-se continuar
apresentando as opções. Obs: use como estrutura de repetição
com teste no final e como estrutura condicional múltipla escolha.'''
# Define a função 'menu'
def menu():
    # Cria a repetição
    while True:
        # Menu é impresso
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        # 'opcao' recebe o valor definido pelo usuário
        opcao=int(input())
        # Condições são definidas para cada caso do usuário
        if opcao == 1:
            print("1 - Olá. Como vai?")
        elif opcao ==2:
            print("2 - Vamos estudar mais.") 
        elif opcao ==3:
            print("3 - Meus Parabéns!") 
        elif opcao ==0:
            break
        elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
            print("Opção inválida.") 
    print('0 - Fim de serviço.')
def main():
    menu()
    
if __name__=='__main__':
    main()
