import math

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

def restexpmn(x, p, n) : 
	""" Retourne le reste de x^p modulo n """
	resultat = p
	compteur = 1
	i = 1
	while resultat != 1 : 
		resultat = resultat / 2
		compteur = compteur * 2
		i = i + 1
	resultat = [0] * (i)
	for j in range(0, i+1) : 
		if p > 0 and compteur <= p : 
			resultat[(i-j)-1] = 1
			p = p - compteur
		compteur = compteur / 2
	final = x%n
	r = 1
	for j in range(0, i) : 
		if j>0 : 
			final = (final*final) % n
		if resultat[j] == 1 : 
			r = (r * final) % n
	return r
		
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
	
	print "### Reste de x^p modulo n ###"
	x = 7
	p = 4
	n = 11
	r = restexpmn(x, p, n)
	print "x=" + str(x) + ", p=" + str(p) + ", n=" + str(n)
	print "r=" + str(r)
