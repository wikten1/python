def test():
    return lambda *idade: print(idade)

x = test()

x('caio', 'marcos')