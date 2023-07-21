from bs4 import BeautifulSoup
import requests
import re
import csv
import os

#testes para nao encher a outra pagina de estudo

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = "https://www.leroymerlin.com.br/kit-200-abracadeiras-nylon-3,6x150mm-preto-pacote-kala_1567337335"
req = requests.get(url,headers=headers)
html_content = req.text
soup = BeautifulSoup(html_content, "html.parser")

palavra_chave = 'discount'
contador = 0
padrao = r'\d+'
valores = []
linhas_texto = ''

prod_discount = soup.find('div', class_=re.compile('product-buy-box'))


with open('nome_arquivo', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(prod_discount)

#Read_archive__
with open('nome_arquivo', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        linhas_texto = linhas_texto + ','.join(row) + '\n'


for linha in linhas_texto.split('\n'):
    if palavra_chave in linha:
        match = re.search(padrao, linha)
        if match:
            preco = match.group()
            valores.append(preco)
            contador += 1
            if contador >=50:
                break

valores_str =','.join(valores)

print(valores_str)

'''def desconto():
    if prod_discount is True:
        tem_desconto = print('Possui desconto')
    else:
        n_tem_desconto = print('nao tem desconto')
        ''' 