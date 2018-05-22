import math
def tongsn(n):
    s=0
    while (n/10):
        s += n%10
        n = n/10
    return s+n;
N = int(input("Nhap vao so nguyen N: "))
print(tongsn(N))