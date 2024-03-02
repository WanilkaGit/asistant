from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color


class LineExample(BoxLayout):
    def __init__(self, **kwargs):
        super(LineExample, self).__init__(**kwargs)

        # Создаем виджет, на котором будет нарисована линия
        self.line_widget = Widget()

        # Создаем линию с красным цветом (255, 0, 0, 1)
        with self.line_widget.canvas:
            Color(.23, .72, 1, 1)
            Line(points=[100, 900, 800, 900], width=2)

        # Добавляем виджет с линией в макет
        self.add_widget(self.line_widget)


class TestApp(App):
    def build(self):
        return LineExample()


if __name__ == '__main__':
    TestApp().run()