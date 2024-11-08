# Define a função 'anos' recebendo os parâmetros 'deposito' e 'juros'
def anos(deposito,juros):
    # Definição de variáveis
    ano = 0 
    dobro = deposito * 2
    juros = juros*0.01
    # Repetição indeterminada com condição de que 'deposito' deve ser menor que 'dobro'
    while deposito < dobro:
        # 'deposito' recebe 'deposito' adicionado de 'deposito * juros'
        deposito = deposito + deposito*juros
        ano+=1
    return ano

def main():
    deposito = int(input())
    juros = float(input())
    print(f'{anos(deposito,juros)}')
          
if __name__ == '__main__':
    main()
