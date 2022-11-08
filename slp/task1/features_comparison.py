from perceptron import run

features = ['bill_length_mm', 'bill_depth_mm',
            'flipper_length_mm', 'gender', 'body_mass_g']

c1 = "Chinstrap"
c2 = "Gentoo"  # Adelie
ep = 1000
bs = 1
rate = 0.01

for i in range(0, 5):
    for j in range(i + 1, 5):
        print(i, j, run(c1, c2, features[i], features[j], ep, bs, rate))
