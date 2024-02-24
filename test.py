from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        label = Label(text="Modal popup example")
        line = Label(size_hint_y=None, height=2, text="", color=[0.5, 0.5, 0.5, 1]) # Сірий колір
        layout.add_widget(label)
        layout.add_widget(line)
        return layout

MyApp().run()