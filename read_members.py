import sys
import requests
import numpy as np
from bs4 import BeautifulSoup

url_player = "https://de168.die-staemme.de/guest.php?screen=info_player&id="


def get_allyurl():

    url = []
    prefix = "https://de168.die-staemme.de/guest.php?screen=info_member&id="
    counter = 0

    try:

        counter = int(input("Bitte gebe die Anzahl an zu suchenden Stämmen ein: "))
        mode = input("Mindest-Def anzeigen? [y / n]: ")

        if mode != "y" and mode != "n":

            raise ValueError

    except ValueError:

        print("Bitte eine ganze Zahl, bzw. 'y' oder 'n' eingeben.")
        sys.exit()

    for i in range(0, counter):

        try:

            id = int(input(("Bitte gib die Stammes-ID des {0}. Stammes ein: ").format(i + 1)))
            url.append(prefix + str(id))

        except ValueError:

            print("Die ID kann nur aus Zahlen bestehen.")
            sys.exit()

    return url, mode


def find_players(ally):

    html_code = requests.get(ally).text
    soup = BeautifulSoup(html_code, "html.parser")

    members = []

    ally_name = ""

    for name in soup.findAll("table", {"id": "content_value"}):

        content = name.text.split()

        try:

            index = content.index("Mitglieder")

        except ValueError:

            print("ID {0} fehlerhaft.".format(ally))
            sys.exit()

        ally_name = content[index + 1]

    for link in soup.find_all('a'):

        href = "/guest.php?screen=info_player&id"

        if href in link.get('href'):

            member = {}
            name = link.contents[0]
            href_txt = str(link)
            member["ally"] = ally_name
            member["name"] = name
            member["id"] = int(href_txt.split('"')[1].split("=")[2])
            members.append(member)

    return members


def get_playerinfo(members):

    for player in members:

        html_code = requests.get(url_player + str(player["id"])).text
        soup = BeautifulSoup(html_code, "html.parser")

        for link in soup.find_all(id="villages_list"):

            villages = []
            points = []

            content = link.text.split()

            for i in range(0, len(content)):

                if "|" in content[i] and len(content[i]) == 7:

                    villages.append(content[i])
                    points.append(content[i+1])

            player["villages"] = [(villages[i], points[i]) for i in range(0, len(villages))]

        points = np.sum([int(player["villages"][i][1].replace(".", "")) for i in range(len(player["villages"]))])

        player["points"] = points
