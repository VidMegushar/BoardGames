from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import re
import time

def get_extra_data(game_ref):
    # game_url = f"https://boardgamegeek.com{game_ref}/stats"
    game_url = "https://boardgamegeek.com/boardgame/174430/gloomhaven/stats"
    try:
        session = HTMLSession()
        r = session.get(game_url)
        page = r.html.render()
        print(page)
    except expression as identifier:
        print("Cannot access the page")

    soup = BeautifulSoup(page.text)
    html = list(soup.children)[3]
    # print(list(html.children))
    stats = soup.find_all("div", class_="game-secondary")
    ratings = soup.find("div", class_="col-sm-3 col-sm-push-6")
    # print(stats)
    # print(ratings)
    time.sleep(10)
    return True

for i in range(1,2):
    url = f"https://boardgamegeek.com/browse/boardgame/page/{i}"
    try:
        page = requests.get(url)
    except expression as identifier:
        print("Cannot access the page")

    soup = BeautifulSoup(page.text)

    collection = soup.find("div",id="collection")

    for row in collection.find_all("tr")[1:]:
        bgg_rank = (row.find("td", class_="collection_rank").text).strip()
        game = row.find("td", class_="collection_objectname")
        game_name = game.find("a").text
        print(game_name)
        game_date = (game.find("span").text).strip("()")
        game_page_reference = game.find("a")["href"]
        print(game_page_reference)
        extra_game_info = get_extra_data(game_page_reference)
        rating = row.find_all("td", class_="collection_bggrating")
        geek_rating, avg_rating, num_voters = [(rate.text).strip() for rate in rating]
        #print(bgg_rank, game_name, game_date, geek_rating, avg_rating, num_voters)
        time.sleep(1)

