x = [{'nome': 'caio', 'idade':20}, {'nome':'marcos', 'idade':40}]

x = list(filter(lambda x: x['nome'] == 'caio', x))

print(x)