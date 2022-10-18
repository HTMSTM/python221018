from re import X
from unittest import result


def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("함수내부 X :", x)
    print("함수내부 X1:", x1)

wordlist = ["J", "A", "M"]
change(wordlist)
print("함수외부 x :", wordlist)


x = 1
def func(a):
    return a+x

print(func(1))

def func2(a):
    x = 2
    return a + x

print(func2(1))

# 디버깅 연습
def intersect(prelist, postlist):
    # 교집합 글자를 담기위한 리스트
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        # 특정 글자가 postlist에 있고, x가 result 에 없으면
        if (x in postlist) and (x not in result):
            result.append(x)
    return result

# 호출
print( intersect("HAM", "SPAM"))

def times(a=10, b=20):
    return a*b

print( times())
print( times(5))
print( times(b=5))


def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

def aaa(*ar):
    for x in ar:
        print(type(x))
        print(x)
        for y in x:
            print(type(y))
            print(y)

aaa("HAM", "EGG", "SPAM")