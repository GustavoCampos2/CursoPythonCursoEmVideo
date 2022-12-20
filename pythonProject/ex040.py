n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('A media do aluno foi {}. ALUNO APROVADO'.format(media))
elif media < 5:
    print('A media do aluno foi {}. ALUNO REPROVADO'.format(media))
elif 7 > media >= 5:
    print('A media do aluno foi {}. Aluno de RECUPERAÇÃO'.format(media))
