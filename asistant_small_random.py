
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from random import randint
import json


with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

Window.clearcolor = settings["app_theme"]

class RandomScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        chose_lbl = Label(text="",font_size=50)
        self.ranint = Button(text="Кубик",  font_size=100, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.ranint.on_press = self.next
        self.one_for_4 = Button(text="1 з 4", font_size=100, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_sharp = Button(text="", font_size=10, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])

        col1 = BoxLayout(orientation="vertical")
        col1.add_widget(self.ranint)
        self.add_widget(col1)
    def next(self):# прописуємо фунції для двох кнопок 
        self.manager.current = "kube"# ереключення на натсупний екран

class KubeScreen(Screen):

    def __init__(self, **kwargs):
        global random_int, lbl_1, lbl_2, lbl_3, lbl_4, lbl_5, lbl_6, main_layout, line1, line2, line3
        super().__init__(**kwargs)
        
        random_int = randint(1,6)
        
        main_layout = BoxLayout(orientation="vertical")
        
        main_layout2 = BoxLayout(orientation="vertical", size_hint=(1, 0.4))
        
        self.reset_btn = Button(text="ще раз", font_size=80, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.reset_btn.on_press = self.reset
        
        self.start_btn = Button(text="початковий екран", font_size=80, background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.start_btn.on_press = self.start
        
        main_layout2.add_widget(self.reset_btn)
        main_layout2.add_widget(self.start_btn)
        
        main_layout3 =BoxLayout(orientation="vertical")
        if random_int == 1:
            lbl_1 = Label(text="",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            line1 = BoxLayout()
            line2 = BoxLayout()
            line3 = BoxLayout()
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3)    
            
        if random_int == 2:
            lbl_1 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3)
            
        if random_int == 3:
            lbl_1 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3) 
            
        if random_int == 4:
            lbl_1 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            line1 = BoxLayout()
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2 = BoxLayout()
            line2.add_widget(lbl_4)
            line2.add_widget(lbl_5)
            
            line3 = BoxLayout()
            
            main_layout.add_widget(line1)
            main_layout.add_widget(lbl_3)
            main_layout.add_widget(line2)

        if random_int == 5:
            lbl_1 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            line1 = BoxLayout()
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2 = BoxLayout()
            line2.add_widget(lbl_4)
            line2.add_widget(lbl_5)    
            
            line3 = BoxLayout()
            
            main_layout.add_widget(line1)
            main_layout.add_widget(lbl_3)
            main_layout.add_widget(line2)
    
        if random_int == 6:
            lbl_1 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_2 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_3 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_4 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_5 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            lbl_6 = Label(text="*",  font_size=400, color=settings["labels"]["text_color"])
            
            line1 = BoxLayout()
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2 = BoxLayout()
            line2.add_widget(lbl_3)
            line2.add_widget(lbl_4)
            
            line3 = BoxLayout()
            line3.add_widget(lbl_5)
            line3.add_widget(lbl_6)
            
            main_layout.add_widget(line1)
            main_layout.add_widget(line2)
            main_layout.add_widget(line3)
            

        
        main_layout3.add_widget(main_layout)
        main_layout3.add_widget(main_layout2)
        self.add_widget(main_layout3)
        
    def reset(self):
        global random_int, main_layout, line1, line2, line3
        
        if random_int <= 3:
            main_layout.clear_widgets()
        else:
            line1.clear_widgets()
            line2.clear_widgets()
            line3.clear_widgets()
            main_layout.clear_widgets()
        
        random_int = randint(1,6)
        
        if random_int == 1:
            lbl_1.text = ""
            lbl_2.text = "*"
            lbl_3.text = ""
            lbl_4.text = ""
            lbl_5.text = ""
            lbl_6.text = ""
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3)
            
        if random_int == 2:
            lbl_1.text = "*"
            lbl_2.text = ""
            lbl_3.text = "*"
            lbl_4.text = ""
            lbl_5.text = ""
            lbl_6.text = ""
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3)
            
        if random_int == 3:
            lbl_1.text = "*"
            lbl_2.text = "*"
            lbl_3.text = "*"
            lbl_4.text = ""
            lbl_5.text = ""
            lbl_6.text = ""
            
            main_layout.add_widget(lbl_1)
            main_layout.add_widget(lbl_2)
            main_layout.add_widget(lbl_3)
            
        if random_int == 4:
            lbl_1.text = "*"
            lbl_2.text = "*"
            lbl_3.text = ""
            lbl_4.text = "*"
            lbl_5.text = "*"
            lbl_6.text = ""
            
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2.add_widget(lbl_4)
            line2.add_widget(lbl_5)
            
            main_layout.add_widget(line1)
            main_layout.add_widget(lbl_3)
            main_layout.add_widget(line2)
            
        if random_int == 5:
            lbl_1.text = "*"
            lbl_2.text = "*"
            lbl_3.text = "*"
            lbl_4.text = "*"
            lbl_5.text = "*"
            lbl_6.text = ""
            
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2.add_widget(lbl_4)
            line2.add_widget(lbl_5)
            
            main_layout.add_widget(line1)
            main_layout.add_widget(lbl_3)
            main_layout.add_widget(line2)
            
        if random_int == 6:
            lbl_1.text = "*"
            lbl_2.text = "*"
            lbl_3.text = "*"
            lbl_4.text = "*"
            lbl_5.text = "*"
            lbl_6.text = "*"
            
            line1.add_widget(lbl_1)
            line1.add_widget(lbl_2)
            
            line2.add_widget(lbl_3)
            line2.add_widget(lbl_4)
            
            line3.add_widget(lbl_5)
            line3.add_widget(lbl_6)
            
            main_layout.add_widget(line1)
            main_layout.add_widget(line2)
            main_layout.add_widget(line3)
            
    def start(self):
            self.manager.current = "random"
            
        
        
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RandomScreen(name="random"))
        sm.add_widget(KubeScreen(name="kube"))
        return sm

if __name__ == "__main__":
    app = HeartCheck()
    app.run()