from PIL import Image as PILImage
from PIL import ImageFilter as PILFilter
import os

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


class EditorScreen(Screen):
    selected_dir = r"c"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.j = 0
        self.pil_images_list = []  # Список для збереження зображень PIL.Image

        self.btns_list = []
        self.paths_list = []

        self.popup = None

        self.photo_zone = KivyImage(source=None)
        self.photo_zone.fit_mode = "scale-down"


        self.btn_folder = Button(text="Папочки", size_hint=(1, 0.1))
        self.btn_folder.bind(on_release=self.chooseWorkdir)
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


    def chooseWorkdir(self, instance):
        if instance == self.btn_folder:  # Check if the button was pressed
            file_chooser = FileChooserIconView()
            file_chooser.path = EditorScreen.selected_dir
            popup = Popup(title='Виберіть папку або файл', content=file_chooser, size_hint=(0.9, 0.9))
            file_chooser.bind(on_submit=self.setWorkdir)
            popup.open()
            self.popup = popup
        
    def setWorkdir(self, instance, value, *args):
        if value is not None:
            self.path = value[0]
            if self.path:
                if os.path.exists(self.path):
                    if os.path.isdir(self.path):
                        EditorScreen.selected_dir = self.path
                    else:
                        print("Ви обрали файл:", self.path)
                        self.showFileNamesList()
                else:
                    print("Шлях не існує:", self.path)
            else:
                print("Ви не обрали папку або файл")
        self.popup.dismiss()
        return True

    def showFileNamesList(self):
        extensions = [".jpg", ".png", ".jpeg", ".bmp", ".gif", ".PNG"]
        self.filenames = [filename for filename in os.listdir(EditorScreen.selected_dir) if os.path.splitext(filename)[1].lower() in extensions]
        self.b1 = ToggleButton(text=str(os.path.basename(self.path)), group="cipher", size_hint_y = None)
        self.b1.on_press = self.chose_image
        self.photo_zone.source = self.path
        self.list_files.add_widget(self.b1)
        self.btns_list.append(self.b1)
        self.paths_list.append(self.path)
        pil_image = PILImage.open(self.paths_list[self.j])
        self.pil_images_list.append(pil_image)
        self.photo_zone.source = self.paths_list[self.j]

    def chose_image(self):
        for self.j in range(len(self.btns_list)):
            if self.btns_list[self.j].state == "down":
                self.photo_zone.source = self.paths_list[self.j]
                print(self.paths_list[self.j])
    

    
    def do_left(self):
        if self.pil_images_list:
            new_pil_image = self.pil_images_list[self.j].transpose(PILImage.ROTATE_270)
            self.pil_images_list[self.j] = new_pil_image
            self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)

    def do_right(self):
        if self.pil_images_list:
            new_pil_image = self.pil_images_list[self.j].transpose(PILImage.ROTATE_90)
            self.pil_images_list[self.j] = new_pil_image
            self.photo_zone.texture = self.convert_image_to_texture(new_pil_image)

    def do_mirorr(self):
        if self.pil_images_list:
            original_pil_image = self.pil_images_list[self.j]  # Збережіть оригінальне зображення
            mirrored_pil_image = original_pil_image.transpose(PILImage.FLIP_LEFT_RIGHT)  # Відобразити зображення
            self.pil_images_list[self.j] = mirrored_pil_image  # Замініть зображення в списку
            self.photo_zone.texture = self.convert_image_to_texture(mirrored_pil_image)  # Відобразіть зображення з ефектом

    def do_sharpner(self):
        if self.pil_images_list:
            original_pil_image = self.pil_images_list[self.j]  # Збережіть оригінальне зображення
            sharpened_pil_image = original_pil_image.filter(PILFilter.SHARPEN)  # Застосуйте ефект
            self.pil_images_list[self.j] = sharpened_pil_image  # Замініть зображення в списку
            self.photo_zone.texture = self.convert_image_to_texture(sharpened_pil_image)  # Відобразіть зображення з ефектом

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
        img_texture.blit_buffer(pil_image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        return img_texture




class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(EditorScreen(name="editor"))
        return sm

if __name__ == "__main__":

    app = HeartCheck()

    app.run()