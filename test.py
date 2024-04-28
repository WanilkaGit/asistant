from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
import json


with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

class TestApp(App):
    def build(self):
        # Створення кнопки
        btn = Label(text='Натисни мене', color=settings["labels"]["text_color"], size_hint=(0.5, 0.5))
        
        # Додавання події на натискання кнопки
        btn.bind(on_press=self.on_button_press)
        
        return btn

    def on_button_press(self, instance):
        Window.clearcolor = (0.9, 0.9, 0.9, 1) 

# Запуск додатку
if __name__ == '__main__':
    TestApp().run()

