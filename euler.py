import math

def euler(n) : 
	""" Retourne phi de N """
	n = int(n)
	tab = [0] * (n+1)
	i = 2
	n2 = n
	while i <= n : 
		if n2%i == 0 : 
			tab[i] += 1
			n2 /= i
			i = 1
		i += 1;
	resultat = 1
	for i in range(2, n+1) :
		if tab[i] > 0 :  
			resultat *= math.pow(i, tab[i]) - math.pow(i, tab[i]-1)
	return resultat

if __name__ == '__main__':
	n = 1500
	print n
	print euler(n)
