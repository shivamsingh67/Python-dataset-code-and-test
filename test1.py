import unittest
import Question1
import csv
from csv import DictReader

file = open('matches.csv', mode='r')

match_data = DictReader(file)

dict = {'Kolkata Knight Riders': 6, 'Chennai Super Kings': 9, 'Delhi Daredevils': 7, 'Royal Challengers Bangalore': 4, 'Rajasthan Royals': 13, 'Kings XI Punjab': 10, 'Deccan Chargers': 2, 'Mumbai Indians': 7}
dict1 = {'Kolkata Knight Riders': 6, 'Chennai Super Kings': 9, 'Delhi Daredevils': 7, 'Royal Challengers Bangalore': 4, 'Rajasthan Royals': 13, 'Kings XI Punjab': 10, 'Deccan Chargers': 2, 'Mumbai Indians': 22}

class TestTask1(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(Question1.match_played_in_2008(match_data), dict)


if __name__ == '__main__':
    unittest.main()