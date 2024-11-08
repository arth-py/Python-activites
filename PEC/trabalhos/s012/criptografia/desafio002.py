def main():
    alfabeto = 'qbyfzgidjkmoxnlaorspwetvuhc'
    mensagem = input(" Por favor, entre com a mensagem a ser criptografada: ").lower()
    mensagemCriptografada = ""
    chave = int(input("Por favor, entre a chave: "))
    for char in mensagem:
        if char in alfabeto:
            posicao = alfabeto.find(char)
            novaPosicao = (posicao + chave) % 26
            mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
        elif char == ' ':
            pass
        else:
            mensagemCriptografada = mensagemCriptografada + char
        chave+=1

    print("Sua mensagem criptografada é:" , mensagemCriptografada)
if __name__ =='__main__':
    main()
