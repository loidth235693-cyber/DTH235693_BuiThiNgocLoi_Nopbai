# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử n: "))

# Khai báo danh sách rỗng
M = []

# Nhập dãy n số thực
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

# Sắp xếp danh sách theo thứ tự giảm dần
M.sort(reverse=True)

# Xuất kết quả
print("\nDãy sau khi sắp xếp giảm dần là:")
print(M)
