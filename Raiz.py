import math
a=float(input("digite a:   "))
b=float(input("digite b:   "))
c=float(input("digite c:   "))


delta= b **2 - 4*a*c

if delta ==0:
	raiz1=(-b + math.sqrt(delta))/(2*a)
	print("a única raiz é:" , raiz1)
else:
	if delta < 0:
		print("não existe raiz")
	else:
		raiz1=(-b + math.sqrt(delta))/(2*a)
		raiz2=(-b - math.sqrt(delta))/(2*a)

		print("a primeira raiz é:" , raiz1)
		print("a segunda raiz é :",raiz2)




