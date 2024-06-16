# Projeto-microondas-PEP-IFSP

# Projeto de Cálculo de Micro-ondas

Este projeto foi desenvolvido por alunos do PEP-IFSP e tem como objetivo realizar cálculos relacionados a ondas em linhas de transmissão de micro-ondas. A aplicação foi construída utilizando Python e as bibliotecas PyQt6 e Matplotlib para a interface gráfica e visualização de dados.

## Funcionalidades

- Entrada de parâmetros elétricos e físicos da linha de transmissão.
- Cálculo de diversos parâmetros de ondas, como impedância, tensão, velocidade de fase e grupo, entre outros.
- Plotagem de gráficos representando a parte real, imaginária e módulo da impedância ao longo da linha.
- Visualização de gráficos das ondas de tensão e corrente ao longo da linha de transmissão.

## Requisitos

- Python 3.6 ou superior
- PyQt6
- Matplotlib
- NumPy

## Instalação

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

## Como usar

1. Execute o script principal para iniciar a aplicação:

```bash
python main.py
```

2. Insira os valores necessários nos campos de entrada:
    - Capacitância do cabo (F/m)
    - Indutância do cabo (H/m)
    - Distância da carga ao ponto (m)
    - Impedância do cabo (ohms)
    - Tensão sobre a carga (V)
    - Impedância da carga (ohms)
    - Frequência (Hz)

3. Clique no botão "Calcular" para realizar os cálculos e visualizar os resultados e gráficos.

## Estrutura do Código

- `main.py`: Arquivo principal que contém a lógica da aplicação.
- `Janela`: Classe principal que define a interface gráfica e realiza os cálculos e plotagens.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autores

- [Nome do Aluno 1](https://github.com/usuario1)
- [Nome do Aluno 2](https://github.com/usuario2)
- [Nome do Aluno 3](https://github.com/usuario3)

## Agradecimentos

Agradecemos ao Instituto Federal de São Paulo (IFSP) pelo suporte e orientação no desenvolvimento deste projeto.

---

Feito com ❤️ por alunos do PEP-IFSP.
```

### Notas

- Substitua `https://github.com/seu-usuario/seu-repositorio.git` pelo link real do seu repositório no GitHub.
- Adicione os nomes e links para os perfis do GitHub dos autores do projeto.
- Se necessário, crie um arquivo `requirements.txt` listando as dependências (`PyQt6`, `Matplotlib`, `NumPy`).
- Verifique se a licença MIT é a desejada e, se necessário, adicione ou modifique conforme apropriado.
