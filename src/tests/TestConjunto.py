import unittest
from.src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    deff test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto ([])
        self.assertEqual(conjunto.promedio())