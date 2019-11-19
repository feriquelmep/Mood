import unittest
from prueba import probar

class TestProbar(unittest.TestCase):
    def test_sumar(self):
        self.assertAlmostEqual(probar(3,5),8)
        self.assertAlmostEqual(probar(3,0),3)
        self.assertAlmostEqual(probar(3,1),3)