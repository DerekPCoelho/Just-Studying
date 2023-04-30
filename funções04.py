def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'boa'
        elif r['media'] >= 5:
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'ruim'
    return r


resp = notas(5.5, 2.2,7.7, sit=True)
print(resp)