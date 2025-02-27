"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app

# we need to import the file that contains the status codes
from src import status

class CounterTest(TestCase):
    def setUp(self):
      self.client = app.test_client()

    """Counter tests"""
    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_updating_a_counter(self):
        """It should increment a counter"""
        update = self.client.post('/counters/qux')
        self.assertEqual(update.status_code, status.HTTP_201_CREATED)
        baseline = update.json["qux"]
        self.assertEqual(baseline, 0)
        update = self.client.put('/counters/qux')
        self.assertEqual(update.status_code, status.HTTP_200_OK)
        self.assertEqual(update.json["qux"], baseline+1)

    def test_deleting_a_counter(self):
        """It should delete the counter"""
        result = self.client.post('/counters/tux')
        result = self.client.delete('/counters/tux')
        self.assertEqual(result.status_code, status.HTTP_200_OK)