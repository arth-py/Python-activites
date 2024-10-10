'''escreva um programa que leia um número inteiro entre 100 e 999,
mostre quantos dígitos pares existem nesse número. Por exemplo: 245
tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.
'''
def impar(x):
    return x % 2 == 0

def digito_centena(x):
    centena = x // 100
    if centena < 1:
        del centena
    else:
        return impar(centena)

def digito_dezena(x):
    dezena = x // 10
    return impar(dezena)

def digito_unidade(x):
    unidade = x % 10
    return impar(unidade)
    
def main():
    numero = int(input('Insira o número entre 100 e 999: '''))
    resultado_centena = digito_centena(numero)
    resultado_dezena = digito_dezena(numero)
    resultado_unidade = digito_unidade(numero)

    if resultado_centena and resultado_dezena and resultado_unidade:
        print ('tem 3 dígitos pares')
    elif resultado_centena and resultado_dezena and not resultado_unidade:
        print ('tem 2 dígitos pares')
    elif resultado_centena and not resultado_dezena and resultado_unidade:
        print ('tem 2 dígitos pares')
    elif not resultado_centena and resultado_dezena and resultado_unidade:
        print ('tem 2 dígitos pares')
    elif not resultado_centena and not resultado_dezena and resultado_unidade:
        print ('tem 1 dígitos pares')
    elif not resultado_centena and resultado_dezena and not resultado_unidade:
        print ('tem 1 dígitos pares')
    elif resultado_centena and not resultado_dezena and not resultado_unidade:
        print ('tem 1 dígitos pares')
    elif not resultado_centena and not resultado_dezena and not resultado_unidade:
        print ('tem 0 dígitos pares')
        
    
if __name__ == '__main__':
    main()
            
    
    

        
