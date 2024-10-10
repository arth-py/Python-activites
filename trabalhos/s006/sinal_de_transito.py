def sinal_de_transito(cor):
    if cor[0].lower() == 'v':
        return 'Siga'
    elif cor[0].lower() == 'a':
        return 'Atenção'
    elif cor[0].lower() == 'e':
        return 'Pare'
    else:
        return 'Aí você não digitou nenhuma cor >:('
def main():
    cor = str(input('Digite a cor do sinal (e - vermelho, v - verde, a - amarelo ) :').strip())
    print (f' {sinal_de_transito(cor)}')
if __name__ == '__main__':
    main()


