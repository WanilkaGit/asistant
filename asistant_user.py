from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

import json
from time import sleep

import json

# user = {
#     "User_ID": int(),
#     "User_Name": str(),
#     "User_Password": str(),
#     "User_Frase": str(),
#     "User_About": str(),
#     "User_Happy_Birthday": {
#         "Birthday_Day": int(),
#         "Birthday_Moon": int(),
#         "Birthday_Year": int()
#     }
# }

# # Виправлено шлях до файлу, використовуючи правильний роздільник для Windows
# # Додано параметр encoding для відкриття файлу
# with open("JSON\\user_info.json", "w", encoding="utf-8") as file:
#     json.dump(user, file, sort_keys=True, ensure_ascii=False)


with open('JSON//user_info.json', 'r', encoding="utf-8") as file:
    user = json.load(file)
print(user)

def birth_day_func(birth_day, text):
    print(text)

def birth_mounth_func(birth_mounth, text):
    print(text)

def birth_year_func(birth_year, text):
    print(text)

class WriteUserInfoScreen(Screen):
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
        for i in range(1, 32):
            self.birth_day.values.append(str(i))
        self.birth_day.bind(text=birth_day_func)

        self.birth_mounth = Spinner(text="Місяць народження")
        for i in range(1, 13):
            self.birth_mounth.values.append(str(i))
        self.birth_mounth.bind(text=birth_mounth_func)

        self.birth_year = Spinner(text="Рік народження")
        for i in range(1, 25):
            self.birth_year.values.append(str(i))
        self.birth_year.bind(text=birth_year_func)
        user_birth_row.add_widget(self.birth_day)
        user_birth_row.add_widget(self.birth_mounth)
        user_birth_row.add_widget(self.birth_year)

        self.saver_btn = Button(text="Зберегти все", background_normal="blue")
        self.saver_btn.on_press = self.save_ans

        self.skip_btn = Button(text="Я маю записані дані і не бажаю змін", background_normal="blue")
        self.skip_btn.on_press = self.skip_rewrite

        main_col.add_widget(self.user_name)
        main_col.add_widget(self.user_pas)
        main_col.add_widget(self.user_frase)
        main_col.add_widget(self.user_info)
        main_col.add_widget(user_birth_row)
        main_col.add_widget(self.saver_btn)
        main_col.add_widget(self.skip_btn)
        
        scroller = ScrollView()
        scroller.add_widget(main_col)
        self.add_widget(scroller)

    def save_ans(self):
        print(self.user_name.text)
        user["User_Name"] = self.user_name.text
        print(self.user_pas.text)
        user["User_Password"] = self.user_pas.text
        print(self.user_frase.text)
        user["User_Frase"] = self.user_frase.text
        print(self.user_info.text)
        user["User_About"] = self.user_info.text
        print(self.birth_day.text)
        user["User_Happy_Birthday"]["Birthday_Day"] = self.birth_day.text
        print(self.birth_mounth.text)
        user["User_Happy_Birthday"]["Birthday_Moon"] = self.birth_mounth.text
        print(self.birth_year.text)
        user["User_Happy_Birthday"]["Birthday_Year"] = self.birth_year.text
        print(user)
        with open("JSON\\user_info.json", "w", encoding='utf-8') as file:
                json.dump(user, file, ensure_ascii=False, indent=4)
                sleep(5)
        self.skip_rewrite()

    def skip_rewrite(self):
        self.manager.current = "watch_profile"

class ProfileUserInfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('JSON//user_info.json', 'r') as file:
            user = json.load(file)

        main_col = BoxLayout(orientation="vertical")

        user_name = Label(text="Користувач: @"+user["User_Name"])
        user_hb = Label(text=str(user["User_Happy_Birthday"]["Birthday_Day"])+"/"+str(user["User_Happy_Birthday"]["Birthday_Moon"])+"/"+str(user["User_Happy_Birthday"]["Birthday_Year"]))
        user_pas = Label(text="Користувацький пароль: " + user["User_Password"])
        user_frase = Label(text="Корисувач каже: " + user["User_Frase"])
        user_information = TextInput(readonly=True, text="Про користувача: "+user["User_About"])

        main_col.add_widget(user_name)
        main_col.add_widget(user_hb)
        main_col.add_widget(user_pas)
        main_col.add_widget(user_frase)
        main_col.add_widget(user_information)
        self.add_widget(main_col)



class UserInfoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ProfileUserInfoScreen(name="watch_profile"))
        sm.add_widget(WriteUserInfoScreen(name="main"))
        return sm
    
if __name__ == "__main__":
    UserInfoApp().run()