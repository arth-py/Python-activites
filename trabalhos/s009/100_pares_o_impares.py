def e_par():
    par = 0
    impar = 0
    for n in range(0,100):

        n = int(input())
        if n % 2 == 0:
            par += 1
        elif n % 2 != 0:
            impar += 1
    print(f'{par}\n{impar}')

def main():
    e_par()
if __name__ == '__main__':
    main()
    
