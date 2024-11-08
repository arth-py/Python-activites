def conversor(c):
    fahrenheit = (c * (9/5) +32 )
    return fahrenheit

def main():
    celcius = float(input())
    print(f'{conversor(celcius):0.2f}')

if __name__ =='__main__':
    main()
