# 사전
from tkinter import Menu


cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])  - 에러가 뜬다
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "b-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["b-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
# 간 손님
del cabinet["A-3"]
print(cabinet)
# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, values 쌍으로 출력
print(cabinet.items())
# 목욕탕 폐점
cabinet.clear()
print(cabinet)

#튜플 - 더이상 추가하지 않는 고정값
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3,}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
# 교집합( jave 와 python 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java.union(python))
# 차집합 (java 는 할 수 있지만 python은 할 수 없는 개발자)
print(java - python)
print(java.difference(python))
# 교육을 받고 pyhton 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)
# java를 잊어버렸다
java.remove("김태호")
print(java)

# Quiz)
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다!!! --")
 
