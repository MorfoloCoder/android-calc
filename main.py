from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        button_layout = GridLayout(cols=4)
        for row in buttons:
            for button in row:
                button_widget = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size=32)
                button_widget.bind(on_press=self.on_button_press)
                button_layout.add_widget(button_widget)

        layout.add_widget(button_layout)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(current))
            except Exception:
                self.result.text = 'Error'
        else:
            self.result.text = current + button_text

if __name__ == '__main__':
    CalculatorApp().run()
