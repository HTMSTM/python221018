#demoFile2.py

# 파일 쓰기
f = open ("c:\\work\\demo.txt", "wt", encoding = "utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
print( f.read() )

print( f.tell() )

#리셋(다시 처음으로)
f.seek(0)
result = f.readlines()
print(result)

for item in result:
    #코드 보정
    print(item, end="")

print("--- 한줄씩 읽기 ---")
f.seek(0)
print( f.readline(), end="")
print( f.readline(), end="")


f.close()