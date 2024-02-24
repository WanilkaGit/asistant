from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

saveInput = ""

class CalculatorScreen(Screen):

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_col = BoxLayout(orientation="vertical")


        tools_row = BoxLayout(size_hint=(1, 0.25))
        self.info_label = TextInput(text="", foreground_color=[1, 1, 1, 1], readonly=True, font_size=25, size_hint = [1, 0.75], background_color = [0, 0, 0, 1])
        tools_row_btns_col = GridLayout(cols=1, size_hint=(0.25, 1))
        self.setings_btn = Button(text="*", font_size=100)
        self.profile_btn = Button(text="Me", font_size=50)

        tools_row.add_widget(self.info_label)
        tools_row_btns_col.add_widget(self.setings_btn)
        tools_row_btns_col.add_widget(self.profile_btn)
        tools_row.add_widget(tools_row_btns_col)
        main_col.add_widget(tools_row)


        root = BoxLayout(orientation="vertical", padding=5)
        self.result = TextInput(text="", foreground_color=[1, 1, 1, 1], readonly=True, font_size=25, size_hint = [1, 0.75], background_color = [0, 0, 0, 1])
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

        main_col.add_widget(root)
        self.add_widget(main_col)

class ProjectAsistant(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CalculatorScreen(name='main'))
        return sm


if __name__ == "__main__":
    ProjectAsistant().run()