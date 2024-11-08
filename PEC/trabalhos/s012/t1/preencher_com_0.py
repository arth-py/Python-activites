def main():
   lista1 = []
   lista2 = []
   lista3 = []
   lista4 = []
   # Ocupa a lista com zeros
   n = int(input())
   for a in range(n):
       lista1.append(0)
   print(f'{lista1}')
   # Ocupa a lista com números de 1 ao definido pelo usuário no início do código, com uma progressão de uma unidade
   for b in range(1,n+1):
      lista2.append(b)
   print(f'{lista2}')
   # Ocupa a lista com números inteiros definidos pelo usuário
   for c in range(n):
      Ninserido1 = int(input())
      lista3.append(Ninserido1)
   print(f'{lista3}')
   # Ocupa uma lista com números inseridos pelo usuário, mas na ordem inversa de inserção
   for d in range(n):
      Ninserido2 = int(input())
      lista4.insert(0, Ninserido2)
   print(f'{lista4}')
if __name__ == '__main__':
    main()
