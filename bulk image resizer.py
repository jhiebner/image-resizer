from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageFilter
import os

 
def get_pull_folder():
    pull_folder = filedialog.askdirectory()
    p_folder = Label(root, text = f'Pull Folder: {pull_folder}')
    p_folder.pack()
    return pull_folder


def get_save_folder():
    save_folder = filedialog.askdirectory()
    s_folder = Label(root, text = f'Save folder: {save_folder}')
    s_folder.pack()
    return save_folder


def resize_img():
    message = Label(root, text = 'Resizing has started')
    message.pack()
    for filename in os.listdir(folder_name):
        if filename.endswith('.png'):
            img = Image.open(folder_name + "/" + filename)
            new_img = img.resize((115,115))
            new_img.save(save_folder + "/" + filename)
            print(f' {filename} resized!')
        else: pass

root = Tk()
root.title("Bulk Image Resizer")        
        

folder_name = get_pull_folder()
save_folder = get_save_folder()

resize_button = Button(
    text = "Resize folder Images",
    command = resize_img
    )
resize_button.pack()

root.mainloop()



















