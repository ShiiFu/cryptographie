def vernam(mot, cle) : 
	""" Chiffre un mot avec une cle avec la methode Vernam """
	resultat = [0] * len(mot)
	for i in range(len(mot)) : 
		resultat[i] = ( mot[i] + cle[i%len(cle)] ) % 2
	return resultat

if __name__ == '__main__':
	mot = [1,0,0,1,0,0,1,1,1,0,0]
	cle = [1,1,0]
	print mot
	print vernam(mot, cle)
