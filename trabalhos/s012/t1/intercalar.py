
def main():
    listA=[]
    listB=[]
    listC=[]
    #  A lista A receberá 25 inteiros definidos pelo usuário
    for i in range(25):
        numA = int(input())
        listA.append(numA)
    #  A lista B receberá 25 inteiros definidos pelo usuário    
    for n in range(25):
        numB = int(input())
        listB.append(numB)
    # Repetição na qual é adicionado o número da lista A e depois o da lista B 
    for c in range(25):
        listC.append(listA[c])
        listC.append(listB[c])
        
    print(f'{listA}\n{listB}\n{listC}')
    
if __name__ == '__main__':
    main()
