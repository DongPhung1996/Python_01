import math
def tinhbt(x):
    y1 = x*x + math.pow(x,1.5) + x*3 + 1
    y2 = (math.sin(math.pi*x*x) + math.sqrt(x*x + 1))/(math.exp(2*x)+math.cos((math.pi/4)*x))
    print("Y1 = ", y1)
    print("Y2 = ", y2)
x = float(input("Moi ban nhap gia tri cua X: "))
tinhbt(x)
    