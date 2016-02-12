import unittest
from euclide import *

class TestEuclide(unittest.TestCase) :
 
	def test_euclide1(self) :
		resultat = euclide(26, 15)
		self.assertEqual(resultat, (-4, 7))
	
	def test_euclide2(self) :
		resultat = euclide(15, 26)
		self.assertEqual(resultat, None)
	
	
	def test_inverse1(self) :
		resultat = inverse(15, 26)
		self.assertEqual(resultat, 7)
	
	def test_inverse2(self) :
		resultat = inverse(51, 242)
		self.assertEqual(resultat, 19)
        

if __name__ == '__main__':
	unittest.main()
