'''Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito	Média Final
A	>= 9.0
B	>= 7.5 e < 9.0
C	>= 6.0 e < 7.5
D	>= 4.0 e < 6.0
E	< 4.0
O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.

Mensagem	Conceitos
Aprovado	A, B ou C
Reprovado	D ou E'''
def media_final(n1,n2,n3,media_exerc):
    media_final = (n1 + n2 * 2 + n3 * 3 + media_exerc) / 7
    if media_final >= 9.0:
        return f'{media_final:0.2f}\nNota: A\nSituação: Aprovado'
    elif media_final >= 7.5 and media_final < 9.0:
        return f'{media_final:0.2f}\nNota: B\nSituação: Aprovado'
    elif media_final >= 6.0 and media_final < 7.5:
        return f'{media_final:0.2f}\nNota: C\nSituação: Aprovado'
    elif media_final >= 4.0 and media_final < 6.0:
        return f'{media_final:0.2f}\nNota: D\nSituação: Reprovado'
    elif media_final < 4.0:
        return f'{media_final:0.2f}\nNota: E\nReprovado'
def main():
    matricula = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_e = float(input())
    print(f'Matrícula: {matricula}')
    print(f'Média final:{media_final(nota1,nota2,nota3,media_e)}')
if __name__ == '__main__':
    main()
