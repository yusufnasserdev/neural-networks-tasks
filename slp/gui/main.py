import tkinter as tk
import tkinter.ttk as ttk

# Creating tkinter window
window = tk.Tk()
window.title('Signum')

w = 930  # width for the Tk root
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
features = [' bill_length', ' bill_depth',
            ' flipper_length', ' gender', ' body_mass']

classes = [' Adelie', ' Gentoo', ' Chinstrap']


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


# Class 1 selected reaction
def c1_selected(event):
    selection = class1_cb.get()
    selection_index = class1_cb.current()
    class1_cb.set("")
    class1_cb.set(selection)
    new_classes = classes.copy()
    new_classes.pop(selection_index)
    class2_cb['values'] = new_classes


# Class 2 selected reaction
def c2_selected(event):
    selection = class2_cb.get()
    selection_index = class2_cb.current()
    class2_cb.set("")
    class2_cb.set(selection)
    new_classes = classes.copy()
    new_classes.pop(selection_index)
    class1_cb['values'] = new_classes


# Feature 1 label
ttk.Label(window, text="Select feature 1 :",
          font=("Roboto", 12)).grid(column=0, row=5, padx=10, pady=25)

f1_placeholder = tk.StringVar(value=' Feature 1')
feature1_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                           textvariable=f1_placeholder)

# Adding combobox drop down list
feature1_cb['values'] = features

feature1_cb.grid(column=1, row=5)
feature1_cb.current()

# Setting the selection listener
feature1_cb.bind("<<ComboboxSelected>>", f1_selected)

# Feature 2 label
ttk.Label(window, text="Select feature 2 :",
          font=("Times New Roman", 12)).grid(column=0, row=10, padx=10, pady=25)

f2_placeholder = tk.StringVar(value=' Feature 2')
feature2_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                           textvariable=f2_placeholder)

# Adding combobox drop down list
feature2_cb['values'] = features

feature2_cb.grid(column=1, row=10)
feature2_cb.current()

# Setting the selection listener
feature2_cb.bind("<<ComboboxSelected>>", f2_selected)

# Class 1 label
ttk.Label(window, text="Select class 1 :",
          font=("Roboto", 12)).grid(column=2, row=5, padx=40, pady=25)

c1_placeholder = tk.StringVar(value=' Class 1')
class1_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                         textvariable=c1_placeholder)

# Adding combobox drop down list
class1_cb['values'] = classes

class1_cb.grid(column=3, row=5)
class1_cb.current()

# Setting the selection listener
class1_cb.bind("<<ComboboxSelected>>", c1_selected)

# Class 2 label
ttk.Label(window, text="Select class 2 :",
          font=("Roboto", 12)).grid(column=2, row=10, padx=40, pady=25)

c2_placeholder = tk.StringVar(value=' Class 2')
class2_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                         textvariable=c2_placeholder)

# Adding combobox drop down list
class2_cb['values'] = classes

class2_cb.grid(column=3, row=10)
class2_cb.current()

# Setting the selection listener
class2_cb.bind("<<ComboboxSelected>>", c2_selected)

# Learning rate label
ttk.Label(window, text="Enter learning rate :",
          font=("Roboto", 12)).grid(column=1, row=15, padx=10, pady=25)

# Learning rate entry
lr_placeholder = tk.StringVar(value=' Learning rate')
learning_rate = tk.Entry(window, width=25, font=("Roboto", 12), textvariable=lr_placeholder)
learning_rate.grid(column=2, row=15)

# Number of epochs label
ttk.Label(window, text="Number of epochs :",
          font=("Roboto", 12)).grid(column=1, row=20, padx=10, pady=25)

# Number of epochs entry
ne_placeholder = tk.StringVar(value=' # of epochs')
epochs_no = tk.Entry(window, width=25, font=("Roboto", 12), textvariable=ne_placeholder)
epochs_no.grid(column=2, row=20)

# Bias label
ttk.Label(window, text="Bias (if checked) :",
          font=("Roboto", 12)).grid(column=1, row=30, padx=10, pady=25)

# Bias checkbox
bias = tk.IntVar()
bias_check = tk.Checkbutton(window, variable=bias, font=12)
bias_check.grid(column=2, row=30)

# Program main loop
window.mainloop()