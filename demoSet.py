# demoSet.py

a = {1,2,3,3}
b = {3,4,5,5,6}

print( a )
print( b )

print( type ( a ) )

print( a.union(b) )
print( b.union(a) )

print( a.intersection(b) )

print( a.difference(b) )

TT = ("kim", "김유신")
print("id : %s, name : %s" % TT)

T = set((1,2,3))
print (T)
print(type(T))

Y = list(T)
print(Y)
print( type(Y) )

U = tuple(Y)
print(U)
print( type(U))