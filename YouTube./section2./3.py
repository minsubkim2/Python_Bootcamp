# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """ 
나는 소년이고,
파이썬은 쉬워요
"""
# """  포함해서 4줄이 찍힌다.
print(sentence3)

# 슬라이싱 - 필요한 정보만 가져온다
jumin = "930330-1234567" 

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])