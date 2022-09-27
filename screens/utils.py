import numpy as np
from kivy.logger import Logger
from kivy.graphics.texture import Texture
import cv2
def make_new_texture_frame(self):
    Logger.info(f"Camera: Displaying frame")
    # get image height, width
    (h, w) = self.frame.shape[:2]
    # calculate the center of the image
    center = (w / 2, h / 2)
    
    angle90 = 0
    
    scale = 1.0
   
    M = cv2.getRotationMatrix2D(center, -angle90, scale)
    self.frame = cv2.warpAffine(self.frame, M, (h, w))
    self.frame = cv2.resize(self.frame, (1280, 720))
    
    self.frame = self.frame.reshape((self.frame.shape[1], self.frame.shape[0],4))
    buf = self.frame.tostring()
    Logger.info(f"Camera: converted to bytes {len(buf)}")
    texture1 = Texture.create(size=(self.frame.shape[0], self.frame.shape[1]), colorfmt='rgba')
    texture1.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
    return texture1
               
