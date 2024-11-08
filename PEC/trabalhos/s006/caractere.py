def caractere(x):
    if x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
        return 'vogal'
    elif x.lower() == 'b' or x.lower()=='c' or x.lower()=='d' or x.lower() == 'f' or x.lower()=='g' or x.lower()=='h' or x.lower() == 'j' or x.lower()=='k' or x.lower()=='l' or x.lower() == 'm' or x.lower()=='n' or x.lower()=='p' or x.lower() == 'q' or x.lower()=='r' or x.lower()=='s' or x.lower() == 't' or x.lower()=='v' or x.lower()=='w' or x.lower() == 'x' or x.lower()=='y' or x.lower()=='z':
        return 'consoante'
    elif x =='0' or x =='1' or x =='2' or x =='3' or x =='4' or x =='5' or x =='6' or x =='7' or x =='8' or x =='9':
        return 'número'
    else:
        return'símbolo'
def main():
    x = input('Insira um número, consoante ou símbolo para identificá-lo :')

    print(f'{caractere(x)}')
    
if __name__ == '__main__':
    main()
