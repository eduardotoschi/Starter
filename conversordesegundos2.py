a=input("Por favor, entre com o número de segundos que deseja converter:")

b=(float(a))
c=b//86400
g=b%86400
d=g//3600
h=g%3600
e=h//60
f=h%60


print(c,"dias, ",d,"horas,", e,"minutos e ",f,"segundos.")


