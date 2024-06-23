# Cú pháp
# lambda tham số: return

func = lambda x, y, z : x + y + z
print(func(100, 200, 300))
print((lambda x, y, z : x + y - z)(100, 200, 300))

sum = lambda x, y = 10, z = 20 : x + y + z
print(sum(20))
# lambda and map() áp dụng lên các phần từ
a = [1 , 2, 3, 4, 5]
b = list(map(lambda x : x ** 2, a))
print(b)
# lambda and filter() trả về giá trị true false trong list
c = list(filter(lambda x : x > 2, a))
print(c)
# áp dụng thêm với if else
findMax = lambda x, y : x if x > y else y
print(findMax(100, 200))