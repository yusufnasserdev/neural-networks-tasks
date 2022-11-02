def training(x1,x2,t,w0,w1,w2,L,b):
    res=w0+x1*w1+x2*w2;
    if(res>=0):
        yhat=1
    else:
        yhat=-1
    w0new=0
    if(b==True):
        w0new=w0+L*(t-yhat)*1
    w1new=w1+L*(t-yhat)*x1
    w2new=w2+L*(t-yhat)*x2
    return w0,w1new,w2new
