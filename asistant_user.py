from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

import json


# user = {
#     "Me":{
#         "User_ID": int(),
#         "User_Name": str(),
#         "User_password": str(),
#         "User_frase": str(),
#         "User_about": str(),
#         "User_happy_birthday": {
#             "birthday_day": int(),
#             "birthday_moon": int(),
#             "birthday_year": int()
#         }}
# }

# with open("JSON\\user_info.json", "w") as file:
#     json.dump(user, file, sort_keys=True)

with open('JSON\\user_info.json', 'r') as file:
    settings = json.load(file)

def birth_day_func(birth_day, text):
    print(text)

def birth_mounth_func(birth_mounth, text):
    print(text)

def birth_year_func(birth_year, text):
    print(text)

class UserInfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_col = BoxLayout(orientation="vertical")
        main_col.bind(minimum_height=main_col.setter('height'))

        self.user_name = TextInput(hint_text="Вкажіть ваше ім'я")
        self.user_pas = TextInput(hint_text="Вкажіть пароль")
        self.user_frase = TextInput(hint_text="Ваша фраза")
        self.user_info = TextInput(hint_text="Вкажи яка ти кицюня(котик)")

        user_birth_row =GridLayout(rows=1, cols=3)

        self.birth_day = Spinner(text="День народження")
        for i in range(1, 31):
            self.birth_day.values.append(str(i))
        self.birth_day.bind(text=birth_day_func)

        self.birth_mounth = Spinner(text="Місяць народження")
        for i in range(1, 12):
            self.birth_mounth.values.append(str(i))
        self.birth_mounth.bind(text=birth_mounth_func)

        self.birth_year = Spinner(text="Рік народження")
        for i in range(1, 24):
            self.birth_year.values.append(str(i))
        self.birth_year.bind(text=birth_year_func)
        user_birth_row.add_widget(self.birth_day)
        user_birth_row.add_widget(self.birth_mounth)
        user_birth_row.add_widget(self.birth_year)

        self.saver_btn = Button(text="Зберегти все")

        main_col.add_widget(self.user_name)
        main_col.add_widget(self.user_pas)
        main_col.add_widget(self.user_frase)
        main_col.add_widget(self.user_info)
        main_col.add_widget(user_birth_row)
        main_col.add_widget(self.saver_btn)
        
        scroller = ScrollView()
        scroller.add_widget(main_col)
        self.add_widget(scroller)



class UserInfoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserInfoScreen(name="main"))
        return sm
    
if __name__ == "__main__":
    UserInfoApp().run()