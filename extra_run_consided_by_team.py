import csv
from csv import DictReader
from matplotlib import pyplot as plt


def calculate(deliveries_data):

    extra_run_consided_by_team = {}

    for data in deliveries_data:
        if data["bowling_team"] not in extra_run_consided_by_team:
            extra_run_consided_by_team[data["bowling_team"]
                                       ] = data["extra_runs"]
        else:
            extra_run_consided_by_team[data["bowling_team"]
                                       ] += data["extra_runs"]
    return extra_run_consided_by_team


def transfer(extra_run):
    team_name = list(extra_run.keys())
    extra_run = list(extra_run.values())

    return team_name, extra_run


def graph(extra_run, team_name):
    plt.bar(team_name, extra_run, color='pink')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    data = open('deliveries.csv', mode='r')

    deliveries_data = csv.DictReader(data)

    extra_run_data = calculate(deliveries_data)
    team_name, extra_run = transfer(extra_run_data)
    graph(extra_run, team_name)
    


if __name__ == '__main__':
    main()
