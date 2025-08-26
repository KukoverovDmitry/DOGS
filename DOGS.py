from tkinter import *
import requests
from PIL import ImageTk, Image
from io import BytesIO


window = Tk()
window.title("Картинки с сайта")
window.geometry("3600x4200")

label = Label()
label.pack(pady=15)

button = Button(text="Загрузить картинку", command=show_image)
button.pack(pady=15)
print("Введите ссылку на картинку")
