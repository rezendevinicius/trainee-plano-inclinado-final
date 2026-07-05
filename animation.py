import numpy as np
import matplotlib.pyplot as plt
import physics

def animacao(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico):
    angulo_radianos = np.radians(angulo_graus)
    dt = 0.01 
    max_passos = 10000 
    

    posicoes = np.zeros(max_passos)
    velocidades = np.zeros(max_passos)
    velocidades[0] = v0
    
    i = 0
    while posicoes[i] < tamanho and i < max_passos - 1:
        a = physics.calcular_aceleracao_pela_Fr(velocidades[i], massa, angulo_radianos, coef_estatico, coef_dinamico)
        
        if velocidades[i] == 0 and a <= 0:
            print("O bloco permaneceu em repouso.")
            break
            
        velocidades[i + 1] = velocidades[i] + a * dt
        posicoes[i + 1] = posicoes[i] + velocidades[i + 1] * dt
        i += 1
        
    posicoes = posicoes[:i+1] 
    
    # ==========================================
    # Parte da animação
    # ==========================================
    altura_inicial = tamanho * np.sin(angulo_radianos)
    base_final = tamanho * np.cos(angulo_radianos)
    
    plt.figure(figsize=(8, 5))
    
    # Desenhamos 1 frame a cada 5 passos de cálculo para a animação não ficar muito lenta -- recomendação do Gemini
    salto = 5 
    
    for frame in range(0, len(posicoes), salto):
        #Limpa o gráfico anterior
        plt.cla() #Por que no Python é tudo resumido? Poderia ser clear, mas é "cla"...
        
        # Desenha a rampa de novo 
        plt.plot([0, base_final], [altura_inicial, 0], color='black', linewidth=4)
        plt.plot([0, base_final], [0, 0], color='gray', linestyle='--')
        plt.plot([0, 0], [0, altura_inicial], color='gray', linestyle='--')
        
        #Calcula onde o bloco está e desenha
        distancia = posicoes[frame]
        x_atual = distancia * np.cos(angulo_radianos)
        y_atual = altura_inicial - (distancia * np.sin(angulo_radianos))
        
        # 'rs' = red square (quadrado vermelho)
        plt.plot(x_atual, y_atual, 'rs', markersize=15) 
        
        # 4. Mantêm as proporções da janela fixas para não tremer a animação
        plt.xlim(-0.5, base_final + 0.5)
        plt.ylim(-0.5, altura_inicial + 0.5)
        plt.title(f'Animação Simples: Tempo = {frame * dt:.2f} s')
        
        #Pausa o código por 0.01 segundos para criar o movimento
        plt.pause(0.01)
        
    plt.show()