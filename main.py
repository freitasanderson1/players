from requests import get
from bs4 import BeautifulSoup

url = 'https://www.fifaratings.com/players'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

player_info_containers = html_soup.find_all('span', class_ = 'entry-font')
listNames = list()

for index, item in enumerate(player_info_containers):
  player = item.a.text
  listNames.append(f'{index+1} - {player}')

# print(listNames)
nome = None

while not nome:
  nome = input("Insira o nome de algum jogador:")
  for jogador in listNames:
    if nome in jogador:
      print(f'{nome} está na lista!')
      rank, nomeJogador = jogador.split('-')
      print(f'Foi encontrado o jogador {nomeJogador.strip()} na {rank.strip()}ª posição.')
