#demoOS.py
from os.path import *

print( abspath("python.exe") )
print( basename("c:\\work\\demo1.py"))
print(exists("c:\\python39\\python.exe"))

#운영체제 정보
from os import *
print("운영체제: ", name)

#파일 리스트
import glob
print(glob.glob("c:\\work\\*.py"))

