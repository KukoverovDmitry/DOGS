from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import ImageTk, Image
from io import BytesIO

def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breed//image/random")
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        mb.showerror("Error", f"Error: {e}")
        return None
    d



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
            label.congiture(image=img)
            label.img = img
        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")


window = Tk()
window.title("Картинки с сайта")
window.geometry("360x420")

label = Label()
label.pack(pady=15)

button = Button(text="Загрузить картинку", command=show_image)
button.pack(pady=15)




window.mainloop()
