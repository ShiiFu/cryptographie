import unittest
from rsa import *

class TestRsa(unittest.TestCase) :
 
	def test_rsa1(self) :
		resultat = rsa(101, 103, 10331, 7)
		self.assertEqual(resultat, 964)
        

if __name__ == '__main__':
	unittest.main()
