import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as f
from tkinter import messagebox

from gui.connector import input_adaline, input_perceptron, input_backpropagation, input_bonus

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

        self.task = task

        # Creating tkinter window
        window = tk.Tk()
        window.title('Task ' + str(self.task))

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

        m_font = f.Font(family="Calibri", size=12)

        if self.task == 3 or self.task == 4:
            # Number of hidden layers label
            ttk.Label(window, text="Hidden Layers # :",
                      font=m_font).grid(column=1, row=5, padx=40, pady=25)

            # Number of hidden layers entry
            hl_placeholder = tk.StringVar(value='3')
            self.layers_no = tk.Entry(window, width=25, font=m_font, textvariable=hl_placeholder)
            self.layers_no.grid(column=2, row=5)

            # Number of neurons label
            ttk.Label(window, text="Neurons # :",
                      font=m_font).grid(column=3, row=5, padx=40, pady=25)

            # Number of neurons in each hidden layer entry
            neurons_placeholder = tk.StringVar(value='3,2,4')
            self.neurons_no = tk.Entry(window, width=25, font=m_font, textvariable=neurons_placeholder)
            self.neurons_no.grid(column=4, row=5)

        elif self.task == 1 or self.task == 2:
            # Feature 1 label
            ttk.Label(window, text="Select feature 1 :",
                      font=m_font).grid(column=0, row=5, padx=40, pady=25)

            f1_placeholder = tk.StringVar(value=' Feature 1')
            self.feature1_cb = ttk.Combobox(window, width=25, state="readonly", font=m_font,
                                            textvariable=f1_placeholder)

            # Adding combobox drop down list
            self.feature1_cb['values'] = features

            self.feature1_cb.grid(column=1, row=5)
            self.feature1_cb.current()

            # Setting the selection listener
            self.feature1_cb.bind("<<ComboboxSelected>>", self.f1_selected)

            # Feature 2 label
            ttk.Label(window, text="Select feature 2 :",
                      font=m_font).grid(column=0, row=10, padx=40, pady=25)

            f2_placeholder = tk.StringVar(value=' Feature 2')
            self.feature2_cb = ttk.Combobox(window, width=25, state="readonly", font=m_font,
                                            textvariable=f2_placeholder)

            # Adding combobox drop down list
            self.feature2_cb['values'] = features

            self.feature2_cb.grid(column=1, row=10)
            self.feature2_cb.current()

            # Setting the selection listener
            self.feature2_cb.bind("<<ComboboxSelected>>", self.f2_selected)

            # Class 1 label
            ttk.Label(window, text="Select class 1 :",
                      font=m_font).grid(column=2, row=5, padx=40, pady=25)

            c1_placeholder = tk.StringVar(value=' Class 1')
            self.class1_cb = ttk.Combobox(window, width=25, state="readonly", font=m_font,
                                          textvariable=c1_placeholder)

            # Adding combobox drop down list
            self.class1_cb['values'] = classes

            self.class1_cb.grid(column=3, row=5)
            self.class1_cb.current()

            # Setting the selection listener
            self.class1_cb.bind("<<ComboboxSelected>>", self.c1_selected)

            # Class 2 label
            ttk.Label(window, text="Select class 2 :",
                      font=m_font).grid(column=2, row=10, padx=40, pady=25)

            c2_placeholder = tk.StringVar(value=' Class 2')
            self.class2_cb = ttk.Combobox(window, width=25, state="readonly", font=m_font,
                                          textvariable=c2_placeholder)

            # Adding combobox drop down list
            self.class2_cb['values'] = classes

            self.class2_cb.grid(column=3, row=10)
            self.class2_cb.current()

            # Setting the selection listener
            self.class2_cb.bind("<<ComboboxSelected>>", self.c2_selected)

        # Learning rate label
        ttk.Label(window, text="Enter learning rate :",
                  font=m_font).grid(column=1, row=15, padx=40, pady=25)

        # Learning rate entry
        lr_placeholder = tk.StringVar(value='0.01')
        self.learning_rate = tk.Entry(window, width=25, font=m_font, textvariable=lr_placeholder)
        self.learning_rate.grid(column=2, row=15)

        # Number of epochs label
        ttk.Label(window, text="Number of epochs :",
                  font=m_font).grid(column=1, row=20, padx=40, pady=25)

        # Number of epochs entry
        ne_placeholder = tk.StringVar(value='1000')
        self.epochs_no = tk.Entry(window, width=25, font=m_font, textvariable=ne_placeholder)
        self.epochs_no.grid(column=2, row=20)

        # Bias label
        ttk.Label(window, text="Bias (if checked) :",
                  font=m_font).grid(column=1, row=30, padx=40, pady=25)

        # Bias checkbox
        self.bs = tk.IntVar()
        bias_check = tk.Checkbutton(window, variable=self.bs, font=12)
        bias_check.grid(column=2, row=30)

        if self.task == 2:
            # MSE threshold label
            ttk.Label(window, text="Enter MSE Threshold :",
                      font=m_font).grid(column=1, row=35, padx=40, pady=25)

            # MSE threshold entry
            mse_placeholder = tk.StringVar(value='0.01')
            self.mse_threshold = tk.Entry(window, width=25, font=m_font, textvariable=mse_placeholder)
            self.mse_threshold.grid(column=2, row=35)

        if self.task == 3 or self.task == 4:
            # Activation function label
            ttk.Label(window, text="Activation Function :",
                      font=m_font).grid(column=1, row=35, padx=40, pady=25)
            self.active = tk.IntVar(value=1)
            r1 = tk.Radiobutton(window, text="Sigmoid", value=1, variable=self.active)
            r1.grid(column=2, row=35)
            r2 = tk.Radiobutton(window, text="Hyperbolic", value=2, variable=self.active)
            r2.grid(column=3, row=35)

        # Run button
        run = tk.Button(window, text='Run',
                        font=m_font, command=self.run, relief='raised', bg='#FFFFFF')
        run.grid(column=4, row=40)

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
            if int(self.epochs_no.get().strip()) > 0:
                return True
            else:
                messagebox.showerror(title="Error", message="Number of epochs have to be bigger than 0")
                return False
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid epochs number")
            return False

    def valid_rate(self):
        try:
            if float(self.learning_rate.get().strip()) > 0:
                return True
            else:
                messagebox.showerror(title="Error", message="Learning rate have to be bigger than 0")
                return False
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid learning rate")
            return False

    def valid_classes(self):
        if self.task == 1 or self.task == 2:
            if self.class1_cb.get() == " Class 1" or self.class2_cb.get() == " Class 2":
                messagebox.showerror(title="Error", message="Please select both classes")
                return False
        return True

    def valid_features(self):
        if self.task == 1 or self.task == 2:
            if self.feature1_cb.get() == " Feature 1" or self.feature2_cb.get() == " Feature 2":
                messagebox.showerror(title="Error", message="Please select both features")
                return False
        return True

    def valid_mse(self):
        if self.task != 2:
            return True

        try:
            if float(self.mse_threshold.get().strip()) > 0:
                return True
            else:
                messagebox.showerror(title="Error", message="MSE threshold have to be bigger than 0")
                return False
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid MSE threshold")
            return False

    def valid_neurons(self):
        if self.task != 3 and self.task != 4:
            return True

        try:
            neurons_list = self.neurons_no.get().strip().split(',')

            if len(neurons_list) != int(self.layers_no.get().strip()):
                messagebox.showerror(title="Error", message="Please make sure that all the hidden layers have a "
                                                            "neurons number")
                return False

            for neuron in neurons_list:
                try:
                    return int(neuron) > 0
                except ValueError:
                    messagebox.showerror(title="Error", message="Please make sure that all neurons are valid")
                    return False

        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid neurons sequence separated by commas "
                                                        "and no spaces in between")
            return False

    def valid_layers(self):
        if self.task != 3 and self.task != 4:
            return True

        try:
            int(self.layers_no.get().strip())
            return True
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid layers number")
            return False

    def valid_input(self):
        return self.valid_features() and \
               self.valid_classes() and \
               self.valid_rate() and \
               self.valid_epochs() and \
               self.valid_mse() and \
               self.valid_layers() and \
               self.valid_neurons()

    def run(self):

        if self.valid_input():
            epochs = int(self.epochs_no.get().strip())
            rate = float(self.learning_rate.get().strip())

            if self.task == 1 or self.task == 2:
                f2 = self.feature2_cb.get().strip()
                c1 = self.class1_cb.get().strip()
                c2 = self.class2_cb.get().strip()
                f1 = self.feature1_cb.get().strip()

                if self.task == 1:
                    input_perceptron(c1, c2, f1, f2, epochs, self.bs.get(), rate)
                elif self.task == 2:
                    mse = float(self.mse_threshold.get().strip())
                    input_adaline(c1, c2, f1, f2, epochs, self.bs.get(), rate, mse)

            elif self.task == 3 or self.task == 4:
                layers = int(self.layers_no.get().strip())
                neurons = self.neurons_no.get().strip().split(',')
                for i in range(len(neurons)):
                    neurons[i] = int(neurons[i])

                if self.task == 3:
                    input_backpropagation(layers, neurons, epochs, self.active.get(), self.bs.get(), rate)
                elif self.task == 4:
                    input_bonus(layers, neurons, epochs, self.active.get(), self.bs.get(), rate)
