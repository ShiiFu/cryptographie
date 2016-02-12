def euclide(a, b) : 
	if a < b or b < 1 : 
		return None
	r = a%b
	q = (a-r)/b
	if r == 1 : 
		return r, -q
	else : 
		y, x = euclide(b, r)
		y = y - (q * x)
		return x, y

def inverse(n, m) : 
	""" Retourne l'inverse de n modulo m """
	x, y = euclide(m, n)
	return y
		
if __name__ == '__main__':
	print "### Algorithme d'Euclide ###"
	a = 26
	b = 15
	x, y = euclide(a, b)
	print "a=" + str(a) + ", b=" + str(b)
	print "x=" + str(x) + ", y=" + str(y)
	
	print "### Inversion de n modulo m ###"
	n = 51
	m = 242
	y = inverse(n, m)
	print "y=" + str(y)
