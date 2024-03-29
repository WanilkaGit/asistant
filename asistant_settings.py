from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.label import Label

import json

# settings = {
#         "buttons":{
#             "bg_color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "textinput":{
#             "bg_color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "labels": {
#             "color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "switchers": {
#             "bg_color": [float(), float(), float(), float()]}}

# with open("JSON\\settings.json", "w") as file:
#     json.dump(settings, file, sort_keys=True)

with open('JSON\\settings.json', 'r') as file:
    settings = json.load(file)

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")
        self.buttons_label = Button(text="Кнопка")
        self.btns_inp_bgcol = TextInput(hint_text="В кажи колір фону кнопопк")
        self.btns_inp_txtcol = TextInput(hint_text="В кажи колір тексту")
        main_col.add_widget(self.buttons_label)
        main_col.add_widget(self.btns_inp_bgcol)
        main_col.add_widget(self.btns_inp_txtcol)
        
        self.text_input_label = TextInput(text="Поле вводу")
        self.txts_inp_inp_bgcol = TextInput(hint_text="В кажи колір фону Полей введення")
        self.txts_inp_inp_txtcol = TextInput(hint_text="В кажи колір тексту")
        main_col.add_widget(self.text_input_label)
        main_col.add_widget(self.txts_inp_inp_bgcol)
        main_col.add_widget(self.txts_inp_inp_txtcol)
        
        self.label_label = Label(text="Заголовок")
        self.lbls_inp_bgcol = TextInput(hint_text="В кажи колір фону заголовків")
        self.lbls_inp_txtcol = TextInput(hint_text="В кажи колір тексту")
        main_col.add_widget(self.label_label)
        main_col.add_widget(self.lbls_inp_bgcol)
        main_col.add_widget(self.lbls_inp_txtcol)
        
        self.switcher_label = Switch()
        main_col.add_widget(self.switcher_label)

        self.saver_btn = Button(text="Зберегти все")
        self.saver_btn.on_press = self.save_settings
        main_col.add_widget(self.saver_btn)
        
        self.add_widget(main_col)

    def save_settings(self):
        settings["buttons"]["bg_color"] = self.btns_inp_bgcol.text()  
        print(str(self.btns_inp_bgcol.text()))
        settings["buttons"]["text_color"] = self.btns_inp_txtcol.text()
        print(str(self.btns_inp_txtcol.text()))

        settings["textinput"]["bg_color"] = self.txts_inp_inp_bgcol.text()
        print(str(self.txts_inp_inp_bgcol.text()))
        settings["textinput"]["text_color"] = self.txts_inp_inp_txtcol.text()
        print(str(self.txts_inp_inp_txtcol.text()))

        settings["labels"]["bg_color"] = self.lbls_inp_bgcol.text()
        print(str(self.lbls_inp_bgcol.text()))
        settings["labels"]["text_color"] = self.lbls_inp_txtcol.text()
        print(str(self.lbls_inp_txtcol.text()))


class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()