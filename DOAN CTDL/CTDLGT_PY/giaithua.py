#Hàm tính giai thừa của 1 số
def giaithua(m):
    if m == 0:
        return 1
    else:
        return m * giaithua(m - 1)

print(giaithua(4))