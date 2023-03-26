import csv
from csv import DictReader
from matplotlib import pyplot as plt


def calculation(deliveries_data):
    most_run = {}

    for data in deliveries_data:
        if data["batsman"] not in most_run:
            most_run[data["batsman"]] = int(data["batsman_runs"])
        else:
            most_run[data["batsman"]] += int(data["batsman_runs"])

    most_run_data = sorted(most_run.items(), key=lambda x: x[1], reverse=1)

    return most_run_data


def transfer(most_run):
    batsman_name = []
    batsman_run = []
    for data in range(0, 20):
        batsman_name.append(most_run[data][0])
        batsman_run.append(most_run[data][1])

    return batsman_name, batsman_run


def graph(batsman_name, batsman_run):
    plt.bar(batsman_name, batsman_run, color='orange')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    data = open('deliveries.csv', mode='r')
    deliveries_data = csv.DictReader(data)

    most_run = calculation(deliveries_data)
    batsman_name, batsman_run = transfer(most_run)
    graph(batsman_name, batsman_run)
    # print(transfer(most_run))
    print(most_run)


if __name__ == '__main__':
    main()
