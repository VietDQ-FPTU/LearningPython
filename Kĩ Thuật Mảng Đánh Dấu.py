# kỹ thuật mảng đánh dấu(để biết số phần từ trùng nhau lặp lại bao nhiêu lần)
a = [1, 2, 3, 4, 2, 5, 2, 2, 1, 9, 5, 3, 7]
cnt = [0] * 10000001
for x in a:
    cnt[x] += 1
# duyệt theo thứ tự gặp phải
for x in a:
    if cnt[x] != 0:
        #print(x, cnt[x])
        #cnt[x] = 0
# duyêt theo từ bé đến lớn
l, r = min(a), max(a)
for i in range(l, r + 1):
    if cnt[i] != 0:
        print(i, cnt[x])