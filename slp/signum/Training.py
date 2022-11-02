def training(x1, x2, t, w0, w1, w2, l_rate, b):
    res = w0 + x1 * w1 + x2 * w2
    if res >= 0:
        y_hat = 1
    else:
        y_hat = -1
    w0_new = 0
    if b:
        w0_new = w0 + l_rate * (t - y_hat) * 1
    w1_new = w1 + l_rate * (t - y_hat) * x1
    w2_new = w2 + l_rate * (t - y_hat) * x2
    return w0, w1_new, w2_new
