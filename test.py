from kivy.app import App
from kivy.uix.button import Button

class ButtonsApp(App):
    def build(self):
        button = Button(
            text="Click me!",
            size_hint=(0.5, 0.5),  # Встановіть розмір, який вам потрібен
            border=(30, 30, 30, 30),  # Рамка фону кнопки
            background_color="red",  # Колір фону (RGBA)
        )
        return button

if __name__ == "__main__":
    ButtonsApp().run()