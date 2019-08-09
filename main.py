import os
from read_members import get_allyurl, find_players, get_playerinfo
from plot_map import plot_map
from write_members import write_file

path_membertxt = os.path.join(os.path.dirname(__file__), "tabelle_fuer_forum.txt")

if __name__ == "__main__":

    # 112, 332, 383
    url_allies, mode = get_allyurl()

    allies = [find_players(url) for url in url_allies]

    for i in range(len(allies)):

        if len(allies[i]) == 0:

            print("ID {0} fehlerhaft.".format(i))
            allies.remove(i)

        get_playerinfo(allies[i])

    plot_map(allies)
    write_file(path_membertxt, allies, mode)







