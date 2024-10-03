# Calculadora de IMC

Este é um projeto simples de uma **Calculadora de IMC** (Índice de Massa Corporal) utilizando a biblioteca **PySimpleGUI** para interface gráfica.

## Descrição

A Calculadora de IMC permite ao usuário inserir a sua altura e peso, e calcular automaticamente o seu IMC, além de fornecer uma classificação de acordo com as faixas de IMC definidas pela OMS (Organização Mundial da Saúde).

### Fórmula do IMC:

A fórmula utilizada para o cálculo do IMC é a seguinte:

IMC = peso / (altura * altura)

Onde:
- **peso** é informado em quilogramas (kg);
- **altura** é informada em metros (m).

### Faixas de IMC:

- **Abaixo de 18.5**: Abaixo do peso.
- **Entre 18.5 e 24.9**: Peso normal.
- **Entre 25 e 29.9**: Sobrepeso.
- **Entre 30 e 34.9**: Obesidade Grau 1.
- **Entre 35 e 39.9**: Obesidade Grau 2.
- **Acima de 40**: Obesidade Grau 3 (Obesidade Mórbida).

## Requisitos

Para rodar este projeto, você precisará do **Python 3** instalado e das seguintes bibliotecas:

- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)

Para instalar o **PySimpleGUI**, execute:

```bash
pip install PySimpleGUI