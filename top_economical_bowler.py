import csv
from csv import DictReader
from matplotlib import pyplot as plt


def calculation(deliveries_data):
    top_eco_bowler = {}

    for data in deliveries_data:
        if data["bowler"] not in top_eco_bowler:
            top_eco_bowler[data["bowler"]] = int(
                data["total_runs"]) / int(data["ball"])
        else:
            top_eco_bowler[data["bowler"]
                           ] += int(data["total_runs"]) / int(data["ball"])

    top_eco_bowler_data = sorted(
        top_eco_bowler.items(), key=lambda x: x[1], reverse=0)
    return top_eco_bowler_data


def tarnsfer(top_eco_bow):
    bowler_name = []
    bowler_run = []
    for data in range(0, 10):
        bowler_name.append(top_eco_bow[data][0])
        bowler_run.append(top_eco_bow[data][1])

    return bowler_name, bowler_run


def graph(bowler_name, economy):
    plt.bar(bowler_name, economy, color='pink')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    data = open('deliveries.csv', mode='r')
    deliveries_data = csv.DictReader(data)

    top_eco_bow = calculation(deliveries_data)

    print(top_eco_bow)

    bowler_name, economy = tarnsfer(top_eco_bow)

    graph(bowler_name, economy)


if __name__ == '__main__':
    main()
