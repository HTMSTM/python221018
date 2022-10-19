#demoFile.py

url = "http://www.ycampus.com/?page=" + str(1)
print(url)

for x in range(1, 6):
    print(x, "*", x, "=", x*x)

print("---왼쪽 정렬---")
for x in range(1, 6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000))
