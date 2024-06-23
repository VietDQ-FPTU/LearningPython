# cấu trúc tạo hàm: def + tên hàm + (tham số):
def tong(a, b):
    res = a + b
    return res

#Ta có thể viết hàm main bằng cách viết như thông thường nhưng thông thường chúng ta làm như sau
#if __name__ == '__main__':
    #code
    
# ta có thể gán trước giá trị cho tham số, nếu không chuyền tham số thì mặc định sẽ có giá trị được gán ban đầu
def infor(name, age = '10'):
    print(name, age)
infor('viet', '12') # dòng này in ra viet 12
infor('viet') #dòng nay in ra viet 10