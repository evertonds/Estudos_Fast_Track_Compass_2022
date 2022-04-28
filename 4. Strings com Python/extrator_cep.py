endereco = "Rua João Eurico Pandolfi, 13, Casa, Linhares, Espirito Santo, ES, 29900-690"

import re

cep_padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = cep_padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
else:
    print("não tem cep")
