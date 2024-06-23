# range (start, stop, step): sinh ra một dãy sổ (start mặc định là 0 và step là 1 nên không có 2 cái này cũng được)
# for 'biến duyệt' in 'danh sách;
a = range(1, 10, 2)
for i in a:
    print(i, end = ' ')
    
# ta có thể viết nhanh thành
for i in range(10):
    print(i, end = ' ')
    
# Lưu ý: nếu i bị thay đổi trong vòng lặp for thì i sẽ quay lại giá trị cũ khi chạy hết 1 lần vòng lặp
for i in range(10):
    print(i, end = ' ')
    i += 2
    print(i, end = ' ')

# vòng khi chạy xong có thể dùng thêm else
for i in range(10):
    print(i, end = ' ')
else:
    print('hay roi')

# có thể dùng break để thoát vòng lặp hoặc continue để nhảy đến lần lặp tiếp theo
