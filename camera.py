from pathlib import Path

import cv2
import numpy as np
# from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
# from kivy.core.camera import camera_android
from kivy.logger import Logger
# from kivy.uix.button impordt Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy_garden.xcamera import XCamera
from kivy.lang import Builder
from kivymd.app import MDApp as App
from kivymd.uix.button import MDFlatButton as Button
from utils import make_new_texture_frame
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

Logger.info(f"Versions: Numpy {np.__version__}")
Logger.info(f"Versions: Opencv {cv2.__version__}")


class Camera(Screen, App):
    def build(self):
        return
    pass

class CameraCV(XCamera):
    def on_tex(self, *l):
        self.image_bytes = self._camera.texture.pixels
        self.image_size = self._camera.texture.size


class CamApp(App):

   
    def build(self):
       
        
        self.size_ratio = None
        self.img1 = Image(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.speed_button = Button(text="", size_hint=(0.2, 0.4),
                                   pos_hint={'center_x': 0.25, 'center_y': 0.125})
        
        self.speed_button.bind(on_press=self.set_display_speed)
        layout = FloatLayout(size=Window.size)
        layout.add_widget(self.img1)
        layout.add_widget(self.speed_button)
       

        self.display_speed = 2  # 0 for best resolution, 1 for medium, 2 for fastest display
        desired_resolution = (720, 480)
        self.camCV = CameraCV(play=True, resolution=desired_resolution)
        self.camCV.image_bytes = False

        Clock.schedule_interval(self.update_texture, 1.0 / 60.0)
        return layout

    def set_display_speed(self, instance):
        if self.display_speed == 2:
            self.display_speed = 0
        else:
            self.display_speed += 1

    def check_window_size(self):
        self.window_shape = Window.size
        self.window_width = self.window_shape[0]
        self.window_height = self.window_shape[1]
        Logger.info(f"Screen: Window size is {self.window_shape}")


    def update_texture(self, instance):
        self.check_window_size()
        if type(self.camCV.image_bytes) == bool:
            Logger.info("Camera: No valid frame")
            return
        Logger.info(f"Camera: image bytes {len(self.camCV.image_bytes)}")
        Logger.info(f"Camera: image size {self.camCV.image_size}")
        if not self.size_ratio:
            self.camera_width = self.camCV.image_size[0]
            self.camera_height = self.camCV.image_size[1]
            self.size_ratio = self.camera_height / self.camera_width

        Logger.info(f"Camera: update texture")
        self.extract_frame()
        self.process_frame()
        self.display_frame()

        Logger.info(f"Camera: converted to gray and back to rgba")

    def extract_frame(self):
        self.frame = np.frombuffer(self.camCV.image_bytes, np.uint8)
        Logger.info(f"Camera: frame exist")
        self.frame = self.frame.reshape((self.camCV.image_size[1], self.camCV.image_size[0], 4))
        Logger.info(f"Camera: frame size {self.frame.shape}")

    def process_frame(self):
       
        self.frame = cv2.rectangle(self.frame, (5, 5), (220, 220), (255, 0, 0), 2)
        self.frame = cv2.flip(self.frame, -1)

    def display_frame(self):
        self.img1.texture = make_new_texture_frame(self)


if __name__ == "__main__":
    CamApp().run()
