def testing(x1,x2,t,w0,w1,w2):
    res=w0+x1*w1+x2*w2
    if(res>=0):
        yhat=1
    else:
        yhat=-1
    return yhat==t