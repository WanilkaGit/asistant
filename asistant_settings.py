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
#             "color": [float(), float(), float(), float()],
#             "text_color": [float(), float(), float(), float()]},
#         "switchers": {
#             "bg_color": [float(), float(), float(), float()]}}

# with open("JSON\\settings.json", "w") as file:
#     json.dump(settings, file, sort_keys=True)

with open('JSON\\settings.json', 'r') as file:
    settings = json.load(file)

def btns_func_bgcol_r(text, btns_bgcol_r):
    print(text)
    settings["buttons"]["bg_color"][0] = float(text) / 256

def btns_func_bgcol_g(text, btns_bgcol_g):
    print(text)
    settings["buttons"]["bg_color"][1] = float(text) / 256

def btns_func_bgcol_b(text, btns_bgcol_b):
    print(text)
    settings["buttons"]["bg_color"][2] = float(text) / 256

def btns_func_bgcol_r(text, btns_bgcol_r):
    print(text)
    settings["buttons"]["bg_color"][3] = float(text) / 100


def txts_inp_func_bgcol_r(text, txts_bgcol_r):
    print(text)
    settings["textinput"]["bg_color"][0] = float(text) / 256

def txts_inp_func_bgcol_g(text, txts_bgcol_g):
    print(text)
    settings["textinput"]["bg_color"][1] = float(text) / 256

def txts_inp_func_bgcol_b(text, txts_bgcol_b):
    print(text)
    settings["textinput"]["bg_color"][2] = float(text) / 256

def txts_inp_func_bgcol_h(text, txts_bgcol_h):
    print(text)
    settings["textinput"]["bg_color"][3] = float(text) / 100


def lbls_func_bgcol_r(text, txts_bgcol_r):
    print(text)
    settings["textinput"]["bg_color"][0] = float(text) / 256

def lbls_func_bgcol_g(text, txts_bgcol_g):
    print(text)
    settings["textinput"]["bg_color"][1] = float(text) / 256

def lbls_func_bgcol_b(text, txts_bgcol_b):
    print(text)
    settings["textinput"]["bg_color"][2] = float(text) / 256

def lbls_func_bgcol_h(text, txts_bgcol_h):
    print(text)
    settings["textinput"]["bg_color"][3] = float(text) / 100


class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")

####################### BUTTONS #######################
        
        self.buttons_label = Button(text="Кнопка")
        self.btns_line = GridLayout(rows=1)


        self.btns_bgcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.btns_bgcol_r.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_bgcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.btns_bgcol_g.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_bgcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.btns_bgcol_b.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_bgcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.btns_bgcol_h.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)


        self.btns_txtcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.btns_txtcol_r.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_txtcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.btns_txtcol_g.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_txtcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.btns_txtcol_b.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        self.btns_txtcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.btns_txtcol_h.values.append(str(i))
            self.btns_bgcol_r.bind(text=btns_func_bgcol_r)
        main_col.add_widget(self.buttons_label)
        main_col.add_widget(self.btns_line)

####################### TEXT INPUTS #######################

        self.text_input_label = TextInput(text="Поле вводу")
        self.txts_inp_line = GridLayout(rows=1)

        self.txts_inp_bgcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.txts_inpbgcol_r.values.append(str(i))
            self.txts_inpbgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inpbgcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.txts_inpbgcol_g.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inp_bgcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.txts_inp_bgcol_b.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inp_bgcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.txts_inp_bgcol_h.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)


        self.txts_inp_txtcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.txts_inp_txtcol_r.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inp_txtcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.txts_inp_txtcol_g.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inp_txtcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.txts_inp_txtcol_b.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        self.txts_inp_txtcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.txtcol_h.values.append(str(i))
            self.txts_inp_bgcol_r.bind(text=txts_inp_func_bgcol_r)

        main_col.add_widget(self.text_input_label)
        main_col.add_widget(self.txts_inp_line)

####################### LBLS #######################

        self.label_label = Label(text="Заголовок")
        self.lbls_line = GridLayout(rows=1)

        self.lbls_bgcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.lbls_bgcol_r.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_bgcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.lbls_bgcol_g.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_bgcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.lbls_bgcol_b.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_bgcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.lbls_bgcol_h.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)


        self.lbls_txtcol_r = Spinner(text="R")
        for i in range(1, 256):
            self.txtcol_r.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_txtcol_g = Spinner(text="G")
        for i in range(1, 256):
            self.txtcol_g.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_txtcol_b = Spinner(text="B")
        for i in range(1, 256):
            self.lbls_txtcol_b.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)

        self.lbls_txtcol_h = Spinner(text="H")
        for i in range(1, 101):
            self.lbls_txtcol_h.values.append(str(i))
            self.lbls_bgcol_r.bind(text=lbls_func_bgcol_r)


        main_col.add_widget(self.label_label)
        main_col.add_widget(self.lbls_line)

        
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