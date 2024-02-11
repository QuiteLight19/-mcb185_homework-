#Co- Authors: Aman, Ashley
pia = 1
na = 1
signa = -1

for i in range(1, 201, 2):
	pia = pia + signa*(1/(na+2))
	na = na + 2
	signa =-signa
	pib = 3
	nb = 2
	signb = 1
	for j in range(100):
		pib = pib + signb * (4/ ((nb) * (nb+1) * (nb+2)))
		nb = nb + 2
		signb = signb * (-1)
		print(4* pia, pib)
		
		