from math import *

#Prefix sum
#Cho mảng A[] có nhiều N phần tử, yêu cầu truy vấn tổng các phần tử từ chỉ số l tới chỉ số r của mảng
#Chú ý khi l = 0
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    F = [0] * n
    F[0] = a [0]
    for i in range(1, n):
        F[i] = F[i - 1] + a[i]
    l, r = 3, 5
    print(F[r] - F[l - 1])