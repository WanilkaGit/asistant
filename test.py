from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
import json


with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

class TestApp(App):
    def build(self):
        # Створення кнопки
        btn = Button(text='Натисни мене', background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"], background_normal="blue", size_hint=(0.5, 0.5))
        
        # Додавання події на натискання кнопки
        btn.bind(on_press=self.on_button_press)
        
        return btn

    def on_button_press(self, instance):
        Window.clearcolor = (0.9, 0.9, 0.9, 1) 

# Запуск додатку
if __name__ == '__main__':
    TestApp().run()

