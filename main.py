import numpy as np
import physics
import plots
import animation

def main():
    print("Bem-vindo ao simulador de plano inclinado!")
    print("Primeiro, defina as suas variáveis:")
    
    massa = float(input("Digite a massa (kg) do corpo a ser estudado: "))
    v0 = float(input("Digite a velocidade (m/s) inicial desse corpo: "))
    angulo = float(input("Digite o ângulo, em graus, do plano inclinado: "))
    tamanho = float(input("Digite o comprimento, em metro, da rampa: "))
    coef_estatico = float(input("Digite o valor do coeficiente de atrito estático da superfície: "))
    coef_dinamico = float(input("Digite o valor do coeficiente de atrito dinâmico da superfície: "))
    
    while True:
        print("\n" + "="*40)
        print("O que você quer calcular/analisar?")
        print("1- Visualizar gráfico de posição x tempo e animação")
        print("2- Visualizar gráfico de velocidade x tempo e animação")
        print("3- Visualizar a aceleração do sistema")
        print("4- Atribuir novos valores às variáveis")
        print("0- Sair do programa")
        print("="*40)

        opcao = input("Escolha uma opção: ")
        print() # Apenas pula uma linha para organizar o visual
        
        match opcao:
            case "1":
                plots.posicaoxtempo(massa, v0, angulo, tamanho, coef_estatico, coef_dinamico)
                animation.posicaoxtempo(massa, v0, angulo, tamanho, coef_estatico, coef_dinamico)
            case "2":
                plots.velocidadextempo(massa, v0, angulo, tamanho, coef_estatico, coef_dinamico)
                animation.velocidadextempo(massa, v0, angulo, tamanho, coef_estatico, coef_dinamico)
            case "3":
                physics.calcular_aceleracao_pela_Fr(v0, massa, angulo, coef_estatico, coef_dinamico)
            case "4":
                print("--- Atualizando Valores ---")
                massa = float(input("Digite a nova massa (kg): "))
                v0 = float(input("Digite a nova velocidade inicial (m/s): "))
                angulo = float(input("Digite o novo ângulo (graus): "))
                tamanho = float(input("Digite o novo comprimento (m): "))
                coef_estatico = float(input("Digite o novo coef. estático: "))
                coef_dinamico = float(input("Digite o novo coef. dinâmico: "))
            case "0":
                print("Saindo do programa... Até mais!")
                break
            case _:
                print("Opção inválida! Digite um número de 0 a 4.")

if __name__ == '__main__':
    main()