# demoIfElse.py
# 블럭으로 주석처리 = ctrl + /
# score = int(input("점수를 입력 :"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

# # 딕셔너리
# d = {"apple":100, "kiwi":200}
# for k in d.keys():
#     print(k)

# for v in d.values():
#     print(v)

# for k, v in d.items():
#     print(k, v)

print("--= break ---")

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))
    print("item: ", i)
