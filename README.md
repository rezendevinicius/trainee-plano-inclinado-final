## Projeto desenvolvido para o processo trainee do núcleo de estudos sobre física computacional, Nexus, da Ufla.

## Tema: 
Plano inclinado, focado na compreensão da ação das forças envolvidas e nas bibliotecas numpy e matplotlib para traduzir os fenômenos físicos.

## Estrutura do projeto: 


```
projeto-trainee-final/
├── main.py          # Interface de linha de comando (menu interativo)
├── physics.py        # Modelo físico e motor de simulação numérica
├── plots.py           # Geração dos gráficos (posição x tempo, velocidade x tempo)
├── animation.py    # Animação comparando cenários com/sem atrito
├── requirements.txt
└── README.md
```

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/rezendevinicius/trainee-plano-inclinado-final.git
cd trainee-plano-inclinado-final
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python main.py
```

## Como usar

Ao iniciar, o programa solicita:
- Massa do bloco (kg)
- Velocidade inicial (m/s)
- Ângulo da rampa (graus)
- Comprimento da rampa (m)
- Coeficientes de atrito estático e dinâmico

Em seguida, um menu permite:
1. Comparar posição x tempo (com/sem atrito) e ver animação
2. Comparar velocidade x tempo (com/sem atrito) e ver animação
3. Calcular a aceleração inicial do sistema
4. Redefinir os valores das variáveis
0. Sair do programa

## Autor

Vinícius Rezende — Ciência da Computação, UFLA