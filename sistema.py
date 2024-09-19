import PySimpleGUI as sg

class SistemaEquacoes:

    def __init__(self):
        self.layout = [
            sg.theme('Reddit')
            [sg.Text('Primeira Equação:')],
            [sg.Text('a:'), sg.InputText(key='a', size=(5, 1)),
             sg.Text('x +'), sg.Text('b:'), sg.InputText(key='b', size=(5, 1)),
             sg.Text('y ='), sg.Text('c:'), sg.InputText(key='c', size=(5, 1))],
             
            [sg.Text('Segunda Equação:')],
            [sg.Text('d:'), sg.InputText(key='d', size=(5, 1)),
             sg.Text('x +'), sg.Text('e:'), sg.InputText(key='e', size=(5, 1)),
             sg.Text('y ='), sg.Text('f:'), sg.InputText(key='f', size=(5, 1))],

            [sg.Button('Calcular'), sg.Button('Sair')],
            [sg.Text('Resultado:', size=(15, 1)), sg.Text('', size=(25, 1), key='resultado')]
        ]

        self.window = sg.Window('Calculadora de Sistemas de Equações', self.layout)

    def calcular_resultado(self, a, b, c, d, e, f):
        try:
            # Calcula as incógnitas x e y
            x = (c * e - b * f) / (a * e - b * d)
            y = (c - a * x) / b
            
            return x, y
        except ZeroDivisionError:
            return None, None  # Sistema impossível ou indeterminado

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, 'Sair'):
                break
            if event == 'Calcular':
                try:
                    a = float(values['a'])
                    b = float(values['b'])
                    c = float(values['c'])
                    d = float(values['d'])
                    e = float(values['e'])
                    f = float(values['f'])

                    x, y = self.calcular_resultado(a, b, c, d, e, f)
                    
                    if x is None or y is None:
                        resultado = "Erro: Sistema Impossível ou Indeterminado."
                    else:
                        resultado = f'S = {x:.2f}, {y:.2f}'
                    
                    self.window['resultado'].update(resultado)
                except ValueError:
                    self.window['resultado'].update("Erro: Valores inválidos.")

        self.window.close()


if __name__ == '__main__':
    app = SistemaEquacoes()
    app.run()
