from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

import json

# settings = {
#         "buttons":{
#             "bg_color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "textinput":{
#             "bg_color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "labels": {
#             "bg_color": [float(), float(), float(), float()],
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

        main_col.add_widget(Label(text="Швидка настройка"))
        self.switch = Switch()
        self.switch.bind(active=self.on_switch_active)
        main_col.add_widget(self.switch)

        self.buttons_label = Button(text="Кнопка")
        self.btns_line = GridLayout(rows=2, cols=4)
        main_col.add_widget(self.buttons_label)
        main_col.add_widget(self.btns_line)
        self.btns_bgcol_r = TextInput(hint_text="R", input_type='number')
        self.btns_bgcol_g = TextInput(hint_text="G", input_type='number')
        self.btns_bgcol_b = TextInput(hint_text="B", input_type='number')
        self.btns_bgcol_h = TextInput(hint_text="H", input_type='number')

        self.btns_txtcol_r = TextInput(hint_text="R", input_type='number')
        self.btns_txtcol_g = TextInput(hint_text="G", input_type='number')
        self.btns_txtcol_b = TextInput(hint_text="B", input_type='number')
        self.btns_txtcol_h = TextInput(hint_text="H", input_type='number')

        self.btns_line.add_widget(self.btns_bgcol_r)
        self.btns_line.add_widget(self.btns_bgcol_g)
        self.btns_line.add_widget(self.btns_bgcol_b)
        self.btns_line.add_widget(self.btns_bgcol_h)

        self.btns_line.add_widget(self.btns_txtcol_r)
        self.btns_line.add_widget(self.btns_txtcol_g)
        self.btns_line.add_widget(self.btns_txtcol_b)
        self.btns_line.add_widget(self.btns_txtcol_h)

        self.text_input_label = TextInput(text="Поле вводу")
        self.txts_inp_line = GridLayout(rows=2, cols=4)
        main_col.add_widget(self.text_input_label)
        main_col.add_widget(self.txts_inp_line)
        self.txts_inp_bgcol_r = TextInput(hint_text="R", input_type='number')
        self.txts_inp_bgcol_g = TextInput(hint_text="G", input_type='number')
        self.txts_inp_bgcol_b = TextInput(hint_text="B", input_type='number')
        self.txts_inp_bgcol_h = TextInput(hint_text="H", input_type='number')

        self.txts_inp_txtcol_r = TextInput(hint_text="R", input_type='number')
        self.txts_inp_txtcol_g = TextInput(hint_text="G", input_type='number')
        self.txts_inp_txtcol_b = TextInput(hint_text="B", input_type='number')
        self.txts_inp_txtcol_h = TextInput(hint_text="H", input_type='number')

        self.txts_inp_line.add_widget(self.txts_inp_bgcol_r)
        self.txts_inp_line.add_widget(self.txts_inp_bgcol_g)
        self.txts_inp_line.add_widget(self.txts_inp_bgcol_b)
        self.txts_inp_line.add_widget(self.txts_inp_bgcol_h)

        self.txts_inp_line.add_widget(self.txts_inp_txtcol_r)
        self.txts_inp_line.add_widget(self.txts_inp_txtcol_g)
        self.txts_inp_line.add_widget(self.txts_inp_txtcol_b)
        self.txts_inp_line.add_widget(self.txts_inp_txtcol_h)


        self.label_label = Label(text="Заголовок")
        self.lbls_line = GridLayout(rows=2, cols=4)
        main_col.add_widget(self.label_label)
        main_col.add_widget(self.lbls_line)
        self.lbls_bgcol_r = TextInput(hint_text="R", input_type='number')
        self.lbls_bgcol_g = TextInput(hint_text="G", input_type='number')
        self.lbls_bgcol_b = TextInput(hint_text="B", input_type='number')
        self.lbls_bgcol_h = TextInput(hint_text="H", input_type='number')

        self.lbls_txtcol_r = TextInput(hint_text="R", input_type='number')
        self.lbls_txtcol_g = TextInput(hint_text="G", input_type='number')
        self.lbls_txtcol_b = TextInput(hint_text="B", input_type='number')
        self.lbls_txtcol_h = TextInput(hint_text="H", input_type='number')

        self.lbls_line.add_widget(self.lbls_bgcol_r)
        self.lbls_line.add_widget(self.lbls_bgcol_g)
        self.lbls_line.add_widget(self.lbls_bgcol_b)
        self.lbls_line.add_widget(self.lbls_bgcol_h)

        self.lbls_line.add_widget(self.lbls_txtcol_r)
        self.lbls_line.add_widget(self.lbls_txtcol_g)
        self.lbls_line.add_widget(self.lbls_txtcol_b)
        self.lbls_line.add_widget(self.lbls_txtcol_h)


        self.saver_btn = Button(text="Зберегти все")
        self.saver_btn.on_press = self.save_settings
        main_col.add_widget(self.saver_btn)
        
        self.add_widget(main_col)

    def save_settings(self):
        settings["textinput"]["bg_color"][0] = float(self.txts_inp_bgcol_r.text) / 255
        print(float(self.txts_inp_bgcol_r.text)/255)
        settings["textinput"]["bg_color"][1] = float(self.txts_inp_bgcol_g.text) / 255
        print(float(self.txts_inp_bgcol_g.text)/255)
        settings["textinput"]["bg_color"][2] = float(self.txts_inp_bgcol_b.text) / 255
        print(float(self.txts_inp_bgcol_b.text)/255)
        settings["textinput"]["bg_color"][3] = float(self.txts_inp_bgcol_h.text) / 100
        print(float(self.txts_inp_bgcol_h.text)/100)

        settings["textinput"]["text_color"][0] = float(self.txts_inp_txtcol_r.text) / 255
        print(float(self.txts_inp_txtcol_r.text)/255)
        settings["textinput"]["text_color"][0] = float(self.txts_inp_txtcol_r.text) / 255
        print(float(self.txts_inp_txtcol_r.text)/255)
        settings["textinput"]["text_color"][0] = float(self.txts_inp_txtcol_r.text) / 255
        print(float(self.txts_inp_txtcol_r.text)/255)
        settings["textinput"]["text_color"][0] = float(self.txts_inp_txtcol_r.text) / 255
        print(float(self.txts_inp_txtcol_r.text)/255)


        settings["textinput"]["bg_color"][0] = float(self.txts_inp_bgcol_r.text) / 255
        print(float(self.txts_inp_bgcol_r.text)/255)
        settings["textinput"]["bg_color"][1] = float(self.txts_inp_bgcol_g.text) / 255
        print(float(self.txts_inp_bgcol_g.text)/255)
        settings["textinput"]["bg_color"][2] = float(self.txts_inp_bgcol_b.text) / 255
        print(float(self.txts_inp_bgcol_b.text)/255)
        settings["textinput"]["bg_color"][3] = float(self.txts_inp_bgcol_h.text) / 100
        print(float(self.txts_inp_bgcol_h.text)/100)

        settings["textinput"]["text_color"][0] = float(self.txts_inp_txtcol_r.text) / 255
        print(float(self.txts_inp_txtcol_r.text)/255)
        settings["textinput"]["text_color"][1] = float(self.txts_inp_txtcol_g.text) / 255
        print(float(self.txts_inp_txtcol_g.text)/255)
        settings["textinput"]["text_color"][2] = float(self.txts_inp_txtcol_b.text) / 255
        print(float(self.txts_inp_txtcol_b.text)/255)
        settings["textinput"]["text_color"][3] = float(self.txts_inp_txtcol_h.text) / 100
        print(float(self.txts_inp_txtcol_h.text)/255)


        settings["labels"]["bg_color"][0] = float(self.lbls_bgcol_r.text) / 255
        print(float(self.lbls_bgcol_r.text)/255)
        settings["labels"]["bg_color"][1] = float(self.lbls_bgcol_g.text) / 255
        print(float(self.lbls_bgcol_g.text)/255)
        settings["labels"]["bg_color"][2] = float(self.lbls_bgcol_b.text) / 255
        print(float(self.lbls_bgcol_b.text)/255)
        settings["labels"]["bg_color"][3] = float(self.lbls_bgcol_h.text) / 100
        print(float(self.lbls_bgcol_h.text)/100)

        settings["labels"]["text_color"][0] = float(self.lbls_txtcol_r.text) / 255
        print(float(self.lbls_txtcol_r.text)/255)
        settings["labels"]["text_color"][1] = float(self.lbls_txtcol_g.text) / 255
        print(float(self.lbls_txtcol_g.text)/255)
        settings["labels"]["text_color"][2] = float(self.lbls_txtcol_b.text) / 255
        print(float(self.lbls_txtcol_b.text)/255)
        settings["labels"]["text_color"][3] = float(self.lbls_txtcol_h.text) / 100
        print(float(self.lbls_txtcol_h.text)/100)
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)

    def on_switch_active (self, instance, value):
        print(value)
        if value:
            settings = {
                    "buttons":{
                        "bg_color": [0, 0, 0, 1],
                        "text_color": [1, 1, 1, 1]},
                    "textinput":{
                        "bg_color": [0, 0, 0, 1],
                        "text_color": [1, 1, 1, 1]},
                    "labels": {
                        "bg_color": [0, 0, 0, 1],
                        "text_color": [1, 1, 1, 1]},
                    "switchers": {
                        "bg_color": [0, 0, 0, 1]}}
        else:
            settings = {
                    "buttons":{
                        "bg_color": [1, 1, 1, 1],
                        "text_color": [0, 0, 0, 1]},
                    "textinput":{
                        "bg_color": [1, 1, 1, 1],
                        "text_color": [0, 0, 0, 1]},
                    "labels": {
                        "bg_color": [1, 1, 1, 1],
                        "text_color": [0, 0, 0, 1]},
                    "switchers": {
                        "bg_color": [0, 0, 0, 1]}}
        with open("JSON\\settings.json", "w") as file:
            json.dump(settings, file, sort_keys=True)

class SettingsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettigsScreen(name='menu'))
        return sm

if __name__ == "__main__":
    SettingsApp().run()