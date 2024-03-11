print("Hello world")

"""Імпорта"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import choice
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
import json
    
with open('notes_data.json', 'r') as file:
    notes = json.load(file)


class SelectableLabel(Label):
    def on_touch_down(self, touch):
        global key
        if self.collide_point(*touch.pos):
            calc_screen = App.get_running_app().root.get_screen("notes")
            key = self.text
            calc_screen.text_field.text = notes[key]["текст"]
            calc_screen.massege_lbl.text = choice(["Ви обрали замітку", "Обрали, що далі робити будемо", "Обирай дію, вибір за тобою"])
            return True

"""Класи"""
class NotesScreen(Screen):# тут прописаний перший клас/екран
    def __init__(self, **kwargs):# тут можна писати скільки хочеш аргументів
        super().__init__(**kwargs)# копіюємо кістяк супер класу також

        self.list_note = []
        self.list_teg = []

        text_field_lbl = Label(text="for write", font_size=50, size_hint=(1, 0.1))
        self.text_field = TextInput(multiline=True, hint_text="НАПИШІТЬ ЩОСЬ... будь ласка")


        self.list_notes = GridLayout(cols=1, size_hint_y=None)
        self.list_notes.bind(minimum_height = self.list_notes.setter("height"))
        scroll_list_notes = ScrollView()
        scroll_list_notes.add_widget(self.list_notes)
        list_notes_lbl = Label(text="List for notes", font_size=25, size_hint=(1, 0.1))


        self.search_note_inp = TextInput(hint_text="В пиши якщо хочеш знайти потрібну тобі замітку")
        self.search_note_inp.bind(text=self.on_text)

        self.btn_create_notes = Button(text="Create note")
        self.btn_del_notes = Button(text="Delet note")

        self.btn_save_notes = Button(text="Save note", size_hint=(1, 0.24))

        self.btn_create_notes.on_press = self.show_popup
        self.btn_save_notes.on_press = self.save_note
        self.btn_del_notes.on_press = self.del_note

        row1 = BoxLayout(size_hint=(1, 0.24))
        row1.add_widget(self.btn_create_notes)
        row1.add_widget(self.btn_del_notes)

        col1 = BoxLayout(orientation="vertical")
        col1.add_widget(text_field_lbl)
        col1.add_widget(self.text_field)

        col2 = BoxLayout(orientation="vertical", size_hint=(0.5, 1))
        col2.add_widget(list_notes_lbl)
        col2.add_widget(scroll_list_notes)
        col2.add_widget(self.search_note_inp)
        col2.add_widget(row1)
        col2.add_widget(self.btn_save_notes)


        row1 = BoxLayout()
        row1.add_widget(col1)
        row1.add_widget(col2)

        main_layout = BoxLayout(orientation="vertical")
        self.massege_lbl = Label(text="Натисніть на кнопку стартової замітки", font_size=25, size_hint=(1, 0.1))
        main_layout.add_widget(self.massege_lbl)
        main_layout.add_widget(row1)

        self.add_widget(main_layout)

        for note in notes:
            self.note_lbl = SelectableLabel(text=str(note), size_hint_y = None)
            self.note_lbl.bind(on_touch_down=lambda instance, touch: self.note_lbl.on_touch_down(touch))  # Bind the touch event
            self.list_note.append(self.note_lbl)
            self.list_notes.add_widget(self.note_lbl)
    
    def on_text(self, instance, value):
            if value != "":
                self.list_notes.clear_widgets()
                self.list_note = []
                for note in notes:
                    for word in note.split():
                        for word2 in value.split():
                            if word2 == word:
                                self.massege_lbl.text = (str(self.list_note))
                                self.note_lbl = SelectableLabel(text=note, size_hint_y = None)
                                self.note_lbl.bind(on_touch_down=lambda instance, touch: self.note_lbl.on_touch_down(touch))  # Bind the touch event
                                self.list_note.append(note)
                                self.list_notes.add_widget(self.note_lbl)
            else:
                self.list_notes.clear_widgets()
                self.list_note = []
                for note in notes:
                    self.note_lbl = SelectableLabel(text=str(note), size_hint_y = None)
                    self.note_lbl.bind(on_touch_down=lambda instance, touch: self.note_lbl.on_touch_down(touch))  # Bind the touch event
                    self.list_note.append(self.note_lbl)
                    self.list_notes.add_widget(self.note_lbl)


    def show_popup(self):
        line1 = BoxLayout(orientation="vertical")
        name_note = TextInput(hint_text="тут введіть назву замітки для створення замітки")
        def sure_exit():
            if name_note.text != "":
                note_name = name_note.text
                notes[note_name] = {"текст": "", "теги": []}

                popup.dismiss()
                self.massege_lbl.text = choice(["Назву написано замітку створено починаймо писати", "Ви створили замітку", "Замітка готова до заповнення текстом"])
                self.note_lbl = SelectableLabel(text=note_name, size_hint_y = None)
                self.note_lbl.bind(on_touch_down=lambda instance, touch: self.note_lbl.on_touch_down(touch))  # Bind the touch event
                self.list_note.append(self.note_lbl)
                self.list_notes.add_widget(self.note_lbl)
                self.massege_lbl.text = choice(["Після написання не забудьте зберегти", "Не забудьте зберегти", "Текст збережіть і зарз бажано також"])
        def no_sure_exit():
            popup.dismiss()
            self.massege_lbl.text = choice(["Створення відхилено", "Ну не хочеш як хочеш", "Відмовив ха меньше працювати"])
        sure_btn = Button(text="Ok", on_release=lambda _: sure_exit())
        not_sure_btn = Button(text="Cencel", on_release=lambda _: no_sure_exit())
        line1.add_widget(name_note)
        line1.add_widget(Label(text='Це додаткове вікно'))  # Створити екземпляр класу Label
        line1.add_widget(sure_btn)
        line1.add_widget(not_sure_btn)
        content = line1
        popup = Popup(title='Заголовок', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def save_note(self):
        try:
            global key
            notes[key]["текст"] = self.text_field.text
            self.massege_lbl.text = choice(["Зберігаємо замітки текст", "Текст збережений", "Збе-ре-же-но"])
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True)
        except:
            self.massege_lbl.text = choice(["Ви не обрали замітку", "Обиріть замітку", "Що ти хочеш зберегти"])

    def del_note(self):
        try:
            if key in notes:
                del notes[key]
                self.text_field.text = ""
                for widget in self.list_note:
                    if widget.text == key:
                        self.list_notes.remove_widget(widget)
                        self.list_note.remove(widget)  # Видалити віджет із списку
                        self.massege_lbl.text = choice(["Замітку і інформаію про неї видалено", "Ви видалили заиітку", "Ви-да-ле-но"])
                with open('notes_data.json', 'w') as file:
                    json.dump(notes, file, sort_keys=True)
        except:
            self.massege_lbl.text = choice(["Ай яй яй яй обери, а потім видаляй", "Неможлива операція", "А що ти хочеш видалити"])

class HeartCheck(App):# тут прописуємо клас менеджер та клас запуску програми
    def build(self):# функція має бути в класі полюбе або пас
        sm = ScreenManager()# тут створюємо менеджера скрінів
        sm.add_widget(NotesScreen(name="notes"))# дамо кожному класу імя яке буде полегшувати переходи
        return sm
if __name__ == "__main__":
    app = HeartCheck()# це створюєм об"єкт з класу що створили для запуску цього всього
    app.run()# і визиваєм метод ран що запускає програму