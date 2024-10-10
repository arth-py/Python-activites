
def main():
    ListNotas = []
    ListIndices = []
    contador = 0
    # Repetição na qual o usuário insere 50 notas adicionadas a uma lista
    for i in range(50):
        nota= float(input())
        ListNotas.append(nota)
    # Repetição onde cada número da lista MAIOR OU IGUAL A 6 terá seu índice adicionado à lista
    for n in ListNotas:
        if n >= 6:
            ListIndices.append(contador)
        contador +=1
    
    print(f'{ListIndices}')
            
    
if __name__ == '__main__':
    main()
