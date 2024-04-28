from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox

from kivy.core.window import Window

import json

# settings = {
#         "buttons":{
#             "bg_color": str(),
#             "text_color": str()},
#         "textinput":{
#             "bg_color": str(),
#             "text_color": str()},
#         "labels": {
#             "bg_color": str(),
#             "text_color": str()},
#         "app_theme": str()}

# with open("JSON\\settings.json", "w") as file:
#     json.dump(settings, file, sort_keys=True)

with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = ["orange", "gold", "indigo", "red", "mediumblue","limegreen", "deeppink", "snow", "black"]
        main_col = BoxLayout(orientation="vertical")

        """TOOLS ROW"""
        tools_row = BoxLayout(size_hint=(1, 0.25))

        self.info_label = TextInput(text="", foreground_color=[1, 1, 1, 1], readonly=True, font_size=25, size_hint=[1, 0.75],             
        background_color=[0, 0, 0, 1])
        tools_row.add_widget(self.info_label)

        tools_row_btns_col = GridLayout(cols=1, size_hint=(0.25, 1))
        self.setings_btn = Button(text="*", font_size=100)
        self.profile_btn = Button(text="Me", font_size=50)
        tools_row_btns_col.add_widget(self.profile_btn)
        tools_row.add_widget(tools_row_btns_col)
        main_col.add_widget(tools_row)
        """TOOLS ROW"""


        """THEME OPTIONS"""
        self.dark_white = Switch()
        self.dark_white.bind(active=self.switch_theme)


        main_col.add_widget(self.dark_white)
        front_grid = GridLayout(rows=1)
        lbl_front = Label(text="Базовий")
        front_grid.add_widget(lbl_front)
        for color in self.colors:
            self.front_radios = CheckBox(group="front_color", color=color)
            self.front_radios.text = color
            self.front_radios.bind(active=self.save_front_theme)
            front_grid.add_widget(self.front_radios)
        main_col.add_widget(front_grid)


        back_grid = GridLayout(rows=1)
        lbl_back = Label(text="Допоміжний")
        back_grid.add_widget(lbl_back)
        for color in self.colors:
            self.back_radios = CheckBox(group="back_color", color=color)
            self.back_radios.text = color
            self.back_radios.bind(active=self.save_back_theme)
            back_grid.add_widget(self.back_radios)
        main_col.add_widget(back_grid)
        """THEME OPTIONS"""

        self.add_widget(main_col)


    """THEME FUNC"""
    def switch_theme(self, instance, value):
        if value:
            Window.clearcolor = "white"
            settings["app_theme"] = "white"
        else:
            Window.clearcolor = "black"
            settings["app_theme"] = "black"


    def save_front_theme(self, instance, value):
        settings["buttons"]["bg_color"] = instance.text
        print(instance.text)
        settings["textinput"]["text_color"] = instance.text
        print(instance.text)
        settings["labels"]["text_color"] = instance.text
        print(instance.text)
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)


    def save_back_theme(self, instance, value):
        settings["buttons"]["text_color"] = instance.text
        print(instance.text)
        settings["textinput"]["bg_color"] = instance.text
        print(instance.text)
        settings["labels"]["bg_color"] = instance.text
        print(instance.text)
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)
    """THEME FUNC"""


class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()