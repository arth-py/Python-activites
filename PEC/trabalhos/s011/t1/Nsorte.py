'''O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento.
Escreva um programa que leia a data de nascimento, digitada no formado ddmmaaaa
(um número inteiro com 8 dígitos), e mostre o seu número da sorte. Por exemplo,
quem nasceu em 29/04/1989 deve digitar 29041989 e o programa vai calcular que o
número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).'''
def main():
    Nsorte = 0
    data= int(input())
    while True:
        algarismo = data%10 # Guarda o último digito do número digitado
        data //= 10 # Divide o número recebido por 10
        Nsorte += algarismo # Adiciona ao Número da sorte o algarismo guardado
        if data == 0: # Condição para terminar a repetição quando todos os numeros passarem pela repetição
            break
    print(f'{Nsorte}')
    

if __name__ =='__main__':
    main()
