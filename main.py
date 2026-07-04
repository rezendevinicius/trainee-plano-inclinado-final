
import numpy as np
import physics
import plots
import animation

def main():
	# Mensagens iniciais
	
	print("Bem-vindo ao simulador de plano inclinado!")
	print("Primeiro, defina as suas variáveis:")
	
	# declaração das principais variáveis
	
	massa=input("Digite a massa (kg) do corpo a ser estudado")
	v0=input("Digite a velocidade (m/s) inicial desse corpo")
	angulo=input("Digite o ângulo, em graus, do plano inclinado")
	tamanho=input("Digite o comprimento, em metro, da rampa")
	coef_estatico=input("Digite o valor do coeficiente de atrito estático da superfície")
	coef_dinamico=input("Digite o valor do coeficiente de atrito dinâmico da superfície")
	
	# Escolha das funcionalidades
	
	print("O que você quer calcular/analisar?")
	print("1- Visualizar gráfico de posição x tempo e animação")
	print("2- Visualizar gráfico de velocidade x tempo e animação")
	print("3- Visualizar a aceleração do sistema, dados o ângulo da rampa e os coeficientes de atrito")
	print("4- Atribuir novos valores às variáveis")
	print("0- Sair do programa")

	while(true)
	opcao=input()
	
	# Realização das variáveis
	
	match (opcao):
	
	case 1:
		posicaoxtempo(massa,v0,angulo,tamanho,coef_estatico,coef_dinamico)
		break
	case 2:
		velocidadextempo(massa,v0,angulo,tamanho,coef_estatico,coef_dinamico)
		break
	case 3:
		aceleracao(massa,v0,angulo,tamanho,coef_estatico,coef_dinamico)
		break
	case 4:
		massa=input("Digite a massa (kg) do corpo a ser estudado")
		v0=input("Digite a velocidade (m/s) inicial desse corpo")
		angulo=input("Digite o ângulo, em graus, do plano inclinado")
		tamanho=input("Digite o comprimento, em metro, da rampa")
		coef_estatico=input("Digite o valor do coeficiente de atrito estático da superfície")
		coef_dinamico=input("Digite o valor do coeficiente de atrito dinâmico da superfície")
		break
	case 0:
		print("Saindo do programa...")
		return 0


if __name__ == '__main__':
	main()