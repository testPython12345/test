'''
import unittest
import pytest
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")    
    return a/b
class Test(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10,2), 5.0)
        self.assertRaises(ValueError, divide, 10, 0) 
if __name__ == "__main__":
    unittest.main()

add = lambda a, b: a+b
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
'''

"""
basic - 5% скидка
silver - 10% скидка
gold - 15% скидка
"""

def calc_discont(price, level):
    if level == 'basic':
        return price * 0.95
    elif level == 'silver':
        return price * 0.90
    elif level == 'gold':
        return price * 0.85
    else:
        raise ValueError("Unknown level!")

def test_calc_discont():
    assert calc_discont(10000, 'silver') == 9000
    assert calc_discont(10000, 'basic') == 9500
    assert calc_discont(10000, 'gold') == 8500
