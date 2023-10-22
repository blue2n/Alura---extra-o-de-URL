import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError ('A URL não é válida')
        
    def get_url_base(self):
        indice_interrogação = self.url.find('?')
        url_base = self.url[:indice_interrogação]
        return url_base

    def get_url_parametros(self):
        indice_interrogação = self.url.find('?')
        url_parametros = self.url[indice_interrogação + 1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
       return self.url + '\n' + 'Parâmentros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' + self.get_url_base()
    
    def __eq__(self, other):
       return self.url == other.url

url = 'bytebank.com/cambio?quantidade=1000&moedaOrigem=libra&moedaDestino=peso'
extrator_url = ExtratorURL(url)

valor_dolar = 5.03 #valor dia 21/10/23
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_convetido = int(quantidade)/valor_dolar
    print('O valor em dolar será: R${0:.2f}'.format(valor_convetido))
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_convetido = int(quantidade)*valor_dolar
    print('O valor em reais será: ${0:.2f}'.format(valor_convetido))
else:
    print('Conversão de cambio para as moedas {} e {} não está disponível'.format(moeda_origem, moeda_destino))