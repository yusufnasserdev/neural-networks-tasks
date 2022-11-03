import matplotlib.pyplot as plt
import seaborn as sea
from signumTask import mainlogic

"""
def visualization(w, maximum, minmum):
    data = read()
    selected_data = choose_class(data, class1, class2)
    sns.scatterplot(x="bill_length_mm", y="flipper_length_mm", data=selected_data, hue="species")
    plt.title("flipper_length_mm vs bill_length_mm", size=20, color="red")
    x0 = minmum
    x1 = maximum
    y1 = (-(w[2] + w[0]*x1) / w[1])
    y0 = (-(w[2] + w[0]*x0) / w[1])
    plt.plot([x0, x1], [y0, y1])
    plt.show()

"""
"""
y = -0.014*male100['Year']+38

plt.plot(male100['Year'],y,'r-',color = 'b')
ax = plt.gca() # gca stands for 'get current axis'
ax = male100.plot(x=0,y=1, kind ='scatter', color='g', label="Mens 100m", ax = ax)
female100.plot(x=0,y=1, kind ='scatter', color='r', label="Womens 100m", ax = ax)

"""
def visualize(train1,train2,x1,x2,w0,w1,w2):
    plt.figure('fig1')
    df0 = train1
    df1 = train2
    # df2 = df[df.cluster == 2]
    # sea.scatterplot(x1,x2,[df0[x1],df0[x2],df1[x1],df1[x2]], hue="species")
    plt.scatter(df0[x1], df0[x2], color='green')
    plt.scatter(df1[x1], df1[x2], color='blue')
    plt.xlabel(x1)
    plt.ylabel(x2)
    plt.show()
    x1a = 0
    x1b = (-w0) / w2
    x2a = (-w0) / w1
    x2b = 0
    print(x1b)
    print(x2a)
    point1 = [x1a, x1b]
    point2 = [x2a, x2b]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values)
    plt.show()
"""


"""
