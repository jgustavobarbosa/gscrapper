# -*- coding: utf-8 -*-
"""dados_gs.ipynb
direitos @janioguga
"""
""""
caso seja necessário instalação dos seguintes pagostes
!pip3 install scholarly
!pip3 install bibtexparser
!pip install FreeProxy
!pip install scholarly_publications

"""
###Pesquisa por autor"""
from scholarly import scholarly
import time
import pandas as pd
import ast
import re
import requests
import time
from fp.fp import FreeProxy
from scholarly import scholarly, ProxyGenerator
import time
import random
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
from scipy import stats
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from scholarly import scholarly


search_query = scholarly.search_author('Janio Gustavo Barbosa')

# Iinteração de resultados quando o autor nao for encontrado

for author in search_query:
    
    # Informação do autor ja é preenchida no dicionário
    print(author)
else:
    print("No authors found.")

import pandas as pd
from scholarly import scholarly

def pesquisar_autor(nome_autor):
    search_query = scholarly.search_author(nome_autor)
    for author in search_query:
        
    # Informação do autor ja é preenchida no dicionário
        return author
    return None

# Lista de autores para pesquisar / exemplo de pesquisa 
#autores = ["Herbert Leopoldo de Freitas Goes", "Hosanna Pattrig Fertonani", "Daiana Bonfim", "Antonio da Cruz Gouveia Mendes", "Judith Rafaelle Oliveira Pinho", "Judith Rafaelle Oliveira Pinho", "Paola Trindade Garcia",
 #          "Célia Regina Pierantoni","Katia Rejane de Medeiros", "Mario Roberto Dal Poz", "Mário César Scheffer","Marilena Cordeiro Dias Villela Corrêa", "Marilena Cordeiro Dias Villela Corrêa" ]

autores = [
    "Maria Wanderleya de Lavor",
    "Estela Maria Leite Meirelles Monteiro",
    "Nivaldo Carneiro Junior",
    "Carla Gianna Luppi",
    "Emanuella Pinheiro de Farias Bispo",
    "Barbara Patricia da Silva Lima",
    "Fernanda de Freitas Mendonça",
    "Patrícia Campos Pavan Baptista",
    "Chennyfer Dobbins Abi Rached",
    "Wilza Carla Spiri",
    "Silvana Andréa Molina Lima",
    "Ilda Cecília Moreira da Silva",
    "Lucrecia Helena Loureiro",
    "Fernanda Campos Sousa de Almeida",
    "Gilberto Alfredo Pucca Junior",
    "Carla Andrea Trape",
    "Alexandre Pazetto Balsanelli",
    "Isabel Cristina Kowal Olm Cunha",
    "Tatiane Araujo dos Santos",
    "Marina Peduzzi",
    "Maria Bernadete de Sousa Costa",
    "José da Paz Oliveira Alvarenga",
    "Robsmeire Calvo Melo Zurita",
    "Rodrigo Jensen",
    "Débora Rodrigues Vaz",
    "Helena Eri Shimizu",
    "Edgar Merchan-Hamann",
    "Mariana Izabel Sena Barreto de Melo",
    "Maria Elizangela Ramos Junqueira",
    "Patricia Carvalho de Oliveira",
    "Silvio Aparecido Fonseca",
    "Josue Souza Gleriano",
    "Thatianny Tanferri de Brito Paranaguá",
    "Lislaine Aparecida Fracolli",
    "Claudia Flemming Colussi",
    "Maria Teresa Bustamante Teixeira",
    "Patricia Tavares dos Santos",
    "Anaclara Ferreira Veiga Tipple",
    "Silvana de Lima Vieira dos Santos",
    "Liziane Cassia Carlesso",
    "Michael Ferreira Machado",
    "Carlos Dornels Freire de Souza",
    "Cristiane Alves Paz de Carvalho",
    "Juliana Alves Leite Leal",
    "Luciane Cristina Feltrin de Oliveira",
    "Herbert Leopoldo de Freitas Goes",
    "Hosanna Pattrig Fertonani",
    "João Tadeu de Andrade",
    "Preciliana Barreto de Morais",
    "Pedro Vasconcelos Maia do Amaral",
    "Antonio da Cruz Gouveia Mendes",
    "Judith Rafaelle Oliveira Pinho",
    "Paola Trindade Garcia",
    "Tania Cristina França da Silva",
    "Carinne Magnago",
    "Maria Francisca de Paula Soares",
    "Alessandra Brunoro Motta Loss",
    "Camila Cardoso Caixeta",
    "Patrícia Martins Montanari",
    "Lívia Keismanas de Ávila",
    "Hemílio Fernandes Campos Coêlho",
    "Mario Roberto Dal Poz",
    "Mário César Scheffer",
    "Sandra Lucia Correia Lima",
    "Debora Silva Teixeira",
    "Rita de Cássia Franco Rêgo",
    "Veronica Maria Cadena Lima",
    "Míriam Thaís Guterres Dias",
    "Isabela Aparecida de Oliveira Lussi",
    "Thelma Simões Matsukura"
]


# Lista para armazenar os dados de todos os autores
dados_autores = []

# Pesquisar cada autor
for autor in autores:
    resultado = pesquisar_autor(autor)
    if resultado:
        dados_autores.append(resultado)
    else:
        print(f"Nenhum autor encontrado para: {autor}")

# Verificar se encontramos algum autor
if dados_autores:
    # Criar um DataFrame com os dados dos autores
    df = pd.DataFrame(dados_autores)

    # Salvar o DataFrame em uma planilha Excel
    df.to_excel("dados_autores.xlsx", index=False)
    print("Dados dos autores salvos em 'dados_autores.xlsx'")
else:
    print("Nenhum autor encontrado para salvar na planilha.")

df

from scholarly_publications import fetch_publications

# capturando todas as publica~\oes por ID de autor

publications = fetch_publications('ghw4vNkAAAAJ')

# capturando dados especificos de publicação por id 
#publications = fetch_publications('<author_id>', max_publications=<number_of_publications>)

# capturando todas as publicações de um autor por id capturando suas citações pubdate/cited
#publications = fetch_publications('<author_id>', sortby='<pubdate/cited>')
# Verificar se encontramos algum autor
if publications:
    # Criar um DataFrame com os dados dos autores
    df_publications = pd.DataFrame(publications)

    # Salvar o DataFrame em uma planilha Excel
    df_publications.to_excel("/content/drive/MyDrive/Fiocruz/publicacoes/Helena_shimizu_publicacoes.xlsx.xlsx", index=False)
    print("Dados dos autores salvos em 'dados_autores_publicação.xlsx'")
else:
    print("Nenhum autor encontrado para salvar na planilha.")


print(publications)

df_publications

import pandas as pd
from scholarly import scholarly
from scholarly_publications import fetch_publications
import os

def pesquisar_autor(nome_autor):
    search_query = scholarly.search_author(nome_autor)
    for author in search_query:
        return author
    return None

def buscar_e_salvar_publicacoes(scholar_id, nome_autor):
    publications = fetch_publications(scholar_id)
    if publications:
        df_publications = pd.DataFrame(publications)

        # Criar uma pasta para as publicações se não existir
        if not os.path.exists('publicacoes'):
            os.makedirs('publicacoes')

        # Salvar o DataFrame em uma planilha Excel
        nome_arquivo = f"/content/drive/MyDrive/Fiocruz/publicacoes/{nome_autor.replace(' ', '_')}_publicacoes.xlsx"
        df_publications.to_excel(nome_arquivo, index=False)
        print(f"Publicações de {nome_autor} salvas em '{nome_arquivo}'")
    else:
        print(f"Nenhuma publicação encontrada para {nome_autor}")

# Lista de autores para pesquisar
autores = [
    "Maria Wanderleya de Lavor",
    "Estela Maria Leite Meirelles Monteiro",
    "Nivaldo Carneiro Junior",
    "Carla Gianna Luppi",
    "Emanuella Pinheiro de Farias Bispo",
    "Barbara Patricia da Silva Lima",
    "Fernanda de Freitas Mendonça",
    "Patrícia Campos Pavan Baptista",
    "Chennyfer Dobbins Abi Rached",
    "Wilza Carla Spiri",
    "Silvana Andréa Molina Lima",
    "Ilda Cecília Moreira da Silva",
    "Lucrecia Helena Loureiro",
    "Fernanda Campos Sousa de Almeida",
    "Gilberto Alfredo Pucca Junior",
    "Carla Andrea Trape",
    "Alexandre Pazetto Balsanelli",
    "Isabel Cristina Kowal Olm Cunha",
    "Tatiane Araujo dos Santos",
    "Marina Peduzzi",
    "Maria Bernadete de Sousa Costa",
    "José da Paz Oliveira Alvarenga",
    "Robsmeire Calvo Melo Zurita",
    "Rodrigo Jensen",
    "Débora Rodrigues Vaz",
    "Helena Eri Shimizu",
    "Edgar Merchan-Hamann",
    "Mariana Izabel Sena Barreto de Melo",
    "Maria Elizangela Ramos Junqueira",
    "Patricia Carvalho de Oliveira",
    "Silvio Aparecido Fonseca",
    "Josue Souza Gleriano",
    "Thatianny Tanferri de Brito Paranaguá",
    "Lislaine Aparecida Fracolli",
    "Claudia Flemming Colussi",
    "Maria Teresa Bustamante Teixeira",
    "Patricia Tavares dos Santos",
    "Anaclara Ferreira Veiga Tipple",
    "Silvana de Lima Vieira dos Santos",
    "Liziane Cassia Carlesso",
    "Michael Ferreira Machado",
    "Carlos Dornels Freire de Souza",
    "Cristiane Alves Paz de Carvalho",
    "Juliana Alves Leite Leal",
    "Luciane Cristina Feltrin de Oliveira",
    "Herbert Leopoldo de Freitas Goes",
    "Hosanna Pattrig Fertonani",
    "João Tadeu de Andrade",
    "Preciliana Barreto de Morais",
    "Pedro Vasconcelos Maia do Amaral",
    "Antonio da Cruz Gouveia Mendes",
    "Judith Rafaelle Oliveira Pinho",
    "Paola Trindade Garcia",
    "Tania Cristina França da Silva",
    "Carinne Magnago",
    "Maria Francisca de Paula Soares",
    "Alessandra Brunoro Motta Loss",
    "Camila Cardoso Caixeta",
    "Patrícia Martins Montanari",
    "Lívia Keismanas de Ávila",
    "Hemílio Fernandes Campos Coêlho",
    "Mario Roberto Dal Poz",
    "Mário César Scheffer",
    "Sandra Lucia Correia Lima",
    "Debora Silva Teixeira",
    "Rita de Cássia Franco Rêgo",
    "Veronica Maria Cadena Lima",
    "Míriam Thaís Guterres Dias",
    "Isabela Aparecida de Oliveira Lussi",
    "Thelma Simões Matsukura"
]

# Lista para armazenar os dados de todos os autores
dados_autores = []

# Pesquisar cada autor
for autor in autores:
    resultado = pesquisar_autor(autor)
    if resultado:
        dados_autores.append(resultado)
    else:
        print(f"Nenhum autor encontrado para: {autor}")

# Verificar se encontramos algum autor
if dados_autores:
    # Criar um DataFrame com os dados dos autores
    df = pd.DataFrame(dados_autores)

    # Salvar o DataFrame em uma planilha Excel
    df.to_excel("dados_autores.xlsx", index=False)
    print("Dados dos autores salvos em 'dados_autores.xlsx'")

    # Buscar e salvar publicações para cada autor
    for index, row in df.iterrows():
        if 'scholar_id' in row and row['scholar_id']:
            buscar_e_salvar_publicacoes(row['scholar_id'], row['name'])
        else:
            print(f"scholar_id não encontrado para {row['name']}")

else:
    print("Nenhum autor encontrado para salvar na planilha.")

"""https://scholar.google.com/scholar?as_q=&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=Judith+Rafaelle+Oliveira+Pinho&as_publication=&as_ylo=&as_yhi=&hl=pt-BR&as_sdt=0%2C5"""



search_query = scholarly.search_pubs('engajamento')

# e "educação profissional e tecnológica"
# e "educação a distância"

# Iterate through the results and handle the case when no results are found.
try:
    for pub in search_query:
        print(pub)  # Print the entire publication dictionary
        time.sleep(10)  # Wait xx seconds before the next request
except MaxTriesExceededException:
    print("Google Scholar is blocking requests. Try again later or check your network connection.")
else:
    print("No publications found.")

search_query = scholarly.search_pubs('engajamento e educação profissional e tecnológica')

# Iterate through the results and handle the case when no results are found.
for pub in search_query:
    print(next(search_query))
    time.sleep(5)
else:
    print("No authors found.")

def safe_eval(s):
    # Remove o objeto PublicationSource não serializável
    s = re.sub(r'<PublicationSource\.[^:]+: ([^>]+)>', r'\1', s)
    return ast.literal_eval(s)

# Lista para armazenar os dados de todas as linhas
all_data = []

# Ler o arquivo de entrada
with open('/content/engajamento_ead.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Converter a string em dicionário
        data = safe_eval(line.strip())

        # Extrair os dados do dicionário 'bib'
        bib_data = data.pop('bib', {})
        data.update(bib_data)

        # Converter listas em strings
        for key, value in data.items():
            if isinstance(value, list):
                data[key] = ', '.join(map(str, value))

        all_data.append(data)

# Criar um DataFrame com todos os dados
df = pd.DataFrame(all_data)

# Salvar o DataFrame como um arquivo Excel
df.to_excel('/content/engajamento_ead.xlsx', index=False)

print("Dados exportados para 'dados_judicialização_formatado.xlsx'")

df

# @title Number of Citations by Publication Year

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(df['pub_year'], df['num_citations'])
plt.xlabel('Publication Year')
plt.ylabel('Number of Citations')
_ = plt.title('Number of Citations by Publication Year')

pg = ProxyGenerator()
success = pg.ScraperAPI("059d2fdb5a2e5d35480f1b638fc9105c")
scholarly.use_proxy(pg)


search_query = scholarly.search_pubs('engajamento e educação a distância')

# Iterate through the results and handle the case when no results are found.
try:
    for pub in search_query:
        print(pub)  # Print the entire publication dictionary
        time.sleep(8)  # Wait how many seconds you set up before the next request
except MaxTriesExceededException:
    print("Google Scholar is blocking requests. Try again later or check your network connection.")
else:
    print("No publications found.")

def set_new_proxy():
    while True:
        proxy = FreeProxy(rand=True, timeout=5).get()
        pg = ProxyGenerator()
        proxy_works = pg.SingleProxy(http=proxy, https=proxy)
        if proxy_works:
            scholarly.use_proxy(pg)
            break
    print("Working proxy:", proxy)
    return proxy

set_new_proxy()

while True:
    try:
        search_query = scholarly.search_pubs('força de trabalho em saúde cnes')
        print("Got the results of the query")
        break
    except Exception as e:
        print("Trying new proxy")
        set_new_proxy()

pub = next(search_query)
print(pub)


while True:
    try:
        filled = pub.fill()
        print("Filled the publication")
        break
    except Exception as e:
        print("Trying new proxy")
        set_new_proxy()

print(filled)

!pip install scholarly'[tor]'
!pip install scholarly[tor]

# Retrieve the author's data, fill-in, and print

# Get an iterator for the author results

search_query = scholarly.search_author('Míriam Thais Guterres Dias')

# Retrieve the first result from the iterator
first_author_result = next(search_query)
scholarly.pprint(first_author_result)

# Retrieve all the details for the author
author = scholarly.fill(first_author_result )
scholarly.pprint(author)

# Take a closer look at the first publication
first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
scholarly.pprint(first_publication_filled)

# Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author['publications']]
print(publication_titles)

# Which papers cited that publication?
citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
print(citations)

"""## CODIGO COM TENTATIVA DE ALTERAÇÃO DE PROXY"""

def set_new_proxy():
    attempts = 0
    while attempts < 10:  # Limite o número de tentativas
        try:
            proxy = FreeProxy(rand=True, timeout=1).get()
            pg = ProxyGenerator()
            proxy_works = pg.SingleProxy(http=proxy, https=proxy)
            if proxy_works:
                scholarly.use_proxy(pg)
                print("Working proxy:", proxy)
                return proxy
        except Exception as e:
            print(f"Proxy error: {e}")
        attempts += 1
        time.sleep(6)  # Espere um pouco entre as tentativas
    raise Exception("Não foi possível encontrar um proxy funcionando após 10 tentativas")

def perform_search(query):
    max_attempts = 9
    for attempt in range(max_attempts):
        try:
            set_new_proxy()
            search_query = scholarly.search_pubs(query)
            pub = next(search_query)
            print("Publicação encontrada:", pub)
            filled = pub.fill()
            print("Detalhes da publicação preenchidos")
            return filled
        except Exception as e:
            print(f"Erro na tentativa {attempt + 1}: {e}")
            if attempt == max_attempts - 1:
                print("Número máximo de tentativas atingido. Não foi possível completar a busca.")
                return None
        time.sleep(2)  # Espere um pouco entre as tentativas

# Uso
query = 'gestão do trabalho em saúde'
result = perform_search(query)

if result:
    print(result)
else:
    print("Não foi possível obter os resultados.")
# Lista de proxies
proxies = [
    "http://72.10.164.178:29503",
    "http://185.105.91.62:4444",
    "http://217.182.55.226:80",
    "socks4://192.111.139.163:19404",
    "socks4://198.12.253.239:64741",
    "http://72.10.164.178:29503",
    "http://185.105.91.62:4444",
    "http://217.182.55.226:80",
    "socks4://192.111.139.163:19404",
    "socks4://198.12.253.239:64741",
    "http://8.213.151.128:3128",
    "http://15.204.216.229:5534",
    "http://34.143.221.240:8103",
    "http://91.92.244.233:80",
    "http://111.26.177.28:9091",
    "socks4://192.252.209.155:14455",
    "socks4://47.122.65.254:3128",
    "http://94.241.170.152:6666",
    "http://51.250.107.5:3128",
    "http://223.113.80.158:9091",
    "http://213.218.228.253:80",
    "http://185.105.88.63:4444",
    "http://39.125.131.121:80",
    "http://67.43.236.20:11269",
    "socks4://202.137.24.19:7890",
    "http://47.243.92.199:3128",
    "http://35.185.196.38:3128",
    "http://103.127.1.130:80",
    "http://67.43.236.20:6839",
    "socks4://68.71.247.130:4145",
    "socks4://41.79.10.218:4673",
    "http://85.209.153.174:8888",
    "http://67.43.236.18:19165",
    "http://103.36.136.138:8090",
    "http://85.209.153.175:80",
    "http://117.54.114.99:80",
    "http://162.245.85.220:80",
    "http://81.223.232.91:80",
    "socks4://109.248.236.150:9898",
    "http://103.85.181.82:8080",
    "http://103.49.202.252:80",
    "http://103.153.154.6:80",
    "http://58.20.248.139:9002",
    "http://189.240.60.163:9090",
    "http://178.48.68.61:18080",
    "http://72.10.160.91:2671",
    "http://161.34.39.55:9999",
    "http://45.229.31.33:11211",
    "http://91.189.177.190:3128",
    "http://72.10.164.178:32605",
    "http://91.92.155.207:3128",
    "http://72.10.164.178:29343",
    "socks4://192.111.138.29:4145",
    "socks4://79.112.127.195:3128",
    "socks4://190.6.141.30:999",
    "http://210.236.68.210:8080",
    "http://84.252.75.136:4444",
    "http://206.84.40.62:8080",
    "http://67.43.227.228:24585",
    "http://72.10.164.178:10319",
    "http://67.43.227.228:32707",
    "http://152.26.229.88:9443",
    "http://85.209.153.173:8888",
    "http://185.224.170.45:8088",
    "http://35.245.75.186:6666",
    "http://37.247.52.248:80",
    "http://103.59.45.53:8080",
    "http://67.43.236.20:18219",
    "http://23.166.88.240:3128",
    "http://202.152.51.44:8080",
    "socks4://72.195.101.99:4145",
    "http://72.10.164.178:2643",
    "socks4://116.99.225.51:30542",
    "http://38.183.209.231:8080",
    "http://177.44.223.109:8080",
    "http://67.43.227.227:10099",
    "http://154.16.146.48:80",
    "http://62.33.53.248:3128",
    "http://67.43.227.228:18401",
    "http://20.219.144.149:3128",
    "http://187.79.146.98:8080",
    "http://84.252.74.190:4444",
    "http://177.19.167.242:80",
    "http://190.61.84.166:9812",
    "http://138.97.119.10:8080",
    "http://183.234.215.11:8443",
    "http://27.147.218.162:8080",
    "http://182.253.39.205:8080",
    "http://185.105.90.88:4444",
    "http://150.136.4.250:3128",
    "http://187.1.181.124:23500",
    "http://103.159.194.97:8080",
    "http://178.34.190.6:8080",
    "http://67.43.227.227:14193",
    "http://102.33.102.218:8080",
    "socks4://107.180.90.88:46287",
    "http://103.110.36.18:83",
    "http://121.227.31.32:8118",
    "http://47.251.70.179:80",
    "http://190.94.212.149:999",
    "http://183.134.101.187:3128",
    "http://103.147.134.238:1111",
    "http://89.35.237.187:3128",
    "http://85.209.153.175:8888",
    "http://15.204.216.229:15378",
    "http://8.212.107.200:80",
    "http://201.77.108.25:999",
    "http://15.204.216.229:15183",
    "http://47.90.205.231:33333",
    "socks5://117.74.65.207:80",
    "http://190.103.177.131:80",
    "http://67.43.228.251:9385",
    "http://103.99.136.6:8090",
    "http://51.89.255.67:80",
    "http://116.235.238.47:3128",
    "http://103.69.20.115:58080",
    "http://218.23.15.154:9002",
    "http://138.68.235.51:80",
    "http://103.87.85.198:80",
    "http://15.204.216.229:15905",
    "http://103.228.246.131:7070",
    "http://67.43.236.20:2775",
    "http://185.224.170.44:8088",
    "http://201.91.82.155:3128",
    "http://109.86.182.203:3128",
    "http://103.137.83.120:8080",
    "http://4.155.2.13:80",
    "http://103.239.252.212:58080",
    "http://27.54.71.234:8080",
    "http://36.67.199.171:8080",
    "http://57.129.18.78:80",
    "http://185.221.219.98:3128",
    "http://103.48.68.75:83",
    "http://43.255.113.232:80",
    "http://202.5.40.21:5020",
    "http://197.248.75.221:8103",
    "http://15.204.216.229:20757",
    "http://103.203.173.49:84",
    "http://183.215.23.242:9091",
    "http://103.133.221.251:80",
    "http://200.155.142.98:8080",
    "http://85.192.63.67:80",
    "http://171.244.60.55:8080"
  ]


def get_random_proxy():
    proxy = random.choice(proxies)
    return proxy.split('://')[-1]  # Remove o protocolo (http:// ou https://) se presente

def search_with_proxy(query):
    pg = ProxyGenerator()
    proxy = get_random_proxy()
    try:
        if pg.SingleProxy(http=proxy, https=proxy):
            scholarly.use_proxy(pg)
            print(f"Using proxy: {proxy}")

            try:
                search_query = scholarly.search_pubs(query)
                results_found = False

                for pub in search_query:
                    print(pub)
                    results_found = True
                    time.sleep(8)  # Espera 5 segundos entre as requisições

                if not results_found:
                    print("Nenhuma publicação encontrada.")

            except Exception as e:
                print(f"Erro ao usar o proxy {proxy}: {str(e)}")
                return False
        else:
            print(f"Falha ao configurar o proxy: {proxy}")
            return False
    except Exception as e:
        print(f"Erro ao configurar o proxy {proxy}: {str(e)}")
        return False

    return True

def main():
    query = 'gestão do trabalho em saúde'
    max_attempts = 40
    attempt = 2

    while attempt < max_attempts:
        if search_with_proxy(query):
            break
        attempt += 1
        print(f"Tentativa {attempt} de {max_attempts} falhou. Tentando outro proxy...")

    if attempt == max_attempts:
        print("Todas as tentativas falharam. Por favor, tente novamente mais tarde.")

if __name__ == "__main__":
    main()

"""# Modelo TM para palavras chaves nos artigos mais citados"""

ft = pd.read_excel("/content/engajamento_ead.xlsx")

ft.columns

"""###Ajuste do arquivo de citação retirado do Google Scholar"""

ft.drop(columns=['container_type'], inplace=True, axis=1)
ft.drop(columns=['source'], inplace=True, axis=1)
ft.drop(columns=['filled'], inplace=True, axis=1)
ft.drop(columns=['pub_url'], inplace=True, axis=1)
ft.drop(columns=['author_id'], inplace=True, axis=1)
ft.drop(columns=['url_scholarbib'], inplace=True, axis=1)
ft.drop(columns=['citedby_url'], inplace=True, axis=1)
ft.drop(columns=['url_related_articles'], inplace=True, axis=1)
ft.drop(columns=['eprint_url'], inplace=True, axis=1)
ft.drop(columns=['url_add_sclib'], inplace=True, axis=1)
ft.drop(columns=['periodico'], inplace=True, axis=1)
ft.to_excel("/content/dados_ft_formatado.xlsx")

jud = pd.read_excel("/content/engajamento_ead.xlsx")
jud.drop(columns=['container_type'], inplace=True, axis=1)
jud.drop(columns=['source'], inplace=True, axis=1)
jud.drop(columns=['filled'], inplace=True, axis=1)
jud.drop(columns=['pub_url'], inplace=True, axis=1)
jud.drop(columns=['author_id'], inplace=True, axis=1)
jud.drop(columns=['url_scholarbib'], inplace=True, axis=1)
jud.drop(columns=['citedby_url'], inplace=True, axis=1)
jud.drop(columns=['url_related_articles'], inplace=True, axis=1)
jud.drop(columns=['eprint_url'], inplace=True, axis=1)
jud.drop(columns=['url_add_sclib'], inplace=True, axis=1)

jud.to_excel("/content/engajamento_ead_formatado_min.xlsx")



# Baixar recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Função de pré-processamento
def preprocess_text(text):
    if pd.isna(text):
        return ""
    # Remover pontuação e converter para minúsculas
    text = re.sub(r'[^\w\s]', '', str(text).lower())

    # Tokenização
    tokens = word_tokenize(text)

    # Remover stopwords (inglês e português)
    stop_words = set(stopwords.words('english') + stopwords.words('portuguese'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lematização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(tokens)

# Carregar os dados (assumindo que você tem um DataFrame chamado 'df')
# df = pd.read_csv('seu_arquivo.csv')
df = ft
# Aplicar pré-processamento
df['processed_text'] = df['title'].fillna('') + ' ' + df['abstract'].fillna('')
df['processed_text'] = df['processed_text'].apply(preprocess_text)

# Criar matriz de termos
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=list(set(stopwords.words('english') + stopwords.words('portuguese'))))
doc_term_matrix = vectorizer.fit_transform(df['processed_text'])

# Modelagem de Tópicos com LDA
num_topics = 10  # Você pode ajustar este número
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
lda_output = lda_model.fit_transform(doc_term_matrix)

# Adicionar tópicos ao DataFrame
df['dominant_topic'] = lda_output.argmax(axis=1)

# Análise de Citações e outras características
analysis_columns = ['num_citations', 'gsrank', 'pub_year']
topic_stats = df.groupby('dominant_topic')[analysis_columns + ['venue']].agg({
    'num_citations': ['mean', 'median', 'std'],
    'gsrank': ['mean', 'median'],
    'pub_year': ['mean', 'median'],
    'venue': lambda x: x.value_counts().index[0]  # Modo (área mais comum)
})

# Achatando os níveis de coluna multindex
topic_stats.columns = ['_'.join(col).strip() for col in topic_stats.columns.values]

print("Estatísticas por tópico:")
print(topic_stats)

# Teste ANOVA para citações
topic_groups = [group for _, group in df.groupby('dominant_topic')['num_citations']]
f_statistic, p_value = stats.f_oneway(*topic_groups)
print(f"\nResultado do teste ANOVA para citações: F-statistic = {f_statistic}, p-value = {p_value}")

# Extração de Palavras-Chave
def get_top_words(topic_idx, n_words=10):
    topic = lda_model.components_[topic_idx]
    top_words = [(vectorizer.get_feature_names_out()[i], topic[i])
                 for i in topic.argsort()[:-n_words - 1:-1]]
    return dict(top_words)

topic_keywords = {i: get_top_words(i) for i in range(num_topics)}

# TF-IDF para palavras-chave específicas
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words=list(set(stopwords.words('english') + stopwords.words('portuguese'))))
tfidf_matrix = tfidf_vectorizer.fit_transform(df['processed_text'])

# Visualização
plt.figure(figsize=(12, 6))
plt.bar(topic_stats.index, topic_stats['num_citations_mean'])
plt.title('Média de Citações por Tópico')
plt.xlabel('Tópico')
plt.ylabel('Média de Citações')
plt.show()

# Nuvem de palavras para o tópico mais citado
most_cited_topic = topic_stats['num_citations_mean'].idxmax()
wordcloud = WordCloud(background_color='white').generate_from_frequencies(topic_keywords[most_cited_topic])
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f'Palavras-chave do Tópico Mais Citado (Tópico {most_cited_topic})')
plt.show()

# Imprimir palavras-chave dos tópicos mais citados
top_3_topics = topic_stats['num_citations_mean'].nlargest(3).index
print("\nPalavras-chave dos 3 tópicos mais citados:")
for topic in top_3_topics:
    print(f"\nTópico {topic}:")
    for word, weight in topic_keywords[topic].items():
        print(f"{word}: {weight:.4f}")

# Análise de correlação
correlation_features = ['num_citations', 'gsrank', 'pub_year']
correlation_matrix = df[correlation_features].corr()
print("\nMatriz de Correlação:")
print(correlation_matrix)

# Modelo de regressão para prever citações
X = df[['gsrank', 'pub_year']]
y = df['num_citations']

# Remover linhas com valores NaN
X_clean = X.dropna()
y_clean = y[X_clean.index]

# Padronizar as features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_clean)

# Criar e treinar o modelo
model = LinearRegression()
model.fit(X_scaled, y_clean)

print("\nCoeficientes do modelo de regressão:")
for feature, coef in zip(X_clean.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercepto: {model.intercept_:.4f}")

# Análise por área do conhecimento (venue)
venue_stats = df.groupby('venue')['num_citations'].agg(['mean', 'median', 'count'])
venue_stats = venue_stats.sort_values('mean', ascending=False)
print("\nEstatísticas de citações por área do conhecimento:")
print(venue_stats)

# Visualização das top 10 áreas mais citadas
plt.figure(figsize=(12, 6))
venue_stats.head(10)['mean'].plot(kind='bar')
plt.title('Top 10 Áreas do Conhecimento por Média de Citações')
plt.xlabel('Área do Conhecimento')
plt.ylabel('Média de Citações')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Baixar recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Lista de palavras adicionais para remover
additional_words = ['brasil', 'brasileiro', 'sobre', 'público', 'publicas', 'estado', 'curso',
                    'direito', 'saúde', 'judicialização', 'processos', 'judiciais', 'fenomeno',
                    'leis', 'possível', 'análise', 'fenômeno', 'dísponível em: ', 'saúde', 'sistema', 'trabalho',
                    'trabalhador', 'força', 'nacional', 'sus', 'ea', 'único']

# Função de pré-processamento
def preprocess_text(text):
    if pd.isna(text):
        return ""
    # Remover pontuação e converter para minúsculas
    text = re.sub(r'[^\w\s]', '', str(text).lower())

    # Tokenização
    tokens = word_tokenize(text)

    # Remover stopwords (inglês e português) e palavras adicionais
    stop_words = set(stopwords.words('english') + stopwords.words('portuguese') + additional_words)
    tokens = [token for token in tokens if token not in stop_words]

    # Lematização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(tokens)

#Carregar dados de df
# df = pd.read_csv('seu_arquivo.csv')
df = ft

# Remover "Disponível em: " da coluna 'venue'
def remove_disponivel_em(text):
    if isinstance(text, str):
        return text.replace("Disponível em:", "")
    return text

df['venue'] = df['venue'].apply(remove_disponivel_em)



# Aplicar pré-processamento
df['processed_text'] = df['title'].fillna('') + ' ' + df['abstract'].fillna('')
df['processed_text'] = df['processed_text'].apply(preprocess_text)

# Criar matriz de termos
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words=list(set(stopwords.words('english') + stopwords.words('portuguese') + additional_words)))
doc_term_matrix = vectorizer.fit_transform(df['processed_text'])

# Modelagem de Tópicos com LDA
num_topics = 10  # Você pode ajustar este número
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
lda_output = lda_model.fit_transform(doc_term_matrix)

# Adicionar tópicos ao DataFrame
df['dominant_topic'] = lda_output.argmax(axis=1)

# Análise de Citações e outras características
analysis_columns = ['num_citations', 'gsrank', 'pub_year']
topic_stats = df.groupby('dominant_topic')[analysis_columns + ['venue']].agg({
    'num_citations': ['mean', 'median', 'std'],
    'gsrank': ['mean', 'median'],
    'pub_year': ['mean', 'median'],
    'venue': lambda x: x.value_counts().index[0]  # Modo (área mais comum)
})

# Achatando os níveis de coluna multindex
topic_stats.columns = ['_'.join(col).strip() for col in topic_stats.columns.values]

print("Estatísticas por tópico:")
print(topic_stats)

# Teste ANOVA para citações
topic_groups = [group for _, group in df.groupby('dominant_topic')['num_citations']]
f_statistic, p_value = stats.f_oneway(*topic_groups)
print(f"\nResultado do teste ANOVA para citações: F-statistic = {f_statistic}, p-value = {p_value}")

# Extração de Palavras-Chave
def get_top_words(topic_idx, n_words=20):
    topic = lda_model.components_[topic_idx]
    top_words = [(vectorizer.get_feature_names_out()[i], topic[i])
                 for i in topic.argsort()[:-n_words - 1:-1]]
    return dict(top_words)

topic_keywords = {i: get_top_words(i) for i in range(num_topics)}

# TF-IDF para palavras-chave específicas
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words=list(set(stopwords.words('english') + stopwords.words('portuguese') + additional_words)))
tfidf_matrix = tfidf_vectorizer.fit_transform(df['processed_text'])

# Visualização
plt.figure(figsize=(12, 6))
plt.bar(topic_stats.index, topic_stats['num_citations_mean'])
plt.title('Média de Citações por Tópico')
plt.xlabel('Tópico')
plt.ylabel('Média de Citações')
plt.show()

# Nuvem de palavras para o tópico mais citado
most_cited_topic = topic_stats['num_citations_mean'].idxmax()
wordcloud = WordCloud(background_color='white').generate_from_frequencies(topic_keywords[most_cited_topic])
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f'Palavras-chave do Tópico Mais Citado (Tópico {most_cited_topic})')
plt.show()

# Imprimir palavras-chave dos tópicos mais citados
top_3_topics = topic_stats['num_citations_mean'].nlargest(3).index
print("\nPalavras-chave dos 3 tópicos mais citados:")
for topic in top_3_topics:
    print(f"\nTópico {topic}:")
    for word, weight in topic_keywords[topic].items():
        print(f"{word}: {weight:.4f}")

# Análise de correlação
correlation_features = ['num_citations', 'gsrank', 'pub_year']
correlation_matrix = df[correlation_features].corr()
print("\nMatriz de Correlação:")
print(correlation_matrix)

# Modelo de regressão para prever citações
X = df[['gsrank', 'pub_year']]
y = df['num_citations']

# Tratar valores NaN
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Padronizar as features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Criar e treinar o modelo
model = LinearRegression()
model.fit(X_scaled, y)

print("\nCoeficientes do modelo de regressão:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercepto: {model.intercept_:.4f}")

# Análise por área do conhecimento (venue)
venue_stats = df.groupby('venue')['num_citations'].agg(['mean', 'median', 'count'])
venue_stats = venue_stats.sort_values('mean', ascending=False)
print("\nEstatísticas de citações por área do conhecimento:")
print(venue_stats)

# Visualização das top 10 áreas mais citadas
plt.figure(figsize=(12, 6))
venue_stats.head(15)['mean'].plot(kind='bar')
plt.title('Top 10 Áreas do Conhecimento por Média de Citações')
plt.xlabel('Área do Conhecimento')
plt.ylabel('Média de Citações')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""analise
1. Palavras-chave dos tópicos mais citados:

   Tópico 8: relacionado ao sistema de saúde pública, com foco em acesso a medicamentos e assistência farmacêutica.
   Tópico 0: aborda questões judiciais relacionadas a direitos e acesso a medicamentos, com foco geográfico no Rio Grande do Sul e Rio de Janeiro.
   Tópico 6: relacionado a políticas públicas, gestão e justiça, com menção à pandemia de COVID-19.

Os tópicos mais citados parecem girar em torno de questões de saúde pública, acesso a medicamentos e aspectos judiciais relacionados. A pandemia de COVID-19 também aparece como um tema relevante.

2. Matriz de Correlação:

   - Há uma correlação negativa (-0.248) entre número de citações e gsrank, indicando que artigos com melhor ranking no Google Scholar (números mais baixos) tendem a ter mais citações.
   - Existe uma correlação negativa mais forte (-0.316) entre número de citações e ano de publicação, sugerindo que artigos mais antigos tendem a ter mais citações.
   - Há uma correlação positiva (0.279) entre gsrank e ano de publicação, indicando que artigos mais recentes tendem a ter rankings piores no Google Scholar (números mais altos).

3. Coeficientes do modelo de regressão:

   - gsrank: -8.7181 - Isso significa que, em média, para cada ponto de melhora no ranking do Google Scholar, o número de citações aumenta em cerca de 8.7.
   - pub_year: -13.2933 - Em média, para cada ano mais antigo, o artigo tende a ter cerca de 13 citações a mais.
   - Intercepto: 11.9639 - Este é o número base de citações previsto pelo modelo quando as outras variáveis são zero (o que não tem um significado prático neste contexto).

4. Estatísticas de citações por área do conhecimento:

   - As áreas com maior média de citações são "(Syn) thesis" (889 citações), "Tempo social" (711 citações), e uma revista de saúde (395 citações).
   - Há muitas áreas com média de 0 citações, o que pode indicar publicações muito recentes ou áreas de nicho.

1. Os tópicos mais citados estão relacionados a saúde pública, acesso a medicamentos e questões judiciais associadas.
2. Artigos mais antigos e com melhor ranking no Google Scholar tendem a ter mais citações.
3. A área do conhecimento tem um impacto significativo no número de citações, com algumas áreas tendo médias muito mais altas que outras.
4. A pandemia de COVID-19 aparece como um tema relevante nos artigos mais citados, refletindo seu impacto na pesquisa recente.

Recomendações :

1. Foco em pesquisas relacionadas a saúde pública, políticas de acesso a medicamentos e aspectos judiciais da saúde, pois esses temas parecem atrair mais citações.
2. Publicar em revistas de alto impacto para melhorar o ranking no Google Scholar e potencialmente aumentar as citações.
3. Considerar que artigos podem levar tempo para acumular citações, então não desanimar com baixas citações iniciais.
4. Explorar tópicos emergentes (como a resposta à pandemia) que podem atrair interesse e citações.

"""

