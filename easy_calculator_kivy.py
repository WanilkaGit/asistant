from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

saveInput = ""

class Calculator(App):

    def calculate(self, symbol): # add a colon here
        global saveInput
        if symbol.text == "<=": # use == instead of is
            saveInput = self.result.text = ""
        elif symbol.text != "=": # use != instead of is not
            self.result.text += symbol.text
            saveInput += symbol.text
        else:
            try:
                saveInput = self.result.text = str(eval(saveInput))
            except ZeroDivisionError: # handle zero division error
                self.result.text = "Cannot divide by zero"
                saveInput = ""
            except SyntaxError: # handle syntax error
                self.result.text = "Invalid expression"
                saveInput = ""
            except Exception as e: # handle any other error
                self.result.text = "Error"
                saveInput = ""
                print(e)

    def build(self):
        root = BoxLayout(orientation="vertical", padding=5)

        self.result = TextInput(
            text="", foreground_color=[1, 1, 1, 1], readonly=True, font_size=25,
            size_hint = [1, 0.75], background_color = [0, 0, 0, 1])
        root.add_widget(self.result)

        btn_grid = GridLayout(rows=5)

        btn_grid.add_widget(Button(text="<=", on_press=self.calculate, color="#9400D3"))
        btn_grid.add_widget(Button(text="%", on_press=self.calculate))
        btn_grid.add_widget(Button(text="(", on_press=self.calculate))
        btn_grid.add_widget(Button(text=")", on_press=self.calculate))

        btn_grid.add_widget(Button(text="7", on_press=self.calculate))
        btn_grid.add_widget(Button(text="8", on_press=self.calculate))
        btn_grid.add_widget(Button(text="9", on_press=self.calculate))
        btn_grid.add_widget(Button(text="*", on_press=self.calculate))


        btn_grid.add_widget(Button(text="4", on_press=self.calculate))
        btn_grid.add_widget(Button(text="5", on_press=self.calculate))
        btn_grid.add_widget(Button(text="6", on_press=self.calculate))
        btn_grid.add_widget(Button(text="+", on_press=self.calculate))


        btn_grid.add_widget(Button(text="1", on_press=self.calculate))
        btn_grid.add_widget(Button(text="2", on_press=self.calculate))
        btn_grid.add_widget(Button(text="3", on_press=self.calculate))
        btn_grid.add_widget(Button(text="/", on_press=self.calculate))

        btn_grid.add_widget(Button(text=".", on_press=self.calculate))
        btn_grid.add_widget(Button(text="0", on_press=self.calculate))
        btn_grid.add_widget(Button(text="=", on_press=self.calculate))
        btn_grid.add_widget(Button(text="-", on_press=self.calculate))


        root.add_widget(btn_grid)
        return root

if __name__ == "__main__":
    Calculator().run()