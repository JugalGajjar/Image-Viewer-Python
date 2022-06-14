from tkinter import *
from PIL import Image, ImageTk

def button_back():
    global my_label, back, next
    global current

    if current >= 0:
        current -= 1

        if current == 0:
            back = Button(root, text="Back", padx=30, pady=15, borderwidth=3, state=DISABLED)
            back.grid(row=1, column=0, pady=5)
        if current != (len(image_list)-1):
            next = Button(root, text="Next", padx=30, pady=15, borderwidth=3, command=button_next)
            next.grid(row=1, column=2, pady=5)

        my_label.grid_forget()

        my_label = Label(image=image_list[current])
        my_label.grid(row=0, column=0, columnspan=3)

        status = Label(root, text="Image {} of {}".format(current+1, len(image_list)))
        status.grid(row=2, column=2)

def button_next():
    global my_label, back, next
    global current

    if current <= 4:
        current += 1

        if current == (len(image_list)-1):
            next = Button(root, text="Next", padx=30, pady=15, borderwidth=3, state=DISABLED)
            next.grid(row=1, column=2, pady=5)
        if current != 0:
            back = Button(root, text="Back", padx=30, pady=15, borderwidth=3, command=button_back)
            back.grid(row=1, column=0, pady=5)

        my_label.grid_forget()

        my_label = Label(image=image_list[current])
        my_label.grid(row=0, column=0, columnspan=3)

        status = Label(root, text="Image {} of {}".format(current+1, len(image_list)))
        status.grid(row=2, column=2)

root = Tk()
root.title("My Image Viewer")
root.iconbitmap("Icon.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Images\\1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Images\\2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images\\3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images\\4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images\\5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("Images\\6.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

current = 0

back = Button(root, text="Back", padx=30, pady=15, borderwidth=3, command=button_back, state=DISABLED)
exit = Button(root, text="Exit", padx=30, pady=15, borderwidth=3, command=root.quit)
next = Button(root, text="Next", padx=30, pady=15, borderwidth=3, command=button_next)

back.grid(row=1, column=0, pady=5)
next.grid(row=1, column=2, pady=5)
exit.grid(row=1, column=1, pady=5)

status = Label(root, text="Image {} of {}".format(current+1, len(image_list)))
status.grid(row=2, column=2)

root.mainloop()