def par_ou_impar(numero):
    if numero % 2 == 0:
        return numero + 5
    elif numero % 2 != 0:
        return numero + 8
def main():
    numero = int(input('Insira o número, se ele for par, será retornado + 5, se não, será retornado + 8: '))
    print(f'O número final é : {par_ou_impar(numero)}')
if __name__ == '__main__':
    main()
