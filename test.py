from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch

from kivy.uix.popup import Popup

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

class MyApp(App):
    def build(self):
        button = Button(text='Відкрити вспливаюче вікно')
        button.bind(on_release=self.show_popup)
        return button

    def show_popup(self, button):
        settings_screen = SettigsScreen()
        popup = Popup(title='Вспливаюче вікно',
                    content=settings_screen,
                    size_hint=(None, None), size=(400, 400))
        popup.open()

if __name__ == '__main__':
    MyApp().run()