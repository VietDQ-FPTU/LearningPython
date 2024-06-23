# list slicing:
# Cú pháp List[start, stop, step]
# Ví dụ
a = [2, 3, 54, 546, 345, 235435]
b = a[2: 5: 1]
print(b)
# Lật ngược list
c = a[::-1]
print(c)
# thay đổi list
print(a)
a[2: 5] = [0]
print(a)
a[2: 5] = [1, 2, 4]
print(a)
# chèn vào đầu
a[:0] = [434, 524, 54642]
print(a)
# chèn vào cuối
a[len(a):] = [0, 0, 0]
print(a)
# copy nhưng làm thế này nhanh hơn
d = a[:]
print(d)