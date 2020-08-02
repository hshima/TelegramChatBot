import re
import requests
import datetime
import json

from bs4 import BeautifulSoup


def main():
    #Finds link for the current dica da semana
    res = requests.get("http://www.ceagesp.gov.br/entrepostos/servicos/dicas-da-semana/" + str(datetime.datetime.now().year))
    res.encoding = 'utf-8'
    soup_year = BeautifulSoup(res.text, 'html.parser')
    pattern = "(?<='href',')(.*)-estao-mais-em-conta-(.*)(?=')"
    link_dica_semana = None
    if match := re.search(pattern, str(soup_year), re.IGNORECASE):
        link_dica_semana = match.group(0)

    #Finds the content in the page found
    res = requests.get(link_dica_semana)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser', multi_valued_attributes=None)
    baixa = soup.find_all("div", class_ = "box-preco-bea b")
    igual = soup.find_all("div", class_ = "box-preco-bea e")
    alta = soup.find_all("div", class_ = "box-preco-bea a")

    subiu = alta[0].text
    desceu = baixa[0].text
    igual = igual[0].text

    return {'subiu': subiu,'desceu': desceu, "igual": igual}

def subiu():
    return main()['subiu']

def desceu():
    return main()['desceu']

def igual():
    return main()['igual']

def test():
    pass

'''
if __name__ == "__main__":
    subiu()
'''