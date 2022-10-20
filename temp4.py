#temp4.py

import time

print( time.time() )
print( time.time() )
print( time.localtime() )
print( time.gmtime() )

import random
print( random.random())
print( random.random())

#리스트 컴프리헨션(리스트 내장)
print( [random.randrange(20) for i in range(10)])
print( [random.randrange(20) for i in range(10)])

print("--- 샘플링 ---")
print( random.sample(range(20), 10))
print( random.sample(range(20), 10))