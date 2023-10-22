url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

#Sanitização da URL
url = url.strip()

#Validação da URL
if url == '':
    raise ValueError('A URL está vazia')

#Separa base e os parâmetros
indice_interrogação = url.find('?')
url_base = url[:indice_interrogação]
url_parametros = url[indice_interrogação + 1:]
print(url_parametros)

#Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_comercial = url_parametros.find('&', indice_valor)

if indice_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_comercial]
print(valor)