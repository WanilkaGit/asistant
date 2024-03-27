import os
print("Поточний каталог:", os.getcwd(JSON\\notes.json))
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from asistant_small_calculator import *
from asistant_small_foto_editor import *
from asistant_samall_notes import *
from asistant_small_random import *


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")


        tools_row = BoxLayout(size_hint=(1, 0.25))

        self.info_label = TextInput(text="", foreground_color=[1, 1, 1, 1], readonly=True, font_size=25, size_hint = [1, 0.75], background_color = [0, 0, 0, 1])
        tools_row.add_widget(self.info_label)

        tools_row_btns_col = GridLayout(cols=1, size_hint=(0.25, 1))
        self.setings_btn = Button(text="*", font_size=100)
        self.setings_btn.on_press = self.settings
        self.profile_btn = Button(text="Me", font_size=50)
        self.profile_btn.on_press = self.profile
        tools_row_btns_col.add_widget(self.setings_btn)
        tools_row_btns_col.add_widget(self.profile_btn)
        tools_row.add_widget(tools_row_btns_col)


        function_grid = GridLayout(cols=2)

        self.btn_calc = Button(text="calculator", font_size=50)
        self.btn_calc.on_press=self.start_calc
        self.btn_edit = Button(text="Photo Editor", font_size=50)
        self.btn_edit.on_press=self.start_edit
        self.btn_rand = Button(text = "Randomizer", font_size=50)
        self.btn_rand.on_press=self.start_random
        self.btn_notes = Button(text="Notes", font_size=50)
        self.btn_notes.on_press=self.start_notes

        function_grid.add_widget(self.btn_calc)
        function_grid.add_widget(self.btn_edit)
        function_grid.add_widget(self.btn_rand)
        function_grid.add_widget(self.btn_notes)

        main_col.add_widget(tools_row)
        main_col.add_widget(function_grid)
        self.add_widget(main_col)


    def settings(self):
        pass

    def profile(self):
        pass

    def start_calc(self):
        self.manager.current = 'calculator'

    def start_edit(self):
        self.manager.current = "editor"

    def start_random(self):
        self.manager.current = "random"

    def start_notes(self):
        self.manager.current = 'notes'

class ProjectAsistant(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        sm.add_widget(EditorScreen(name="editor"))
        sm.add_widget(NotesScreen(name="notes"))
        sm.add_widget(RandomScreen(name="random"))
        sm.add_widget(KubeScreen(name="kube"))
        return sm

if __name__ == "__main__":
    ProjectAsistant().run()