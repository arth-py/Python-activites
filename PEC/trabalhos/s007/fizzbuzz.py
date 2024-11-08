def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FIZZBUZZ'
    elif x % 3 == 0:
        return 'FIZZ'
    elif x % 5 == 0:
        return 'BUZZ'
    else:
        return x
    
def main():
    numero = int(input('Insira o número : '))
    print(f'{fizzbuzz(numero)}')
if __name__ == '__main__':
    main()
