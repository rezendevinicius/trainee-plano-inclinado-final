
import numpy as np
import matplotlib.pyplot as plt
import physics 

def posicaoxtempo(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico):

    # versão comentada abaixo foi substituída pela função em "physics" que já serve para comparar com e sem atrito. Manteve-se o trecho para tornar mais clara a evolução do código
    '''
    angulo_radianos = np.radians(angulo_graus)
    dt = 0.01 
    
    # Pré-alocação
    # 10000 passos de 0.01s representam 100 segundos de simulação
    max_passos = 10000 
    tempos = np.zeros(max_passos)
    posicoes = np.zeros(max_passos)
    velocidades = np.zeros(max_passos)
    
    posicoes[0] = 0.0
    velocidades[0] = v0
    
    i = 0
    
    # A simulação roda enquanto a posição for menor que o tamanho da rampa
    while posicoes[i] < tamanho and i < max_passos - 1:
        
        # se velocidades[i] == 0 (usa atrito estático), se > 0 (usa atrito cinético)
        aceleracao_atual = physics.calcular_aceleracao_pela_Fr(velocidades[i], massa, angulo_radianos, coef_estatico, coef_dinamico)
        
        # Se o bloco está parado (v=0) e a aceleração também deu 0 (atrito estático segurou),
        # quebramos o laço para ele não simular para sempre.
        if velocidades[i] == 0 and aceleracao_atual <= 0:
            print("O bloco não conseguiu vencer o atrito estático e permaneceu parado.")
            break
            
        # Euler-Cromer
        tempos[i + 1] = tempos[i] + dt
        velocidades[i + 1] = velocidades[i] + aceleracao_atual * dt
        posicoes[i + 1] = posicoes[i] + velocidades[i + 1] * dt
        
        i += 1 # Avança para o próximo instante
        
    # Como alocamos 10000 posições, cortamos fora os zeros que sobraram para o gráfico não ficar esquisito
    tempos = tempos[:i+1] # Explicação do Gemini para essa sintaxe nova: A sintaxe [:i+1] no Python é chamada de Slicing (fatiamento). Ela diz ao computador: "Pegue o array original, comece do início e corte tudo o que vier depois da posição i+1".
    posicoes = posicoes[:i+1]
    velocidades = velocidades[:i+1]
    
    # O "Tempo Total" agora é simplesmente o último valor de tempo que foi registrado!
    tempo_total = tempos[-1] # aqui "-1" significa último elemento. Muito diferenbte do meu querido C++
    print(f"Tempo total para percorrer a rampa: {tempo_total:.2f} segundos") # 'f' aqui vem de sring formatada, e o :.2f é para limitar a 2 casas decimais (f -> float)
    
    '''
    
    # Cenário sem atrito
    tempos_sa, posicoes_sa, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, 0, 0)
    
    # Cenário com atrito
    tempos_ca, posicoes_ca, _ = physics.simular_movimento(massa, v0, angulo_graus, tamanho, coef_estatico, coef_dinamico)
    
    plt.figure(figsize=(7, 4))
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
