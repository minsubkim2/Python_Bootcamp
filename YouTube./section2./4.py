# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) #python 의 첫번째 값이 대문자이냐 확인 "Python is Amazing"
print(len(python)) # 문자열의 길이를 변환
print(python.replace("Python", "Java")) # Python 대신 Java 가 출력된다

index = python.index("n")
print(index) # python 문자에서 n이 몇번째인지 나온다 = 5(0부터 센다)
index = python.index("n", index + 1) # 이번엔 두번째 n을 찾는다
print(index)

print(python.find("Jave")) # index랑 같고 없는 문장을 쓰면 -1 이 나온다
# print(python.index("Jave")) #index는 오류가 뜬다

print(python.count("n")) #python 이란 문장에서 n이 총 몇번 나오는지

# 문자열 포멧
# print("a" + "b")
# print("a", "b")
print("나는 %d살입니다." % 20) #d 는 정수값만 든다
print("나는 %s을 좋아해요." % "파이썬") #s 문자열만 든다
print("Apple 은 %c로 시작해요." % "A") #c 문자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {2}색을 좋아해요.".format("파란", "빨간"))

