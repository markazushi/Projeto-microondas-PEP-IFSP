# Projeto-microondas-PEP-IFSP

Este projeto foi desenvolvido por alunos do curso de Bacharelado em Engenharia Eletrica do IFSP-PEP (Instituto Federal de Ciência e Tecnologia de São Paulo - Campus - Presidente Epitácio) e tem como objetivo realizar cálculos relacionados a ondas em linhas de transmissão de micro-ondas. A aplicação foi construída utilizando Python e as bibliotecas _CustomTkinter_ e _PyQt6_ para as interfaces gráficas, além das biblioteca _NumPy_ e _MatPlotLib_ para os cálculos e gráficos do back-end.

## Funcionalidades

- Entrada de parâmetros elétricos e físicos da linha de transmissão.
- Cálculo de diversos parâmetros de ondas, como impedância, tensão, velocidade de fase e grupo, entre outros.
- Plotagem de gráficos representando a parte real, imaginária e módulo da impedância ao longo da linha.
- Visualização de gráficos interativos das ondas de tensão e corrente ao longo da linha de transmissão.

## Requisitos

- Python 3.6 ou superior
- Matplotlib
- NumPy
- PyQt6 + Mplcursors (para `Main_PyQt.py`)
- CustomTkinter (para `Main_CTk.py`)

## Instalação

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd Projeto-microondas-PEP-IFSP
```

Instale os pacotes necessários:

```bash
pip install matplotlib NumPy PyQt6 mplcursors
```
   ou
```bash
pip install matplotlib NumPy customtkinter
```

## Como usar

1. Execute o script principal para iniciar a aplicação:

```bash
python Main_PtQt.py
```
   ou
```bash
python Main_CTk.py
```

2. Insira os valores necessários nos campos de entrada:
    - Distância da carga ao ponto (**d** em m)
    - Impedância do cabo (**Zo** em ohms)
    - Capacitância do cabo (**C** em F/m)
    - Indutância do cabo (**L** em H/m)
    - Frequência da onda (**f** em Hz)
    - Impedância da carga (**Zl** em ohms)
    - Tensão sobre a linha (**Vi** em V)
    - Números de pontos para plotagem (default=1000)
    - Ponto de amostragem (posição **x** em m)

3. Clique no botão "Calcular" para realizar os cálculos e poder visualizar resultados e gráficos.

## Estrutura do Código

- `Main_CTk.py`: Arquivo principal que contém a lógica da aplicação aplicada com a biblioteca _CustomTkinter_.
- `Prog`: Classe principal que define a interface gráfica, realizando os cálculos e plotagens.
- `Main_CTk.py`: Arquivo principal que contém a lógica da aplicação aplicada com as bibliotecas _PyQt_ e _Mplcursors_.
- `Janela`: Classe principal que define a interface gráfica, realizando os cálculos e plotagens.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

## Autores

- [Giovana C. Lopes](https://github.com/SraAmontillado)
- [Gustavo M. M. Soares](https://github.com/MoratoZ)
- [Marcelo K. Shioya Jr.](https://github.com/markazushi)

## Agradecimentos

Agradecemos ao Instituto Federal de São Paulo (IFSP) e ao Prof. Dr. Andryos da Silva Lemes pelo suporte e orientação no desenvolvimento deste projeto.

---

Feito com ❤️ por alunos do PEP-IFSP.
