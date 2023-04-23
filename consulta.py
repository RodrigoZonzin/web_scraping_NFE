import pandas as pd
from bs4 import BeautifulSoup
import os 
import requests

def adiciona_dado(url, loja):

    if os.path.exists('basededados.csv'):
        df = pd.read_csv('basededados.csv'); 
    else:
        df = pd.DataFrame(columns=['produto', 'quantidade_total_itens', 'unidade', 'valor_total', 'estabelecimento'])


    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'table table-striped'})

    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')

        if(cells != []):
            produto = cells[0].text.strip()[0:15].replace('\t', '').replace('\n', ''); 
            quantidade_total_itens = cells[1].text.strip()[20:]; 
            unidade = cells[2].text.strip(); 
            valor_total = cells[3].text.strip()[16:]; 

            todos_os_dados = {'produto': produto,'quantidade_total_itens': quantidade_total_itens, 'unidade': unidade, 'valor_total': valor_total, 'estabelecimento': loja} 

            df = df._append(todos_os_dados, ignore_index = True);

    
    df.to_csv('basededados.csv', index = False)
    return 1;
