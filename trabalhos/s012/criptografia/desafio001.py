def main():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    chave = int(input())
    letra = input('Por favor, entre com uma letra pra criptografar: ')
    posicao = alfabeto.find(letra)
    novaPosicao = (posicao + chave) % 26
    letraCriptografada = alfabeto[novaPosicao]
    print('Sua letra criptografada é ' , letraCriptografada)

if __name__ == '__main__':
    main()
