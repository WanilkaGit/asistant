from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
import json

# settings = {
#         "buttons":{
#             "color": [float(), float(), float(), float()],
#             "size": [int(), int(), int(), int()]},
#         "textinput":{
#             "color": [float(), float(), float(), float()],
#             "size": [int(), int(), int(), int()]},
#         "labels": {
#             "color": [float(), float(), float(), float()],
#             "size": [int(), int(), int(), int()]},
#         "switchers": {
#             "color": [float(), float(), float(), float()],
#             "size": [int(), int(), int(), int()]}}

# with open("JSON\\settings.json", "w") as file:
#     json.dump(settings, file, sort_keys=True)

with open('JSON\\settings.json', 'r') as file:
    settings = json.load(file)

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")
        self.grid_line = GridLayout(rows=1)
        self.grid_line.bind(minimum_width = self.grid_line.setter("width"))
        scrol = ScrollView()
        scrol.add_widget(self.grid_line)

        self.standart_btn = Button(text="Standart")
        self.notes_btn = Button(text="Notes")
        self.random_btn = Button(text="Random")
        self.foto_editor_btn = Button(text="Foto editor")
        self.calc_btn = Button(text="Calculator")
        self.me_btn = Button(text="Me")
        self.menu_btn = Button(text="Menu")

        self.grid_line.add_widget(self.standart_btn)
        self.grid_line.add_widget(self.notes_btn)
        self.grid_line.add_widget(self.random_btn)
        self.grid_line.add_widget(self.foto_editor_btn)
        self.grid_line.add_widget(self.calc_btn)
        self.grid_line.add_widget(self.me_btn)
        self.grid_line.add_widget(self.menu_btn)
        main_col.add_widget(scrol)
        self.add_widget(main_col)

class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()