import tkinter as tk
import tkinter.ttk as ttk

from PIL import Image, ImageTk
from confusion_matrix import gimme_conf_mat


def show_output(tp, tn, fp, fn, acc):
    # Creating tkinter window
    output_window = tk.Tk()
    output_window.title('Output')

    w = 900  # width for the Tk root
    h = 800  # height for the Tk root

    # get screen width and height
    ws = output_window.winfo_screenwidth()  # width of the screen
    hs = output_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    output_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Accuracy label
    ttk.Label(output_window, text="Accuracy :",
              font=("Roboto", 12)).grid(column=1, row=5, padx=10, pady=25)

    acc *= 100
    acc_txt = str(acc) + "0 %"

    # Accuracy number
    ttk.Label(output_window, text=acc_txt,
              font=("Roboto", 12)).grid(column=2, row=5, padx=10, pady=25)

    gimme_conf_mat(tp, tn, fp, fn)

    # Display confusion matrix image
    img = Image.open('conf_mat.png')
    display = ImageTk.PhotoImage(master=output_window, width=200, height=200, image=img)

    # Image Label
    ttk.Label(output_window,
              image=display).grid(column=2, row=15, padx=10, pady=25)

    # Program main loop
    output_window.mainloop()
