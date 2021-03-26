import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.ss.lv/lv/transport/cars/today-5/sell/'
LAPAS = 'lapas/'


def saglaba(url, datne):
    rezultats = requests.get(url)
    if rezultats.status_code == 200:
        with open(datne, 'w', encoding='UTF-8') as f:
            f.write(rezultats.text)

# saglaba(URL, LAPAS + "pirma_lapa.html")

def info(datne):
    dati = []

    with open(datne, 'r', encoding="UTF-8") as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    galvena = zupa.find(id = 'page_main')

    tabulas = galvena.find_all("table")

    # for tabula in tabulas:
    #     print(tabula)
    #     print("===================================")
    #     print("===================================")
    #     print("===================================")

    auto_tabula = tabulas[2]

    rindas = auto_tabula.find_all("tr")

    for rinda in rindas[1:]:
        lauki = rinda.find_all("td")
        # for lauks in lauki:
        #     print(lauks)
        #     print("===================================")

        auto = {}

        auto["saite"] = lauki[1].find("a")["href"]
        auto["bilde"] = lauki[1].find("img")["src"]
        auto["apraksts"] = lauki[2].find("a").text.replace("\n", " ")

        marka = lauki[3].text

        print(marka)
        
        # print(auto)
        exit()








info(LAPAS + "pirma_lapa.html")