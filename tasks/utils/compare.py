from task2.adaline import run_adaline
from task1.perceptron import run_perceptron

features = ['bill_length_mm', 'bill_depth_mm',
            'flipper_length_mm', 'gender', 'body_mass_g']

c1 = "Chinstrap"
c2 = "Gentoo"  # Adelie
ep = 1000
bs = 1
rate = 0.01
mse = 0.01


def compare_perceptron():
    for i in range(0, 5):
        for j in range(i + 1, 5):
            print(i, j, run_perceptron(c1, c2, features[i], features[j], ep, bs, rate))


def compare_adaline():
    for i in range(0, 5):
        for j in range(i + 1, 5):
            print(i, j, run_adaline(c1, c2, features[i], features[j], ep, bs, rate, mse))

