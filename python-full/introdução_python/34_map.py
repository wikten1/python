x = [{'nome': 'caio', 'idade': 20}, {'nome': 'marcos', 'idade': 22}]

x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor do que 30 anos'} if x ['idade'] < 30 else(x)))