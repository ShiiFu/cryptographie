import unittest
from euler import *


class TestEuler(unittest.TestCase) :
 
	def test_euler1(self) :
		resultat = euler(1500)
		self.assertEqual(resultat, 400)
		
	def test_euler2(self) :
		resultat = euler(120)
		self.assertEqual(resultat, 32)
		
	def test_euler3(self) :
		resultat = euler(1000)
		self.assertEqual(resultat, 400)
		
	def test_euler4(self) :
		resultat = euler(59)
		self.assertEqual(resultat, 58)
	
	def test_euler5(self) :
		resultat = euler(euler(1500))
		self.assertEqual(resultat, 160)
        


if __name__ == '__main__':
	unittest.main()
