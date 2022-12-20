def notas(*num, sit=False):
    """
    -> função para analisar notas
    :param num: um ou mais notas dos alunos (aceita vairas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionatio com vairas informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    r['media'] = f'{sum(num) / len(num):.2f}'
    return r


resp = notas(9, 2, 1, sit=True)
print(resp)
help(notas)
