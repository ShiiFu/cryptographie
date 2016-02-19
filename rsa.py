from euler import *
from euclide import *

def rsa(n, p, M, e) : 
	""" Crypte le message par le RSA avec les parametres n, p et e """
	N = n * p
	#print "N : " + str(N)
	phiN = euler(N)
	#print "phiN : " + str(phiN)
	d = inverse(e, phiN)
	#d = d + phiN
	#print "d : " + str(d)
	M2 = restexpmn(M, e, N)
	return M2


if __name__ == '__main__':
	print rsa(101, 103, 10331, 7)
	#print rsa(7, 13, 23, 5)
