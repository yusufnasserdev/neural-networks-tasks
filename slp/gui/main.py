import tkinter.font
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import tkinter as tk

# Creating tkinter window
window = tk.Tk()
window.title('Signum')

w = 800  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Features list
features = ['bill_length', 'bill_depth',
            'flipper_length', 'gender', 'body_mass']


# Feature 1 selected reaction
def f1_selected(event):
    selection = feature1_cb.get()
    selection_index = feature1_cb.current()
    feature1_cb.set("")
    feature1_cb.set(selection)
    new_features = features.copy()
    new_features.pop(selection_index)
    feature2_cb['values'] = new_features


# Feature 2 selected reaction
def f2_selected(event):
    selection = feature2_cb.get()
    selection_index = feature2_cb.current()
    feature2_cb.set("")
    feature2_cb.set(selection)
    new_features = features.copy()
    new_features.pop(selection_index)
    feature1_cb['values'] = new_features


# Feature 1 label
ttk.Label(window, text="Select feature 1 :",
          font=("Calibre", 15)).grid(column=0, row=5, padx=10, pady=25)

placeholder1 = tk.StringVar(value=' Feature 1')
feature1_cb = ttk.Combobox(window, width=25, state="readonly", font="16",
                           textvariable=placeholder1)

# Adding combobox drop down list
feature1_cb['values'] = features

feature1_cb.grid(column=1, row=5)
feature1_cb.bind("<<ComboboxSelected>>", f1_selected)

# Feature 2 label
ttk.Label(window, text="Select feature 2 :",
          font=("Times New Roman", 15)).grid(column=0, row=10, padx=10, pady=25)

placeholder2 = tk.StringVar(value=' Feature 2')
feature2_cb = ttk.Combobox(window, width=25, state="readonly", font="16",
                           textvariable=placeholder2)

feature2_cb.bind("<<ComboboxSelected>>", f2_selected)

# Adding combobox drop down list
feature2_cb['values'] = features

feature2_cb.grid(column=1, row=10)
feature2_cb.current()

window.mainloop()
