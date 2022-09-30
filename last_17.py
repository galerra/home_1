file = open('17_3.txt', 'r')
a = [int(i) for i in file]
m = -100000000000
k = 0
n = -100000000000
for i in a:
    if (i % 10) == 3 and i > m:
        m = i
print(m)


for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if (((x % 10 == 3) and (y % 10 != 3)) or ((x % 10 != 3) and (y % 10 == 3))) and (m ** 2 <= (x ** 2 + y ** 2)):
        k += 1
        if (x ** 2 + y ** 2) >= n:
            n = (x ** 2 + y ** 2)
print(k, n)
file.close()




