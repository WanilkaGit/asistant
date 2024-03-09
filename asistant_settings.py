from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.switch import Switch
from kivy.uix.button import Button

class SettingsScreen(Screen):
    def __init__(self, **kwargs):# тут можна писати скільки хочеш аргументів
        super().__init__(**kwargs)# копіюємо кістяк супер класу також
        main_col = BoxLayout()
        scrol = ScrollView()
        grid_line = GridLayout(rows=1)
        grid_line.bind(minimum_weight=grid_line.setter("weight"))
        scrol.add_widget(grid_line)
        calc_btn = Button()
        rand_btn = Button()
        menu_btn = Button()
        me_btn = Button()
        notes_btn = Button()
        foto_edit_btn = Button()
        self.add_widget(scrol)

class Settings(App):
    def build():
        sm = ScreenManager()
        sm.add_widget(SettingsScreen(name="settings"))

if __name__ == "__main__":
    Settings().run()