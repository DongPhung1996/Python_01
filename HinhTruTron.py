import math
def trutron(R,h):
    S_Day=R*2*math.pi
    S_XQ=2*R*h*math.pi
    V=S_Day*h
    if (R<0) or (h<0):
        print("ban nhap khong hop le") 
    else:
        print("Dien tich day la: ", S_Day)
        print("Dien tich XQ la: ", S_XQ)
        print("The tich la: ", V)
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
trutron(r,h)