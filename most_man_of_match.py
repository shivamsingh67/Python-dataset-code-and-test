import csv
from csv import DictReader
from matplotlib import pyplot as plt


def calculation(match_data):
    most_player_of_the_match = {}

    for data in match_data:
        if data["date"][:-6] == '2012':
            if data["player_of_match"] not in most_player_of_the_match:
                most_player_of_the_match[data["player_of_match"]] = 1
            else:
                most_player_of_the_match[data["player_of_match"]] += 1

    return most_player_of_the_match


def transfer(mostplayer_of_the_match):
    player_name = list(mostplayer_of_the_match.keys())
    player_of_the_match_count = list(mostplayer_of_the_match.values())

    return player_name, player_of_the_match_count


def graph(player_name, player_of_the_match_count):
    plt.bar(player_name, player_of_the_match_count, color='pink')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    data = open('matches.csv', mode='r')
    match_data = csv.DictReader(data)

    mostplayer_of_the_match = calculation(match_data)
    player_name, player_of_the_match_count = transfer(mostplayer_of_the_match)

    graph(player_name, player_of_the_match_count)


if __name__ == '__main__':
    main()
