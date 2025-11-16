def NhapDayTangDan():
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))
            if n <= 0:
                print("Vui lòng nhập số nguyên dương!")
                continue
            break
        except ValueError:
            print("Phải nhập số nguyên!")
    
    while True:
        lst = []
        print(f"\nNhập {n} số theo thứ tự tăng dần:")
        for i in range(n):
            x = int(input(f"Nhập số thứ {i+1}: "))
            lst.append(x)
        
        # Kiểm tra xem list có tăng dần không
        hop_le = True
        for i in range(1, n):
            if lst[i] <= lst[i - 1]:
                hop_le = False
                break
        
        if hop_le:
            print("\n✅ Dãy hợp lệ!")
            return lst
        else:
            print("\n❌ Dãy KHÔNG tăng dần. Vui lòng nhập lại!\n")

# --- Chạy chương trình ---
day = NhapDayTangDan()
print("Dãy số sau khi nhập xong là:", day)
