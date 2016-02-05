import unittest
from vernam import *


class TestVernam(unittest.TestCase) :
 
	def test_vernam1(self) :
		mot = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
		cle = [1, 1, 0]
		resultat = vernam(mot, cle)
		self.assertEqual(resultat, [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1])
        
	def test_vernam2(self) :
		mot = [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]
		cle = [1, 1, 0]
		resultat = vernam(mot, cle)
		self.assertEqual(resultat, [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0])
	
	def test_vernam3(self) :
		mot = [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1]
		cle = [1, 1, 0]
		resultat = vernam(vernam(mot, cle), cle)
		self.assertEqual(resultat, mot)


if __name__ == '__main__':
	unittest.main()
