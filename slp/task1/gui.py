import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from preprocessing import report
from connector import send_input

# Lists used in combo-boxes

features = [' bill_length_mm', ' bill_depth_mm',
            ' flipper_length_mm', ' gender', ' body_mass_g']

classes = [' Adelie', ' Gentoo', ' Chinstrap']


def combobox_listener(combo1, combo2, event, new_list):
    # Getting both feature combo-boxes selections
    selection1 = combo1.get()
    selection2 = combo2.get()

    # Setting feature1 combobox selection
    combo1.set("")
    combo1.set(selection1)

    # Giving up the focus
    event.widget.master.focus_set()

    try:
        s2_index = new_list.index(selection2)
        new_list.pop(s2_index)
    except ValueError:
        pass

    s1_index = new_list.index(selection1)
    new_list.pop(s1_index)

    # Setting the new combobox values
    combo1['values'] = new_list
    combo2['values'] = new_list


class GUI:
    def __init__(self, task):

        # Creating tkinter window
        window = tk.Tk()
        window.title('Task One')

        w = 930  # width for the Tk root
        h = 650  # height for the Tk root

        # get screen width and height
        width = window.winfo_screenwidth()  # width of the screen
        height = window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (width / 2) - (w / 2)
        y = (height / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Feature 1 label
        ttk.Label(window, text="Select feature 1 :",
                  font=("Roboto", 12)).grid(column=0, row=5, padx=10, pady=25)

        f1_placeholder = tk.StringVar(value=' Feature 1')
        self.feature1_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                                        textvariable=f1_placeholder)

        # Adding combobox drop down list
        self.feature1_cb['values'] = features

        self.feature1_cb.grid(column=1, row=5)
        self.feature1_cb.current()

        # Setting the selection listener
        self.feature1_cb.bind("<<ComboboxSelected>>", self.f1_selected)

        # Feature 2 label
        ttk.Label(window, text="Select feature 2 :",
                  font=("Roboto", 12)).grid(column=0, row=10, padx=10, pady=25)

        f2_placeholder = tk.StringVar(value=' Feature 2')
        self.feature2_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                                        textvariable=f2_placeholder)

        # Adding combobox drop down list
        self.feature2_cb['values'] = features

        self.feature2_cb.grid(column=1, row=10)
        self.feature2_cb.current()

        # Setting the selection listener
        self.feature2_cb.bind("<<ComboboxSelected>>", self.f2_selected)

        # Class 1 label
        ttk.Label(window, text="Select class 1 :",
                  font=("Roboto", 12)).grid(column=2, row=5, padx=40, pady=25)

        c1_placeholder = tk.StringVar(value=' Class 1')
        self.class1_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                                      textvariable=c1_placeholder)

        # Adding combobox drop down list
        self.class1_cb['values'] = classes

        self.class1_cb.grid(column=3, row=5)
        self.class1_cb.current()

        # Setting the selection listener
        self.class1_cb.bind("<<ComboboxSelected>>", self.c1_selected)

        # Class 2 label
        ttk.Label(window, text="Select class 2 :",
                  font=("Roboto", 12)).grid(column=2, row=10, padx=40, pady=25)

        c2_placeholder = tk.StringVar(value=' Class 2')
        self.class2_cb = ttk.Combobox(window, width=25, state="readonly", font=("Roboto", 12),
                                      textvariable=c2_placeholder)

        # Adding combobox drop down list
        self.class2_cb['values'] = classes

        self.class2_cb.grid(column=3, row=10)
        self.class2_cb.current()

        # Setting the selection listener
        self.class2_cb.bind("<<ComboboxSelected>>", self.c2_selected)

        # Learning rate label
        ttk.Label(window, text="Enter learning rate :",
                  font=("Roboto", 12)).grid(column=1, row=15, padx=10, pady=25)

        # Learning rate entry
        lr_placeholder = tk.StringVar(value=' Learning rate')
        self.learning_rate = tk.Entry(window, width=25, font=("Roboto", 12), textvariable=lr_placeholder)
        self.learning_rate.grid(column=2, row=15)

        # Number of epochs label
        ttk.Label(window, text="Number of epochs :",
                  font=("Roboto", 12)).grid(column=1, row=20, padx=10, pady=25)

        # Number of epochs entry
        ne_placeholder = tk.StringVar(value=' # of epochs')
        self.epochs_no = tk.Entry(window, width=25, font=("Roboto", 12), textvariable=ne_placeholder)
        self.epochs_no.grid(column=2, row=20)

        # Bias label
        ttk.Label(window, text="Bias (if checked) :",
                  font=("Roboto", 12)).grid(column=1, row=30, padx=10, pady=25)

        # Bias checkbox
        self.bs = tk.IntVar()
        bias_check = tk.Checkbutton(window, variable=self.bs, font=12)
        bias_check.grid(column=2, row=30)

        # Run button
        run = tk.Button(window, text='Run',
                        font=("Roboto", 12), command=self.run, relief='raised', bg='#FFFFFF')
        run.grid(column=3, row=30)

        # Program main loop
        window.mainloop()

    # Feature 1 selected reaction
    def f1_selected(self, event):
        combobox_listener(self.feature1_cb, self.feature2_cb, event, features.copy())

    # Feature 2 selected reaction
    def f2_selected(self, event):
        combobox_listener(self.feature2_cb, self.feature1_cb, event, features.copy())

    # Class 1 selected reaction
    def c1_selected(self, event):
        combobox_listener(self.class1_cb, self.class2_cb, event, classes.copy())

    # Class 2 selected reaction
    def c2_selected(self, event):
        combobox_listener(self.class2_cb, self.class1_cb, event, classes.copy())

    def valid_epochs(self):
        try:
            int(self.epochs_no.get().strip())
            return True
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid epochs number")
            return False

    def valid_rate(self):
        try:
            float(self.learning_rate.get().strip())
            return True
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid learning rate")
            return False

    def valid_classes(self):
        if self.class1_cb.get() == " Class 1" or self.class2_cb.get() == " Class 2":
            messagebox.showerror(title="Error", message="Please select both classes")
            return False
        return True

    def valid_features(self):
        if self.feature1_cb.get() == " Feature 1" or self.feature2_cb.get() == " Feature 2":
            messagebox.showerror(title="Error", message="Please select both features")
            return False
        return True

    def valid_input(self):
        return self.valid_features() and self.valid_classes() and self.valid_rate() and self.valid_epochs()

    def run(self):
        if self.valid_input():
            c1 = self.class1_cb.get().strip()
            c2 = self.class2_cb.get().strip()
            f1 = self.feature1_cb.get().strip()
            f2 = self.feature2_cb.get().strip()
            epochs = int(self.epochs_no.get().strip())
            rate = float(self.learning_rate.get().strip())
            send_input(c1, c2, f1, f2, epochs, self.bs.get(), rate)
