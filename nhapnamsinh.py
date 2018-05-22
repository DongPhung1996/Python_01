#Chuong trinh : Nhap nam sinh Xuat tuoi
import time
x=time.localtime()
print (x[0])
def Xuat_tuoi(Namsinh):
  x=time.localtime()
  a=x[0]-Namsinh
  if a==0:
      print ("Tuoi cua ban la :",a+1)
  elif (a<0):
       print ("Tuoi nay chua ton tai")
  else:
       print ("Tuoi cua ban la :",a)
NS=int(input("Nhap nam sinh : "))
Xuat_tuoi(NS)