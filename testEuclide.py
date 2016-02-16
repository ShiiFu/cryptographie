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
	
	
	def test_restexpmn1(self) :
		resultat = restexpmn(7, 2, 11)
		self.assertEqual(resultat, 5)
	
	def test_restexpmn2(self) :
		resultat = restexpmn(7, 4, 11)
		self.assertEqual(resultat, 3)
	
	def test_restexpmn3(self) :
		resultat = restexpmn(7, 8, 11)
		self.assertEqual(resultat, 9)
	
	def test_restexpmn4(self) :
		resultat = restexpmn(7, 16, 11)
		self.assertEqual(resultat, 4)
	
	def test_restexpmn5(self) :
		resultat = restexpmn(7, 32, 11)
		self.assertEqual(resultat, 5)
	
	def test_restexpmn6(self) :
		resultat = restexpmn(7, 58, 11)
		self.assertEqual(resultat, 9)
	
	def test_restexpmn7(self) :
		resultat = restexpmn(23, 2, 91)
		self.assertEqual(resultat, 74)
	
	def test_restexpmn8(self) :
		resultat = restexpmn(23, 4, 91)
		self.assertEqual(resultat, 16)
	
	def test_restexpmn9(self) :
		resultat = restexpmn(23, 5, 91)
		self.assertEqual(resultat, 4)
	
	def test_restexpmn10(self) :
		resultat = restexpmn(4, 2, 91)
		self.assertEqual(resultat, 16)
	
	def test_restexpmn11(self) :
		resultat = restexpmn(4, 4, 91)
		self.assertEqual(resultat, 74)
	
	def test_restexpmn12(self) :
		resultat = restexpmn(4, 8, 91)
		self.assertEqual(resultat, 16)
	
	def test_restexpmn13(self) :
		resultat = restexpmn(4, 16, 91)
		self.assertEqual(resultat, 74)
	
	def test_restexpmn14(self) :
		resultat = restexpmn(4, 29, 91)
		self.assertEqual(resultat, 23)
        

if __name__ == '__main__':
	unittest.main()
