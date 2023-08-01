a = str(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
c = []
d = []
b = str(input("输入:"))
for i in range(100):
    if a[int(i)] == b[int(i)]:
        print(str(i + 1) + "对")
        c.append(a[int(i)])
        print(c)
    else:
        print("错的:" + b[int(i-1)] + b[int(i)] + b[int(i+1)]+ "对的:" + a[int(i-1)] + a[int(i)] + a[int(i+1)])
        d.append(b[int(i)])
        print(d)
print(a in b)