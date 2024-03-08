from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.switch import Switch

class NotesScreen(Screen):# тут прописаний перший клас/екран
    a = Settings()
    a.add_kivy_panel(SettingColor())
    main = BoxLayout()
    main.add_widget(a)
    