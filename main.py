from kivy.factory import Factory
from kivy.core.window import Window
from kivymd.app import MDApp
from pathlib import Path
from kivy.uix.screenmanager import ScreenManager

from screens.camera import CamApp


from kivy.lang import Builder


class MainApp(MDApp):

    def build(self):
        Builder.load_file('screens/camera.kv')
        # Builder.load_file('screens/camera.kv')
        
        
        sm = ScreenManager()
        sm.add_widget(CamApp(name='CameraScreen'))
        # sm.add_widget(CamApp(name='camera_screen'))
       
       
        return sm


if __name__ == '__main__':
    MainApp().run()

