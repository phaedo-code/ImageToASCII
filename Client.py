import tkinter as tk
from PIL import Image

# Jeffrie McGehee 2.23.25 | Image to ASCII

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

with Image.open('sky.jpg') as im:

    # color = 1 or 2 inverts the colors shown
    color = 1
    # change the size of the ASCII text
    label_size = 5
    # size of the total window
    window_x = im.size[0] * label_size
    window_y = im.size[1] * label_size

    root = tk.Tk()
    # canvas
    canvas = tk.Canvas(root, width = window_x, height = window_y, bg = "black")

    root.geometry(f"{window_x}x{window_y}")
    root.title("TextGrid")

    gridx = round(window_x / label_size)
    gridy = round(window_y / label_size)
    # iterate over each pixel and create a label with the ASCII of the pixel
    for y in range(gridy):
        for x in range(gridx):
            rgbcolor = rgb_to_hex(im.getpixel((x, y))[0], im.getpixel((x, y))[1], im.getpixel((x, y))[2])
            if im.getpixel((x, y))[color] < 10:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f".", font=("Arial", label_size), fill=rgbcolor)
            elif im.getpixel((x, y))[color] < 30:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"-", font=("Arial", label_size), fill=rgbcolor)
            elif im.getpixel((x, y))[color] < 50:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"+", font=("Arial", label_size), fill=rgbcolor)
            elif im.getpixel((x, y))[color] < 100:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"o", font=("Arial", label_size), fill=rgbcolor)
            elif im.getpixel((x, y))[color] < 150:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"x", font=("Arial", label_size), fill=rgbcolor)
            elif im.getpixel((x, y))[color] < 200:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"X", font=("Arial", label_size), fill=rgbcolor)
            else:
                canvas.create_text(label_size * x + label_size / 2, label_size * y + label_size / 2, text=f"#", font=("Arial", label_size), fill=rgbcolor)

canvas.pack()

#TODO to create animated video / GIF
'''
def animated_loop():
    root.after(100, animated_loop)

animated_loop()
'''

# run root
root.mainloop()