#DemoDict.py

color = {"apple":"red", "banana":"yellow"}

print(color)
print( len(color))
print( color["apple"])

color["kiwi"] = "green"
print( color)

#반복문
for item in color.items():
    print(item)

for k, v in color.items():
    print(k, v)

device = {"아이폰":5, "아이패드":10, "타블렛":20}
print( device["아이폰"])

device["맥북"] = 15
print( device )

device["아이폰"]=6
del device["타블렛"]
print(device)

print("--- 참조만 복사 ---")

phone={"kim":"111", "lee":"222", "park":"3333"}
print( phone )
print( phone["kim"])
print( "kim" in phone )
print( "kang" in phone )


p = phone
p[ "kang"] = "123"
print( phone)
print( p )
print( id(phone), id(p))