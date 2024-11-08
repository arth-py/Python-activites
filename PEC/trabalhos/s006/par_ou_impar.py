def par_impar(x):
    return x % 2 != 0
def main():
    x = int(input('insira o número para saber se ele é par ou impar : ').strip())
    print(f'{par_impar(x)}')
if __name__ == '__main__':
    main()
