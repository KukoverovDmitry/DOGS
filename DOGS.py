from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import ImageTk, Image
from io import BytesIO

def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        mb.showerror("Ошибка", f"Возникла ошибка по запросу к API: {e}")
        return None




def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)

            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.img = img
        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")
    progress.stop()

def prog():
    progress["value"] += 0
    progress.start(30)
    window.after(3000, show_image)



window = Tk()
window.title("Картинки с сайта")
window.geometry("360x420")

label = ttk.Label()
label.pack(pady=15)

button = ttk.Button(text="Загрузить картинку", command=prog)
button.pack(pady=15)

progress = ttk.Progressbar(window, orient="horizontal", length=280, mode="determinate")
progress.pack(pady=15)



window.mainloop()
