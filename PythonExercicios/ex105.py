def notas(*notas, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vária informações sobre a situação da turma.
    """
    turma = dict()
    turma['Total'] = len(notas)
    turma['Maior'] = max(notas)
    turma['Menor'] = min(notas)
    turma['Média'] = sum(notas)/len(notas)
    if sit:
        if sum(notas)/len(notas) >= 7:
            turma['Situação'] = 'BOA'
        elif 5 < sum(notas)/len(notas) < 7:
            turma['Situação'] = 'RAZOÁVEL'
        else:
            turma['Situação'] = 'RUIM'
    return turma


resp = notas(5, 9.25, 7.5, 8, 8.2, 5.5, sit=True)
print(resp)
help(notas)
