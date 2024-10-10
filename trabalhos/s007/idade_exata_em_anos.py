  
def func_mes(d_atual,m_atual,a_atual,d_nasc,m_nasc,a_nasc):
    if m_atual > m_nasc:
        return a_atual - a_nasc
    elif m_atual < m_nasc:
        return a_atual - a_nasc - 1
    elif m_atual == m_nasc:
        if d_atual > d_nasc:
            return a_atual - a_nasc
        elif d_atual < d_nasc:
            return a_atual - a_nasc - 1
        elif d_atual == d_nasc:
            return a_atual - a_nasc
def main():
    dia_atual = int(input('Insira o dia atual : '))
    mes_atual = int(input('Insira o mês atual : '))
    ano_atual = int(input('Insira o ano atual : '))
    dia_nasc = int(input('Insira o dia de nascimento : '))
    mes_nasc = int(input('Insira o mês de nascimento : '))
    ano_nasc = int(input('Insira o ano de nascimento : '))
    print(f'Sua idade atual é: {func_mes(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc)}')
if __name__ =='__main__':
    main()
