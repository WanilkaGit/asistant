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
#             "text_color": str(),
#             "border_color": str()},
#         "textinput":{
#             "bg_color": str(),
#             "text_color": str(),
#             "border_color": str()},
#         "labels": {
#             "text_color": str("white"),
#             "border_color": str()},
#         "app_theme": "black",
#         "front_color": str(),
#         "back_color": str(),
#         "border_color": str()}

# with open("JSON\\settings.json", "w") as file:
#     json.dump(settings, file, sort_keys=True)

with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = ["orange", "gold", "indigo", "red", "mediumblue","limegreen", "deeppink", "snow", "black"]
        main_col = BoxLayout(orientation="vertical", spacing=2)


        """THEME OPTIONS"""
        """BLACK/White THEME"""
        self.dark_white = Switch()
        if settings["app_theme"] == "white":
            self.dark_white.active = True
            Window.clearcolor = "white"
        else:
            self.dark_white.active = False
            Window.clearcolor = "black"
        self.dark_white.bind(active=self.switch_theme)


        """FRONT THEME"""
        main_col.add_widget(self.dark_white)
        front_grid = GridLayout(rows=1, spacing=2)
        lbl_front = Label(text="Базовий", color=settings["labels"]["text_color"])
        front_grid.add_widget(lbl_front)
        for color in self.colors:
            self.front_radios = CheckBox(group="front_color", color=color)
            self.front_radios.text = color
            if settings["front_color"] == self.front_radios.text:
                self.front_radios.active = True
            self.front_radios.bind(active=self.save_front_theme)
            front_grid.add_widget(self.front_radios)
        main_col.add_widget(front_grid)


        """BACK THEME"""
        back_grid = GridLayout(rows=1, spacing=2)
        lbl_back = Label(text="Допоміжний", color=settings["labels"]["text_color"])
        back_grid.add_widget(lbl_back)
        for color in self.colors:
            self.back_radios = CheckBox(group="back_color", color=color)
            self.back_radios.text = color
            if settings["back_color"] == self.back_radios.text:
                self.back_radios.active = True
            self.back_radios.bind(active=self.save_back_theme)
            back_grid.add_widget(self.back_radios)
        main_col.add_widget(back_grid)
        
        """BACK THEME"""
        border_color_grid = GridLayout(rows=1, spacing=2)
        lbl_border = Label(text="Допоміжний", color=settings["labels"]["text_color"])
        border_color_grid.add_widget(lbl_border)
        for color in self.colors:
            self.border_radios = CheckBox(group="background_color", color=color)
            self.border_radios.text = color
            if settings["border_color"] == self.border_radios.text:
                self.border_radios.active = True
            self.border_radios.bind(active=self.save_border_theme)
            border_color_grid.add_widget(self.border_radios)
        main_col.add_widget(border_color_grid)
        """THEME OPTIONS"""

        self.add_widget(main_col)


    """THEME FUNC"""
    """BLACK/WHITE"""
    def switch_theme(self, instance, value):
        if value:
            Window.clearcolor = "white"
            settings["app_theme"] = "white"
            with open("JSON\\settings.json", "w") as file:
                json.dump(settings, file, sort_keys=True)
        else:
            Window.clearcolor = "black"
            settings["app_theme"] = "black"
            with open("JSON\\settings.json", "w") as file:
                json.dump(settings, file, sort_keys=True)

    """FRONT FUNC"""
    def save_front_theme(self, instance, value):
        settings["front_color"] = instance.text
        settings["buttons"]["bg_color"] = instance.text
        settings["textinput"]["text_color"] = instance.text
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)

    """BACK FUNC"""
    def save_back_theme(self, instance, value):
        settings["back_color"] = instance.text
        settings["buttons"]["text_color"] = instance.text
        settings["labels"]["text_color"] = instance.text
        settings["textinput"]["bg_color"] = instance.text
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)
    
    def save_border_theme(self, instance, value):
        settings["border_color"] = instance.text
        settings["buttons"]["border_color"] = instance.text
        settings["labels"]["border_color"] = instance.text
        settings["textinput"]["border_color"] = instance.text
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)


class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()