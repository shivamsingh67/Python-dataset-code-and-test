import unittest
import toss_winner_2010
import csv
from csv import DictReader

file = open('matches.csv', mode='r')

matches_data = DictReader(file)

dict = {'Deccan Chargers': 9, 'Mumbai Indians': 9, 'Delhi Daredevils': 8, 'Kolkata Knight Riders': 7, 'Kings XI Punjab': 5, 'Chennai Super Kings': 10, 'Royal Challengers Bangalore': 6, 'Rajasthan Royals': 6}


class TestTask3(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(toss_winner_2010.calculate_data(matches_data), dict)


if __name__ == '__main__':
    unittest.main()

