import os
import numpy as np
import matplotlib.pyplot as plt


def plot_map(allies):

    ally_names = [allies[i][0]["ally"] for i in range(len(allies))]

    x_coords = []
    y_coords = []

    for p in range(len(allies)):

        ally = allies[p]

        villages = []
        villages_x = []
        villages_y = []

        for player in ally:

            temp_villages = [player["villages"][k][0] for k in range(len(player["villages"]))]

            for j in range(len(temp_villages)):

                villages.append(temp_villages[j])

        for i in range(0, len(villages)):

            data = villages[i].split("|")

            villages_x.append(int(data[0]))
            villages_y.append(int(data[1]))

        x_coords.append(villages_x)
        y_coords.append(villages_y)

    fig = plt.figure(figsize=(8.5, 7.5))
    ax = fig.add_subplot(111)
    plt.grid(True, linestyle="-.", color="grey")

    max_x = 0
    max_y = 0

    min_x = 1000
    min_y = 1000

    for i in range(0, len(x_coords)):

        ax.scatter(x_coords[i], y_coords[i], marker="o", label=ally_names[i])

        if np.max(x_coords[i]) > max_x:

            max_x = np.max(x_coords[i])

        if np.max(y_coords[i]) > max_y:

            max_y = np.max(y_coords[i])

        if np.min(x_coords[i]) < min_x:

            min_x = np.min(x_coords[i])

        if np.min(y_coords[i]) < min_y:

            min_y = np.min(y_coords[i])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    x_range = max_x - min_x
    y_range = max_y - min_y

    ax.arrow(min_x - 0.05*x_range, min_y - 0.05*y_range, 0, 10, color="red", width=0.3)

    ax.set_xlim(min_x - 0.1*x_range, max_x + 0.1*x_range)
    ax.set_ylim(min_y - 0.1*y_range, max_y + 0.1*y_range)
    ax.set_facecolor('lightgreen')

    plt.title("Roter Pfeil entspricht den Laufzeiten:\n" +
              "Speer / Schwert / Axt / Bogen: 03:00:00 / 03:40:00 / 03:00:00 / 03:00:00\n" +
              "Späher /LKav / BerBog / SKav: 01:30:00 / 01:40:00 / 01:40:00 / 01:50:00\nRamme / Kata / AG: 04:60:00 / 04:60:00 / 05:50:00", loc="left")
    plt.legend()
    plt.savefig(os.path.join(os.path.dirname(__file__), "karte.png"))
    plt.show()
