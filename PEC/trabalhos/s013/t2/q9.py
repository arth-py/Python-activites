

def produto_escal(list1,list2):
    soma = 0
    for a in range(5):
        produto = list1[a] * list2[a]
        soma += produto
    return soma
        

def main():
    list1 = []
    list2 = []
    for i in range(5):
        list1.append(int(input()))
    for l in range(5):
        list2.append(int(input()))
    print(f'{list1}\n{list2}')
    for b in range(4):
        print(f'({list1[b]} x {list2[b]}) + ', end='')
    print(f'({list1[4]} x {list2[4]}) = {produto_escal(list1,list2)}')
        

if __name__ == '__main__':
    main()
