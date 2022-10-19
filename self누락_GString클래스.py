#전역변수
str = "Not Class Member"

class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = ""
        print(" class init ")
    def __del__(self):
        print(" class del ") 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 전역변수 str을 보게 됨
        print(str)
        # 멤버변수 str을 보게 됨
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
