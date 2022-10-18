# class1.py
#1) 클래스 형식 정의
class Person:
    #초기화 메소드
    def __init__(self):
        self.name = "default name"
    #인스터스 메소드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"
p2.name = "이순신"
p1.print()
p2.print()
