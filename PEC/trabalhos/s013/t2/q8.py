
def main():
    lista =[]
    
    for i in range(20):
        num = int(input())
        if num in lista[0:i+1]:
            continue
        else:
            lista.append(num)
    print(f'{lista}')
if __name__ == '__main__':
    main()
