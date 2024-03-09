from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup


class FolderChooserPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Виберіть папку"

        layout = BoxLayout(orientation='vertical')

        file_chooser = FileChooserListView(path='/', dirselect=True)
        # file_chooser.filters = [lambda folder, filename: folder.isdir()]

        layout.add_widget(file_chooser)

        button = Button(text="Підтвердити вибір", size_hint=(1, 0.2))
        # button.bind(on_press=self.confirm_selection)
        layout.add_widget(button)

        self.content = layout

    def confirm_selection(self, instance):
        selected_path = self.content.children[0].selection and self.content.children[0].selection[0] or ''
        if selected_path:
            print("Selected folder:", selected_path)
            self.dismiss()


class FolderChooserApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        button = Button(text="Відкрити вікно вибору папки")
        button.bind(on_press=self.open_folder_chooser)
        layout.add_widget(button)

        return layout

    def open_folder_chooser(self, instance):
        folder_chooser_popup = FolderChooserPopup()
        folder_chooser_popup.open()


if __name__ == "__main__":
    FolderChooserApp().run()
