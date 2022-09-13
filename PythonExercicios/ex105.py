def notas(*notas, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com vária informações sobre a situação da turma.
    """
    soma = maior = menor = 0
    turma = {}
    for c, v in enumerate(notas):
        if c == 0:
            maior = menor = v
        elif v > maior:
            maior = v
        elif v < menor:
            menor = v
        soma += v
    media = soma / len(notas)
    turma['Total'] = len(notas)
    turma['Maior'] = maior
    turma['Menor'] = menor
    turma['Média'] = media
    if sit:
        if media >= 7:
            turma['Situação'] = 'BOA'
        elif 5 < media < 7:
            turma['Situação'] = 'RAZOÁVEL'
        else:
            turma['Situação'] = 'RUIM'
    return turma


resp = notas(5, 9.25, 7.5, 8, 8.2, 5.5, sit=True)
print(resp)
help(notas)
