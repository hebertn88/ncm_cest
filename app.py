import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18', verify=False)

soup = BeautifulSoup(resp.content, "html.parser")

table_index = soup.table

table_titles = table_index.find_previous_siblings("p", attrs={"class":"A6-1Subtitulo"}, limit=2)
title, subtitle = [text.get_text() for text in reversed(table_titles)]

print(title)
print(subtitle)