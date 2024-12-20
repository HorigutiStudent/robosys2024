#!/usr/bin/python3

# Copyright (c) 2024 Horiguchi Masahumi
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php


import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

class ViewPicture:
    def __init__(
        self,
        picture_size:tuple=(500,707),
    ):
        self.picture_size = picture_size
        #GithubActionsでは相対パスを使用する
        self.image_path = "pictures/menue.jpg"
  
  
    def done(self) -> None:
        image = self.__get_image()
        label = tk.Label(root,image=image)
        label.pack()
        root.mainloop()
        
      
    def __get_image(self) -> ImageTk.PhotoImage:
        image = Image.open(self.image_path)
        resized = image.resize(self.picture_size,Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized)
        return tk_image

      
if __name__ == "__main__":
    view = ViewPicture()
    view.done()      
