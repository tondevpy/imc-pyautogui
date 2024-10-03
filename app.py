import PySimpleGUI as sg

# criar um tema
sg.theme('reddit')

# criar um layout
layout = [
    [sg.Text('Informe sua altura (ex: 1.80)')],
    [sg.Input(key='altura')],
    [sg.Text('Informe seu peso (ex: 76)')],
    [sg.Input(key='peso')],
    [sg.Button(button_text='Calcular')],
    [sg.Text('', key='resultado')]  
]

# criar uma janela
window = sg.Window('Calculadora de IMC', layout=layout)

# Loop de leitura de eventos
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular':
        try:
            # Obter valores de altura e peso
            altura = float(values['altura'])
            peso = float(values['peso'])

            # Calcular o IMC
            imc = peso / (altura * altura)

            # Definir a faixa de peso com base no IMC
            if imc < 18.5:
                faixa = 'Abaixo do peso'
            elif 18.5 <= imc < 25:
                faixa = 'Peso normal'
            elif 25 <= imc < 30:
                faixa = 'Sobrepeso'
            elif 30 <= imc < 35:
                faixa = 'Obesidade Grau 1'
            elif 35 <= imc < 40:
                faixa = 'Obesidade Grau 2'
            else:
                faixa = 'Obesidade Grau 3'

            # Atualizar o campo de resultado com o valor do IMC e a faixa de peso
            window['resultado'].update(f'Seu IMC é: {imc:.2f} ({faixa})')
        except ValueError:
            # Tratar erros de entrada inválida
            window['resultado'].update('Por favor, insira valores válidos!')

# Fechar a janela
window.close()
