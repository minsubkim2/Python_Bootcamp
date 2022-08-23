# 애완동물을 소개해 주세요~  #변수 - 문장만 바꿔주면 간단히 바꿀수 있다
animai = "강아지"
name = "연탄이"
age = 4  #숫자를 문자로 만들어야 하기 때문에 str을 붙여야 한다
hobby = "산책"
is_adult = age >= 3

# print("우리짐 강아지의 이름은 연탄이예요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? True") ㅅ ㅅ
print("우리집 " + animai + "의 이름은 " + name + "이예요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# , 대신 사용 가능하며 이 경우 str은 사용하지 않아도 된다.
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

''' 주석  이렇게
하면
여러문장이
주석처리
된다'''

