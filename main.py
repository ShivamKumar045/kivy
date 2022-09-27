from kivy.lang import Builder
from kivy.app import App
import camera
from kivy.uix.screenmanager import Screen

kv = Builder.load_string('''
<MainWindow>:
    GridLayout:
        cols:1
        GridLayout:
            rows:1
            Button:
                text:"NOVA ROBA"
                on_release:
                    root.call_camera()
''')


class MainWindow(Screen):
    def call_camera(self):
        camera.CamApp().run()
    pass

class main_app(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    main_app().run()