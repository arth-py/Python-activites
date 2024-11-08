def data_recente(dia1,mes1,ano1,dia2,mes2,ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}' 
    elif ano2 > ano1:
        return f'{dia2}/{mes2}/{ano2}'
    elif ano2 == ano1:
        if mes1 > mes2:
            return f'{dia1}/{mes1}/{ano1}'
        elif mes2 > mes1:
            return f'{dia2}/{mes2}/{ano2}'
        elif mes2 == mes1:
            if dia1 >= dia2:
                return f'{dia1}/{mes1}/{ano1}'
            elif dia2 >= dia1:
                return f'{dia2}/{mes2}/{ano2}'
def main():
    dia1=int(input('Insira o dia da primeira data : '))
    mes1=int(input('Insira o mês da primeira data : '))
    ano1=int(input('Insira o ano da primeira data : '))
    dia2=int(input('Insira o dia da segunda data : '))
    mes2=int(input('Insira o mês da segunda data : '))
    ano2=int(input('Insira o ano da segunda data : '))
    print(f'A data mais recente é : {data_recente(dia1,mes1,ano1,dia2,mes2,ano2)}')
if __name__ == '__main__':
    main()
    
                
    
