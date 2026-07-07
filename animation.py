import numpy as np
import matplotlib.pyplot as plt
import physics

def animacao(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico):
    angulo_radianos = np.radians(angulo_graus)
    
    _, posicoes_sa, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, 0, 0)
    _, posicoes_ca, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico)
    
    # Os dois vetores podem ter tamanhos diferentes (quando um bloco chega antes do outro)
    n_frames = max(len(posicoes_sa), len(posicoes_ca))
    
    altura_inicial = tamanho * np.sin(angulo_radianos)
    base_final = tamanho * np.cos(angulo_radianos)
    
    plt.figure(figsize=(8, 5))
    salto = 5 # para pular frames desnecessários e "acelerar" a animação
    dt = 0.01
    
    for frame in range(0, n_frames, salto):
        plt.cla() # apaga para redesenhar atualizado 
        
        # Desenha a rampa
        plt.plot([0, base_final], [altura_inicial, 0], color='black', linewidth=4)
        plt.plot([0, base_final], [0, 0], color='gray', linestyle='--')
        plt.plot([0, 0], [0, altura_inicial], color='gray', linestyle='--')
        
        # Índice "travado" no último frame válido, caso um bloco já tenha chegado ao fim
        idx_sa = min(frame, len(posicoes_sa) - 1)
        idx_ca = min(frame, len(posicoes_ca) - 1)
        
        distancia_sa = posicoes_sa[idx_sa]
        distancia_ca = posicoes_ca[idx_ca]
        
        x_sa = distancia_sa * np.cos(angulo_radianos)
        y_sa = altura_inicial - (distancia_sa * np.sin(angulo_radianos))
        
        x_ca = distancia_ca * np.cos(angulo_radianos)
        y_ca = altura_inicial - (distancia_ca * np.sin(angulo_radianos))
        
        # 'bs' = blue square (sem atrito), 'rs' = red square (com atrito)
        plt.plot(x_sa, y_sa, 'bs', markersize=15, label='Sem atrito')
        plt.plot(x_ca, y_ca, 'rs', markersize=15, label='Com atrito')
        
        plt.xlim(-0.5, base_final + 0.5)
        plt.ylim(-0.5, altura_inicial + 0.5)
        plt.legend(loc='upper right')
        plt.title(f'Comparação com e sem atrito: Tempo = {frame * dt:.2f} s')
        
        plt.pause(0.01)
        
    plt.show()