# Hàm kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # chỉ cần kiểm tra đến căn bậc 2
        if n % i == 0:
            return False
    return True

# Nhập mảng số tự nhiên
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Phân loại
le = []
chan = []
nguyen_to = []
khong_nt = []

for x in M:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

    if la_nguyen_to(x):
        nguyen_to.append(x)
    else:
        khong_nt.append(x)

# Xuất kết quả
print("Dòng 1 (số lẻ):", le, f"→ Có {len(le)} số lẻ")
print("Dòng 2 (số chẵn):", chan, f"→ Có {len(chan)} số chẵn")
print("Dòng 3 (số nguyên tố):", nguyen_to)
print("Dòng 4 (không phải số nguyên tố):", khong_nt)
