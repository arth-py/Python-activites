def diferenca(n1,n2,n3):
    dif1_2 = abs(n2 - n1)
    dif1_3 = abs(n3 - n1)
    if dif1_2 > dif1_3:
        return dif1_3
    else:
        return dif1_2
    
def main():
    n1 = int(input('Defina o primeiro valor:\n'))
    n2 = int(input('Defina o segundo valor:\n'))
    n3 = int(input('Defina o terceiro valor:\n'))
    
    dif = diferenca(n1,n2,n3)  
    print(dif)
    
if __name__ == "__main__":
    main()
