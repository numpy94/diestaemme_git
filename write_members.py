def write_file(path, allies, mode):

    with open(path, "w", encoding="utf-8") as file:

        ally_names = [allies[i][0]["ally"] for i in range(len(allies))]

        for i in range(0, len(allies)):

            file.write("[size=12]Stamm: [ally]" + str(ally_names[i]) + "[/ally][/size]")

            if mode == "y":

                file.write("[table]\n[**]Spieler[||]Punkte[||]Dörfer[||]Mindest-Def[/**]\n")

            else:

                file.write("[table]\n[**]Spieler[||]Punkte[||]Dörfer[/**]\n")

            for j in range(0, len(allies[i])):

                player = allies[i][j]

                villages = [player["villages"][i][0] for i in range(0, len(player["villages"]))]
                villages = ["[coord]" + str(villages[j]) + "[/coord]" for j in range(0, len(villages))]
                villages = "\n".join(villages)

                if mode == "y":
                    file.write("[*][player]" + str(player["name"]) + "[/player][|]" + str(player["points"])
                               + "[|]" + villages + "[|]" + str(round(player["points"] * 0.15, 0)) + "\n")

                else:

                    file.write("[*][player]" + str(player["name"]) + "[/player][|]" + str(player["points"])
                               + "[|]" + villages + "\n")

            file.write("[/table]\n")
            file.write("------------------------------------------------------------\n")
