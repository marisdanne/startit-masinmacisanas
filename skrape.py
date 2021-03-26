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

    for rinda in rindas[1:-1]:
        lauki = rinda.find_all("td")
        # for lauks in lauki:
        #     print(lauks)
        #     print("===================================")

        auto = {}

        auto["saite"] = lauki[1].find("a")["href"]
        auto["bilde"] = lauki[1].find("img")["src"]
        auto["apraksts"] = lauki[2].find("a").text.replace("\n", " ")

        lauki[3].br.replace_with('!')

        auto["marka"] = lauki[3].text.replace("!", " ")
        auto["razotajs"] = lauki[3].text.split("!")[0]
        auto["modelis"] = lauki[3].text.split("!")[1]
        auto["gads"] = lauki[4].text

        tilpums = lauki[5].text

        if tilpums[-1] == "D":
            auto["dzinejs"] = "Dīzelis"
            auto["tilpums"] = tilpums[:-1]
        elif tilpums[-1] == "H":
            auto["dzinejs"] = "Hibrīds"
            auto["tilpums"] = tilpums[:-1]            
        else:
            auto["dzinejs"] = "Benzīns"
            auto["tilpums"] = tilpums            
        
        if not lauki[6].text == "-":
            auto["nobraukums"] = lauki[6].text.replace(" tūkst.", "")
        else:
            continue
            # alternatīva auto["nobraukums"] = ""

        auto["cena"] = lauki[7].text.replace("  €", "").replace(",", "")

        dati.append(auto)

    return dati


d1 = info(LAPAS + "pirma_lapa.html")
print(d1)