#demoRE.py
import re

#print( dir(re) )

#정규표현식(특정한 규칙)
result = re.search("[0-9]*th", "35th")
print( result )
print( result.group())
#매칭 오브젝트
result = re.match("[0-9]*th", "35th")
print( result )
print( result.group() )

print("--- search 함수 사용 ---")
print( bool(re.search("apple", "this is apple")))
print( bool(re.match("apple", "this is apple")))

result = re.search("\d{4}", "올해는 2022년 입니다.")
print( result.group() )

result = re.search("\d{5}", "우리 동네는 52100번지입니다.")
print( result.group() )

