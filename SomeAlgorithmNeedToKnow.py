import math
# Tìm số nhỏ nhất lớn hơn a và chia hết cho b
((a + b - 1) // b) * b

# Tỉnh tổng ước của 1 số
def tong_uoc(n):
    tong = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong

#Kiểm tra số nguyên tố
def prime(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#Liệt kê các số nguyên tố từ 1 tới n
n = int(input())
for i in range(1, n + 1):
    if prime(i):
        print(i, end = ' ' )
            
# Phân tích thành các thừa số nguyên tố
# CHÚ Ý: Khi số mũ của các thừa số cộng thêm 1 và cộng chúng lại sẽ ra số ước
def pt(n):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            #i : thửa số nguyên tố
            while n % i == 0:
                print(i, end = ' ')
                n //= i
        #N là số nguyên tố
        if n > 1:
            print(n)

# Kiểm tra số chính phương
def square(n):
    can = math.isqrt(n)
    return can * can == n
# can 3
def cube(n):
    can = int(math.pow(n, 1/3))
    return can ** 3 == n or ((can + 1) ** 3 == n)

# ước chung lớn nhất
def gcd(a, b):
    while b != 0:
        #Đổi a, b => b, a % b
        a. b = b, a  % b
    return a
# Bội chung nhỏ nhất
def lcm(a, b):
    return a * b // gcd(a, b)

# Tổ hợp chập k của n
def tohop(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Kiểm tra xem có phải số thuận nghịch hay không, số đối xứng
def palin(n):
    rev = 0
    temp = n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == temp

# Kiểm tra số hoàn hảo( có tổng số ước bằng với chính nó)
def perfect(n):
    tong = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n //i:
                tong += n // i
    return tong == n