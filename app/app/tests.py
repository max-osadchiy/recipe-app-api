from django.test import SimpleTestCase
# from rest_framework.test import APIClient

from app import calc


class CalcTest(SimpleTestCase):
    '''Test the calc module.'''

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)

        self.assertEquals(res, 5)
