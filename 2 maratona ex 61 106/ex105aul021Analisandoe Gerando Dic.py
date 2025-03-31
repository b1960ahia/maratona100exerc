def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['SITUAÇÃO'] = 'BOA'
        elif r['media'] >= 5:
            r['SITUAÇÃO'] = 'RAZOAVEL'
        else:
            r['SITUAÇÃO'] = 'RUIM'
    return r


resp = notas(6.5, 5.4, 7.6, 3.5, sit=True)
print(resp)

