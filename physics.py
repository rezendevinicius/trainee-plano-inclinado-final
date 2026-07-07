
import numpy as np

def calcular_aceleracao_pela_Fr(v0, massa, angulo, coef_estatico, coef_dinamico, g=9.81):
    P = massa * g
    Py = P * np.cos(angulo)
    Px = P * np.sin(angulo)
    N = Py
    Fr = 0
    Fat_max = 0
    
    if (v0 == 0):
        Fat_max = N * coef_estatico
        if (Px > Fat_max):
            Fr = Px - (N * coef_dinamico)
        else:
            Fr = 0
    else:
        Fr = Px - (N * coef_dinamico)
    
    return (Fr / massa)


def simular_movimento(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico, dt=0.01, max_passos=10000):
    angulo_radianos = np.radians(angulo_graus)
    
    tempos = np.zeros(max_passos)
    posicoes = np.zeros(max_passos)
    velocidades = np.zeros(max_passos)
    velocidades[0] = v0
    
    i = 0
    while posicoes[i] < tamanho and i < max_passos - 1:
        a = calcular_aceleracao_pela_Fr(velocidades[i], massa, angulo_radianos, coef_estatico, coef_dinamico)
        
        if velocidades[i] == 0 and a <= 0:
            break
        
        tempos[i + 1] = tempos[i] + dt
        velocidades[i + 1] = velocidades[i] + a * dt
        posicoes[i + 1] = posicoes[i] + velocidades[i + 1] * dt
        i += 1
    
    return tempos[:i+1], posicoes[:i+1], velocidades[:i+1]