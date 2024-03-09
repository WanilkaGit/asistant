from PIL import Image as PILImage
from PIL import ImageFilter as PILFilter

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image as KivyImage
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import os


class EditorScreen(Screen):
    selected_dir = r"c"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.path = None
        self.j = 0
        self.pil_images_list = []  # Список для збереження зображень PIL.Image

        self.btns_list = []
        self.paths_list = []

        self.popup = None

        self.photo_zone = KivyImage(source=None)
        self.photo_zone.fit_mode = "scale-down"

        self.btn_folder = Button(text="Папочки", size_hint=(1, 0.1))
        self.list_files = GridLayout(cols=1, size_hint_y=None)
        self.list_files.bind(minimum_height = self.list_files.setter("height"))
        list_f_view = ScrollView()
        list_f_view.add_widget(self.list_files)

        self.btn_detail = Button(text="Деталізація")
        self.btn_256_color = Button(text="Зжимання")
        self.btn_left = Button(text="Вліво")
        self.btn_right = Button(text="Вправо")
        self.btn_mirror = Button(text="Люстерко")
        self.btn_sharp = Button(text="Різкість")
        self.btn_b_w = Button(text="Ч/Б")
        self.btn_blur = Button(text="Розмиття")

        self.btn_left.on_press = self.do_left
        self.btn_right.on_press = self.do_right
        self.btn_mirror.on_press = self.do_mirorr
        self.btn_sharp.on_press = self.do_sharpner
        self.btn_b_w.on_press = self.do_b_w
        self.btn_folder.on_press = self.chooseWorkdir

        col1 = BoxLayout(orientation="vertical", size_hint=(0.145, 1))
        col1.add_widget(self.btn_folder)
        col1.add_widget(list_f_view)

        row2 = BoxLayout()
        row2.add_widget(col1)
        row2.add_widget(self.photo_zone)

        row1 = BoxLayout(size_hint=(1, 0.1))
        row1.add_widget(self.btn_left)
        row1.add_widget(self.btn_right)
        row1.add_widget(self.btn_mirror)
        row1.add_widget(self.btn_sharp)
        row1.add_widget(self.btn_b_w)
        row1.add_widget(self.btn_blur)
        row1.add_widget(self.btn_256_color)
        row1.add_widget(self.btn_detail)

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(row2)
        main_layout.add_widget(row1)
        self.add_widget(main_layout)

    def chooseWorkdir(self):
        layout = BoxLayout(orientation="vertical")
        self.file_chooser = FileChooserIconView()
        self.file_chooser.dirselect = True
        button = Button(text="Підтвердити вибір", size_hint=(1, 0.2))
        button.on_press = self.showFileNamesList
        layout.add_widget(self.file_chooser)
        layout.add_widget(button)
        self.popup = Popup(title='Виберіть папку або файл', size_hint=(0.9, 0.9))
        self.popup.add_widget(layout)
        self.popup.open()

    # def setWorkdir(self, instance):
    #     print(self.file_chooser.path)
    #     if self.file_chooser.path:
    #         print("Ви обрали файл:", self.path)
    #         self.showFileNamesList()
    #     else:
    #         print("Шлях не існує:", self.path)
    #     self.popup.dismiss()
    #     return True
    def showFileNamesList(self):
        if self.file_chooser.path:
            extensions = [".jpg", ".png", ".jpeg", ".bmp", ".gif", ".PNG"]
            self.filenames = [filename for filename in os.listdir(self.file_chooser.path) if os.path.splitext(filename)[1].lower() in extensions]
            print(self.filenames)
            print(self.file_chooser.path)
            i = 0
            for filename in self.filenames:
                self.b1 = ToggleButton(text=filename, group="cipher", size_hint_y=None)
                self.list_files.add_widget(self.b1)
                self.btns_list.append(self.b1)
                self.b1.on_press = self.chose_image
                self.full_path = os.path.join(self.file_chooser.path, filename)
                self.paths_list.append(self.full_path)
                pil_image = PILImage.open(self.paths_list[i])
                self.pil_images_list.append(pil_image)
                i += 1
            self.popup.dismiss()

    def chose_image(self):
        for i in range(len(self.btns_list)):
            if self.btns_list[i].state == "down":
                self.photo_zone.source = self.paths_list[i]

    def do_left(self):
        if self.pil_images_list:
            for i in range(len(self.pil_images_list)):
                if self.btns_list[i].state == 'down':
                    new_pil_image = self.pil_images_list[i].transpose(PILImage.ROTATE_270)
                    self.pil_images_list[i] = new_pil_image
                    self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)

    def do_right(self):
        if self.pil_images_list:
            for i in range(len(self.pil_images_list)):
                if self.btns_list[i].state == 'down':
                    new_pil_image = self.pil_images_list[i].transpose(PILImage.ROTATE_90)
                    self.pil_images_list[i] = new_pil_image
                    self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)


    def do_mirorr(self):
        if self.pil_images_list:
            for i in range(len(self.pil_images_list)):
                if self.btns_list[i].state == 'down':
                    new_pil_image = self.pil_images_list[i].transpose(PILImage.FLIP_LEFT_RIGHT)
                    self.pil_images_list[i] = new_pil_image
                    self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)

    def do_sharpner(self):
        if self.pil_images_list:
            for i in range(len(self.pil_images_list)):
                if self.btns_list[i].state == 'down':
                    new_pil_image = self.pil_images_list[i].filter(PILFilter.SHARPEN)
                    self.pil_images_list[i] = new_pil_image
                    self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)

    def do_b_w(self):
        if self.pil_images_list:
            try:
                print("Тут має бути щось")
                original_pil_image = self.pil_images_list[self.j]  # Збережіть оригінальне зображення
                print("Тут має бути щось")
                bw_pil_image = original_pil_image.convert("L")  # Застосувати ефект
                print("Тут має бути щось")
                self.pil_images_list[self.j] = bw_pil_image  # Замінити зображення в списку
                print("Тут має бути щось")
                self.photo_zone.texture = self.convert_image_to_texture(bw_pil_image)
                print("Тут має бути щось")
            except Exception as e:
                print("Помилка під час конвертації відтінків сірого:", e)


    def convert_image_to_texture(self, pil_image):
        img_texture = Texture.create(size=(pil_image.width, pil_image.height))
        if pil_image.mode == "RGB":
            img_texture.blit_buffer(pil_image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        if pil_image.mode == "RGBA":
            img_texture.blit_buffer(pil_image.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        return img_texture