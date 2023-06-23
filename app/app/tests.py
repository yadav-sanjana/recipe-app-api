"""
Sample of testcase
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_number(self):
        res = calc.add(5, 6)
 
        self.assertEqual(res, 11)

    def test_sub_number(self):
        res = calc.sub(7, 6)

        self.assertEqual(res, 1)
