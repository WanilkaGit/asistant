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

class SettigsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")
        self.buttons_label = Button(text="Кнопка")
        self.btns_line = GridLayout(rows=2, cols=4)
        self.btns_bgcol_r = TextInput(hint_text="R", input_type='number')
        self.btns_bgcol_g = TextInput(hint_text="G", input_type='number')
        self.btns_bgcol_b = TextInput(hint_text="B", input_type='number')
        self.btns_bgcol_h = TextInput(hint_text="H", input_type='number')

        self.btns_txtscol_r = TextInput(hint_text="R", input_type='number')
        self.btns_txtscol_g = TextInput(hint_text="G", input_type='number')
        self.btns_txtscol_b = TextInput(hint_text="B", input_type='number')
        self.btns_txtscol_h = TextInput(hint_text="H", input_type='number')

        self.text_input_label = TextInput(text="Поле вводу")
        self.txts_inp_line = GridLayout(rows=1)
        self.txts_inp_bgcol_r = TextInput(hint_text="R", input_type='number')
        self.txts_inp_bgcol_g = TextInput(hint_text="G", input_type='number')
        self.txts_inp_bgcol_b = TextInput(hint_text="B", input_type='number')
        self.txts_inp_bgcol_h = TextInput(hint_text="H", input_type='number')

        self.txts_inp_txtcol_r = TextInput(hint_text="R", input_type='number')
        self.txts_inp_txtcol_g = TextInput(hint_text="G", input_type='number')
        self.txts_inp_txtcol_b = TextInput(hint_text="B", input_type='number')
        self.txts_inp_txtcol_h = TextInput(hint_text="H", input_type='number')


        self.label_label = Label(text="Заголовок")
        self.lbls_line = GridLayout(rows=1)
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