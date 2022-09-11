# 탈출문자
print("백문이 불여일견\n백견이 불여일타")
#\" \' : 문장 내에서 따음표
#저는 "나도코딩"입니다.
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")

#\\ : 문장 내에서 \
print("\\usr\\local\\bin\\python3")

#\r : 커서를 맨 앞으로 이동
print("Rad Apple\rPine") #Pine Apple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple") #Red     Apple

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#예0 http://naver.com
#규칙1: http:// 부분은 제외 규칙2 : 처음 만나는 점(.) 이후 부분은 제외
#규칙3 : 참은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 예) 생성된 비밀번호 : nav51

url = "http://naver.com"
my_str = url.replace("http://","") # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 처음부터 .직전까지만
# print(my_str)
password = my_str[:3] +str(len(my_str)) + str(my_str.count("e")) +"!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
