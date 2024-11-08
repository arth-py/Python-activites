# Função para verificar se é par
def par_ou_impar(x):
    return x % 2 == 0

def main():
    NumLista = []
    NumPar= []
    NumImpar= []
    # Repetição para o usuário inserir 20 números e adicionálos a lista
    for i in range(20):
        numero = int(input())
        NumLista.append(numero)
    # Repetição dentro da NumLista 
    for num in NumLista:
        # Condição para verificar se o número é par ou impar adiconando às respectivas listas
        if par_ou_impar(num):
            NumPar.append(num)
        else:
            NumImpar.append(num)
    print(f'{NumLista}\n{NumPar}\n{NumImpar}')
        
        
        
if __name__ == '__main__':
    main()
