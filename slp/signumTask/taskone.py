from mainlogic import logic


def send_input(c1, c2, f1, f2, epochs, rate, bias):
    print(bias)
    logic(c1, c2, f1, f2, epochs, bias, rate)
