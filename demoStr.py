#demoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"

print( len(strA) )
print( len(strB) )
print( strA.capitalize() )
print( strA.upper() )
print( strA.count("p") )
print( strA.count("p", 7))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

u = " spam and ham "
result = u.strip()
print( u )
print( result )

u = "<<< spam and ham >>>"
result = u.strip("<> ")
print( u )
print( result )

result = result.replace("spam", "spam egg")
print( result )
lst = result.split()

print( lst )
print(" ---  다시 하나로 합치기 --- ")
print( ":)".join(lst))