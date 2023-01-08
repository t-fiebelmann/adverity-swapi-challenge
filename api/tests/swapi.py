import unittest
from .swapi import People

class SwapiTest(unittest.TestCase):
    def __init__(self):
        self.people = People()

    def test_get_all(self):
        people = self.people.get_all()
        self.assertEquals(people.count(), 87)
    
    def test_get_one(self):
        people = self.people.get_one()
        self.assertEquals(people.count(), 1)