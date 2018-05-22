import math
def sotien(n):
    a = [10,3,3,1]
    for i in a[:]:
        so_to = n/i
        print("Tien",i,"d co" , so_to, "to")
        n=n%i 
N = int(input("nhap vao so tien: "))
sotien(N)
    