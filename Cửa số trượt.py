n = int(input())
a = list(map(int, input().split()))
k = int(input())
tong = sum(a[:k]) #Tổng k số từ phần tử 0
for i in range(1, n - k + 1):
    tong = tong - a[i - 1] + a[i + k - 1]
    print(tong, end = ' ')