# list trong python có thể lưu lẫn lộn các kiểu phần tử
#1 Tạo list
a = []
b = [1, 'viet', 3.4]
print(b)
#2 có thể cắt các phần từ của 1 string vào 1 list
x = 'Ngan Kim Ngo'
y = list(x)
print(y)
#3 hàm len()
print(len(y))
#4 Truy cập thông qua chỉ số có hỗ trợ index âm. giá ở vị trí cuối cùng là -1
print(y[0])
print(y[-12])
#5 duyệt list
for i in range(0, len(y)):
    print(y[i], end = ' ')
for item in y:
    print(item, end = ' ')
#6 thay đổi giá trị phần tử
y[0] = 'viet'
#7 thêm phần tử vào list.
#append(): thêm vào cuối list
#insert(): thêm vào vị trí bất kì(nếu cho chỉ số vượt quá len() thì sẽ cho vào vị trí cuối)
v = []
v.append('ngan')
print(v)
v.insert(0, 'viet')
print(v)
#8 xóa phần tử khỏi list
#list.pop(): cho chỉ số, nếu ko cho thì xóa thằng cuối
b = [1, 2, 3, 4, 5]
b.pop(1)
print(b)
b.pop()
print(b)
# hoặc ta có thể del
del b[0]
print(b)
# xóa thông qua giá trị remove(): nếu ko có giá trị đó sẽ báo lỗi
# chỉ xóa giá trị đầu tiên tìm thấy
b.remove(3)
print(b)
# xóa mọi phần tử clear
b.clear()
print(b)
#9 sao chép list
n = [3, 23, 5]
m = n * 2
print(m)
# chứa 10 chiều phần tử 0
z = [0] * 10
print(z)
#10 kiểm tra có giá trị này trong list không
if 3 in n:
    print('YES')
#11 nối 2 list vào nhau
z.extend(m)
print(z)
#12 copy tại list mới giống với list cũ nhưng 2 list khác nhau
z = m.copy()
print(z)
#13 hàm count()
print(z.count(3))
#14 index(): trả về index của giá trị cho
# chi trả về index giá trị đầu tiên bắt gặp
print(z.index(3))
#15 lật ngược 1 list
z.reverse()
print(z)
#16 sắp xếp các phần tử trong list
z.sort()
print(z)