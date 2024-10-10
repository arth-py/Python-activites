# Define a função 'portal_do_aluno'
def portal_do_aluno():
    # Cria a repetição indeterminada
    while True:
        nota = float(input())
        # Define a condição para caso o usuário digite um valor inválido
        if nota < 0 or nota > 10:
            print('Nota inválida.')
        # A seguir são condições para a respectiva nota
        elif nota >= 8.5:
            print("A")
            break
        elif nota >= 7.0:
            print("B")
            break
        elif nota >= 5.0:
            print("C")
            break
        elif nota >= 4.0:
            print("D")
            break
        elif nota >= 0.0:
            print("E")
            break
        
def main():
    portal_do_aluno()
    
if __name__ =='__main__':
    main()
