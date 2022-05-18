from numpy import double


cm = double(input("Ingrese su distancia en centimetros: "))
km = cm/100000
m = cm/100
print("Usted ingreso "+str(cm)+" centimetros y estos son "+str(km)+" kilometros o "+str(m)+" metros")