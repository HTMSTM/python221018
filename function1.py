# function1.py

# 1. 함수정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)


# 2. 함수 호출
retValue = setValue(5)
print(retValue)

# 함수정의
def swap(x, y):
    return y, x

# 호출
result = swap(3, 4)
print(result)