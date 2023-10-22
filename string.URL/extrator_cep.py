import re

endereco = 'Rua Vergueiro 1211, sala 810, Aclimação, São Paulo, SP, 01533-000'

padrao = re.compile('[0-9]{5}[-]{0-1}[0-9]{3}')
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)