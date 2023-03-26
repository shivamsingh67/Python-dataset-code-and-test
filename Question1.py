import csv
from csv import DictReader
from matplotlib import pyplot as plt


def match_played_in_2008(match_data):
    match_played_data = {}

    for data in match_data:
        if data["date"][:-6] == '2008':
            if data["winner"] not in match_played_data:
                match_played_data[data["winner"]] = 1
            else:
                match_played_data[data["winner"]] += 1

    return match_played_data


def transfer(winner_2008_data):
    winner_team = list(winner_2008_data.keys())
    winner_count = list(winner_2008_data.values())

    return winner_team, winner_count


def graph(winner_team, winner_count):
    plt.bar(winner_team, winner_count, color='pink')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    read_data = open('matches.csv', mode='r')
    match_data = csv.DictReader(read_data)

    winner_2008_data = match_played_in_2008(match_data)
    print(winner_2008_data)
    winner_team, winner_count = transfer(winner_2008_data)
    graph(winner_team, winner_count)


if __name__ == '__main__':
    main()
