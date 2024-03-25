from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.label import Label

import json

settings = {
        "buttons":{
            "bg_color": [float(), float(), float(), float()],
            "text_color": [float(), float(), float(), float()]},
        "textinput":{
            "bg_color": [float(), float(), float(), float()],
            "text_color": [float(), float(), float(), float()]},
        "labels": {
            "color": [float(), float(), float(), float()],
            "text_color": [float(), float(), float(), float()]},
        "switchers": {
            "bg_color": [float(), float(), float(), float()]}}

with open("JSON\\settings.json", "w") as file:
    json.dump(settings, file, sort_keys=True)

with open('JSON\\settings.json', 'r') as file:
    settings = json.load(file)

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")
        buttons_label = Button(text="Кнопка")
        main_col.add_widget(buttons_label)
        
        text_input_label = TextInput(text="Поле вводу")
        main_col.add_widget(text_input_label)
        
        label_label = Label(text="Заголовок")
        main_col.add_widget(label_label)
        
        switcher_label = Switch(color=[0, 1, 0, 1])
        main_col.add_widget(switcher_label)
        
        self.add_widget(main_col)

class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()