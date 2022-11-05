def testing(x1, x2, t, w0, w1, w2):
    res = w0 + x1 * w1 + x2 * w2
    if res >= 0:
        y_hat = 1
    else:
        y_hat = -1
    return y_hat
