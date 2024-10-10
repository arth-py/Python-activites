# Função que executa a ferramenta 'len' sobre a variável
def contar_caracteres(x):
    return len(x)
# Função main a ser executada
def main():
# A variável 'frase' recebe o valor definido pelo usuário
    frase = input('Digite a quantidade de caracteres a serem contados: ').strip()
# Imprime a quantidade de caracteres escritos na variável 'frase'   
    print(f'A quantidade de caracteres digitados é: {contar_caracteres(frase)}')
# Fecha a função 'main'
if __name__ == '__main__':
    main()

