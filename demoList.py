# demoList.py
strA = "python is very powerful"

print( strA[0] )
print( strA[0:6] )
print( strA[:6] )
print( strA[-1] )
print( strA[-3:] )
print( strA[:-3] )
print( len(strA) )

print(" --- list 연습 ---")
colors = ["red", "blue", "green"]
print( colors )
print( len(colors) )
print( len( colors[1]) )
print( colors[0] )

colors.append("white");
print( colors )

colors.insert(1, "yellow")
print( colors )

print( colors.index("blue") )

colors += ["red"]
colors += "red"

print( colors )

colors.sort()
print( colors )

colors.reverse()
print( colors )

# 함수 정의

def calc(a, b):
    return a+b, a*b

# 호출
result = calc(5, 6)
print( result )

print("id:%s, name:%s" % ("kim", "김유신"))