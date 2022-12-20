def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


ano = int(input('Em que ano você nasceu? '))
voto(ano)
a1 = voto(ano)
print(a1)
