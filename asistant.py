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

from asistant_settings import *
from asistant_user import *
import json


with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

Window.clearcolor = settings["app_theme"]

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")


        tools_row = BoxLayout(size_hint=(1, 0.25))

        self.info_label = TextInput(text="", readonly=True, font_size=25, size_hint = [1, 0.75], background_color=settings["textinput"]["bg_color"], foreground_color=settings["textinput"]["text_color"])
        tools_row.add_widget(self.info_label)

        tools_row_btns_col = GridLayout(cols=1, size_hint=(0.25, 1))
        self.setings_btn = Button(text="*", font_size=100, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.setings_btn.on_press = self.settings
        self.profile_btn = Button(text="Me", font_size=50, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.profile_btn.on_press = self.profile
        tools_row_btns_col.add_widget(self.setings_btn)
        tools_row_btns_col.add_widget(self.profile_btn)
        tools_row.add_widget(tools_row_btns_col)


        function_grid = GridLayout(cols=2)

        self.btn_calc = Button(text="calculator", font_size=50, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_calc.on_press=self.start_calc
        self.btn_edit = Button(text="Photo Editor", font_size=50, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_edit.on_press=self.start_edit
        self.btn_rand = Button(text = "Randomizer", font_size=50, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_rand.on_press=self.start_random
        self.btn_notes = Button(text="Notes", font_size=50, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_notes.on_press=self.start_notes

        function_grid.add_widget(self.btn_calc)
        function_grid.add_widget(self.btn_edit)
        function_grid.add_widget(self.btn_rand)
        function_grid.add_widget(self.btn_notes)

        main_col.add_widget(tools_row)
        main_col.add_widget(function_grid)
        self.add_widget(main_col)


    def settings(self):
        self.manager.current = 'settings'

    def profile(self):
        self.manager.current = 'user'

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
        sm.add_widget(SettigsScreen(name="settings"))
        sm.add_widget(WriteUserInfoScreen(name="user"))
        sm.add_widget(ProfileUserInfoScreen(name="watch_profile"))
        return sm

if __name__ == "__main__":
    ProjectAsistant().run()