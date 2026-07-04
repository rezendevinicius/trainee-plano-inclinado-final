
import numpy as np


def calcular_aceleracao_pela_Fr(v0,massa,angulo,coef_estatico,coef_dinamico,g=9.81):
	P=massa*g
	Py=P*np.cos(angulo)
	Px=P*np.sin(angulo)
	N=Py
	Fr=0
	Fat_max=0
	
	if (v0==0):
		Fat_max=N*coef_estatico
		if (Px>Fat_max):
			Fr=Px-(N*coef_dinamico)
		else:
			Fr=0
	else:
		Fr=Px-(N*coef_dinamico)
	
	return (Fr/massa)
