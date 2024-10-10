def paises1(popA,popB):
    ano=0
    while True:
        popA+=popA*(2/100)
        popB+=popB*(3/100)
        ano+=1
        if popB > popA:
            break
    print(f'{ano}')

def paises2(popA,popB):
    ano=0
    while True:
        popA+=popA*(3/100)
        popB+=popB*(2/100)
        ano +=1
        if popA > popB:
            break
    print(f'{ano}')

def main():
    popB=int(input())
    popA=int(input())
    if popA > popB:
        paises1(popA,popB)
    elif popB > popA:
        paises2(popA,popB)
        

if __name__ == '__main__':
    main()
