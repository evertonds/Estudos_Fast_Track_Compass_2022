url = "bytebank.com/cambio?moedaOrigem=real"
print(url)


indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
<<<<<<< HEAD
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

=======
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)
>>>>>>> parent of 3c0b2c5 (Adicionando método len)
