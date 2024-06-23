#Lý thuyết đồng dư
#(A + B) % C = ((A % C) + (B % C)) % C
#(A - B) % C = ((A % C) - (B % C)) % C
#(A * B) % C = ((A % C) * (B % C)) % C
#(A / B) % C = ((A % C) * (B^-1 % C)) % C

#Tính n! chia dư cho 10^9 + 7
#Khi bài toán yêu cầu chia dư kết quả cho 1 số nào đo => Tính đến đêu chia dư đến đó
#TÍnh a^b chi dư cho c

a, b, c = map(int, input().split())
#print((a ** b) % c)
res = 1
for i in range(b):
    res *= a
    res %= c
print(res)
