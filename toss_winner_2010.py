import csv
from csv import DictReader
from matplotlib import pyplot as plt


def calculate_data(match_data):
    toss_winner_2010 = {}

    for data in match_data:
        if data["date"][:-6] == '2010':
            if data["toss_winner"] not in toss_winner_2010:
                toss_winner_2010[data["toss_winner"]] = 1
            else:
                toss_winner_2010[data["toss_winner"]] += 1

    return toss_winner_2010


def trasfer_to_list(toss_winner_2010):
    toss_winner_name = list(toss_winner_2010.keys())
    toss_winner_count = list(toss_winner_2010.values())

    return toss_winner_name, toss_winner_count


def graph(toss_winner_name, toss_winner_count):
    plt.bar(toss_winner_name, toss_winner_count, color='pink')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    data = open('matches.csv', mode='r')
    match_data = csv.DictReader(data)
    toss_winner_2010 = calculate_data(match_data)
    toss_winner_name, toss_winner_count = trasfer_to_list(toss_winner_2010)
    graph(toss_winner_name, toss_winner_count)
    print(toss_winner_2010)


if __name__ == '__main__':
    main()
