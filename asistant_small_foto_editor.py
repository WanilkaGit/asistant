from PIL import Image as PILImage
from PIL import ImageFilter

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image as KivyImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import os
import json


with open('JSON//settings.json', 'r') as file:
    settings = json.load(file)

Window.clearcolor = settings["app_theme"]

class EditorScreen(Screen):
    selected_dir = r"d:"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.workdir = None
        self.save_dir = 'Modified/'

        self.btns_list = []
        self.popup = None

        self.photo_zone = KivyImage(source=None, keep_data=False)
        if settings["app_theme"] == "white":
            self.photo_zone.color = "black"
        elif settings["app_theme"] == "black":
            self.photo_zone.color = "white"
        self.photo_zone.fit_mode = "scale-down"

        self.btn_folder = Button(text="Папочки", size_hint=(1, 0.1), background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.list_files = GridLayout(cols=1, size_hint_y=None, spacing=2)
        self.list_files.bind(minimum_height = self.list_files.setter("height"))
        list_f_view = ScrollView()
        list_f_view.add_widget(self.list_files)

        self.btn_detail = Button(text="Деталізація", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_256_color = Button(text="Зжимання", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_left = Button(text="Вліво", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_right = Button(text="Вправо", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_mirror = Button(text="Люстерко", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_sharp = Button(text="Різкість", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_b_w = Button(text="Ч/Б", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])
        self.btn_blur = Button(text="Розмиття", background_normal="blue", background_color=settings["buttons"]["bg_color"], color=settings["buttons"]["text_color"])

        self.btn_left.on_press = self.do_left
        self.btn_right.on_press = self.do_right
        self.btn_mirror.on_press = self.do_mirorr
        self.btn_sharp.on_press = self.do_sharpner
        self.btn_b_w.on_press = self.do_b_w
        self.btn_blur.on_press = self.do_blur
        self.btn_folder.on_press = self.chooseWorkdir

        col1 = BoxLayout(orientation="vertical", size_hint=(0.145, 1), spacing=2)
        col1.add_widget(self.btn_folder)
        col1.add_widget(list_f_view)

        row2 = BoxLayout(spacing=2)
        row2.add_widget(col1)
        row2.add_widget(self.photo_zone)

        row1 = BoxLayout(size_hint=(1, 0.1), spacing=2)
        row1.add_widget(self.btn_left)
        row1.add_widget(self.btn_right)
        row1.add_widget(self.btn_mirror)
        row1.add_widget(self.btn_sharp)
        row1.add_widget(self.btn_b_w)
        row1.add_widget(self.btn_blur)
        row1.add_widget(self.btn_256_color)
        row1.add_widget(self.btn_detail)

        main_layout = BoxLayout(orientation="vertical", spacing=2)
        main_layout.add_widget(row2)
        main_layout.add_widget(row1)
        self.add_widget(main_layout)

    def chooseWorkdir(self):
        layout = BoxLayout(orientation="vertical", spacing=2)
        self.file_chooser = FileChooserIconView()
        self.file_chooser.path = "d:"
        self.file_chooser.dirselect = True
        button = Button(text="Підтвердити вибір", size_hint=(1, 0.2))
        button.on_press = self.showFileNamesList
        layout.add_widget(self.file_chooser)
        layout.add_widget(button)
        self.popup = Popup(title='Виберіть папку або файл', size_hint=(0.9, 0.9))
        self.popup.add_widget(layout)
        self.popup.open()

    def load_image(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, self.save_dir, filename)
        if not os.path.exists(image_path):
            image_path = os.path.join(dir, filename)
        print(image_path)
        self.image = PILImage.open(image_path)

    def show_image(self, path):
        dir, filename = os.path.split(path)
        self.load_image(dir, filename)
        image_path = os.path.join(dir, self.save_dir, filename)
        if not os.path.exists(image_path):
            image_path = os.path.join(dir, filename)
        self.photo_zone.source = image_path
        self.photo_zone.reload()

    def save_image(self):
        path = os.path.join(self.workdir, self.save_dir)  # шлях до папки Modified
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        full_path = os.path.join(path, self.filename)
        self.image.save(full_path)

    def showFileNamesList(self):
        self.workdir = self.file_chooser.path
        if self.workdir:
            extensions = [".jpg", ".png", ".jpeg", ".bmp", ".gif", ".PNG"]
            filenames = [filename for filename in os.listdir(self.file_chooser.path) if os.path.splitext(filename)[1].lower() in extensions]
            for filename in filenames:
                self.b1 = ToggleButton(text=filename, group="cipher", size_hint_y=None)
                self.b1.path = self.file_chooser.path+"/"+filename # тут шлях до файлу
                self.list_files.add_widget(self.b1)
                self.btns_list.append(self.b1)
                path = os.path.join(self.workdir, filename)
                self.b1.bind(on_press=lambda instance, path=path: self.show_image(path))

            self.popup.dismiss()

    def do_left(self):
        self.image = self.image.transpose(PILImage.ROTATE_90)
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.save_image()
        self.show_image(save_path)


    def do_right(self):
        self.image = self.image.transpose(PILImage.ROTATE_270)
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.save_image()
        self.show_image(save_path)

    def do_mirorr(self):
        self.image = self.image.transpose(PILImage.FLIP_LEFT_RIGHT)
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.save_image()
        self.show_image(save_path)

    def do_sharpner(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.save_image()
        self.show_image(save_path)

    def do_b_w(self):
        self.image = self.image.convert('L')
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.save_image()
        self.show_image(save_path)

    def do_blur(self):

        self.image = self.image.filter(ImageFilter.BLUR)
        
        save_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.b1.path = save_path
        self.save_image()
        self.show_image(save_path)

    # def convert_image_to_texture(self, pil_image):
    #     img_texture = Texture.create(size=(pil_image.width, pil_image.height))
    #     if pil_image.mode == "RGB":
    #         img_texture.blit_buffer(pil_image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
    #     if pil_image.mode == "RGBA":
    #         img_texture.blit_buffer(pil_image.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
    #     img_texture
    #     return img_texture

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(EditorScreen(name="random"))
        return sm

if __name__ == "__main__":
    HeartCheck().run()