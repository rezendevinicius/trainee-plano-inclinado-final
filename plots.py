
import numpy as np
import matplotlib.pyplot as plt
import physics 

def posicaoxtempo(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico):

    
    # Cenário sem atrito
    tempos_sa, posicoes_sa, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, 0, 0) # anulamos o atrito simplemente passando 0 para os coeficientes de atrito
    
    # Cenário com atrito
    tempos_ca, posicoes_ca, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico)
    
    plt.figure(figsize=(7, 4)) # polegadas
    plt.plot(tempos_sa, posicoes_sa, color='blue', label='Sem atrito')
    plt.plot(tempos_ca, posicoes_ca, color='red', label='Com atrito')
    plt.title('Posição x Tempo: Comparação com e sem atrito')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.legend()
    plt.grid(True)
    plt.show()



def velocidadextempo(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico):
    # Cenário sem atrito
    tempos_sa, _, velocidades_sa = physics.simular_movimento(massa, v0, angulo_graus, tamanho, 0, 0)
    
    # Cenário com atrito
    tempos_ca, _, velocidades_ca = physics.simular_movimento(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico)
    
    plt.figure(figsize=(7, 4))
    plt.plot(tempos_sa, velocidades_sa, color='blue', linewidth=2, label='Sem atrito')
    plt.plot(tempos_ca, velocidades_ca, color='green', linewidth=2, label='Com atrito')
    plt.title('Velocidade x Tempo: Comparação com e sem atrito')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()
