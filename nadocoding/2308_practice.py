# #숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# #문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9) #ㅋ이 9번
#
# #boolean 자료형
# #참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(not True)
# print(not False)
# print(not (5 > 10))
#
# #변수
# #애완동물을 소개해 주세요~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3
#
#
# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# #print(name + "는 "+str(age)+"살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 ", age,"살이며, ", hobby, "을 아주 좋아해요")
# #,쓰면 띄어쓰기
# print(name + "는 어른일까요?" + str(is_adult))
#
# #주석
# '''이렇게 하면 여러문장이
#  주석처리가
#  됩니다'''
# #연산자
# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2
#
# print(2**3) #2^3 = 8
# print(5%3) #나머지 구하기 2
# print(10%3) # 1 몫 구하기
# print(5//3) #1
# print(10//3) #3
#
# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True
#
# print(3 == 3) # True
# print(4 == 2) # False
# print(3 + 4 == 7) # True
#
# print(1 != 3) # True
# print(not(1 != 3)) # False
#
# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True
#
# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True
#
# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False)
#
# #간단한수식
# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2 # 16
# print(number)
#
# number %= 5 #1
# print(number)
#
# #숫자처리함수
# print(abs(-5)) # 5
# print(pow(4, 2)) # 4^2 = 4^4 =16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3
# print(round(4.99)) # 5
#
# from math import *
# print(floor(4.99)) # 내림, 4
# print(ceil(3.14)) # 올림, 4
# print(sqrt(16)) # 제곱근, 4
#
# #랜덤함수
# from random import *
#
# # print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# # print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
# # print(int(random() * 10) +1) # 1 ~ 10 이하으 임의의 값 생성
#
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# # print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
#
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
# # print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성
#
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
#
# #문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
#  파이썬은 쉬워요"""
# print(sentence3)
#
# #슬라이싱
# print("-------주민번호-------")
# jumin = "040329-4567890"
#
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # :은 0 부터 2 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
#
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지
#
# #문자열처리함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper())
# print(len(python)) # 글자의 수
# print(python.replace("Python", "Java")) #python을 java로 바꾼다
#
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java")) #원하는 글자찾기
# #print(python.index("Java"))
# print("hi")
#
# print(python.count("n"))
#
# #문자열포멧
# print("a" + "b")
# print("a", " b")
#
# #방법
# # print("나는 %d살입니다." % 20)
# # print("나는 %s를 좋아해요." % "파이썬")
# # print("Apple 은 %c로 시작해요." % "A")
# # # %s
# # print("나는 %d살입니다." % 20)
# # print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
#
# #방법 2
# # print("나는 {}살입니다." .format(20))
# # print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# # print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
#
# #방법 3
# # print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# # print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))
#
# #방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#
# #탈출문자
# # \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")
#
# #\" \' : 문자 내에서 따옴표
# #저는 "나도코딩"입니다
# # print('저는 "나도코딩"입니다.')
# # print("저는 \"나도코딩\"입니다.")
# # print("저는 \"나도코딩\"입니다.")
#
# # \\ : 문장 내에서 \
# # print("C:\nadocoding")
#
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
#
# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
#
# # \t : 탭
# print("Red\tApple")
#
# # 리스트 []
#
# # 지하철 칸별로 10명, 20명, 30명
# # subway1 = 10
# # subway1 = 20
# # subway1 = 30
#
# subway = [10, 20, 30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# # 조세호씨는 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))
#
# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)
#
# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)
#
# # 지하털에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
#
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
#
# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)
#
# # 모두 지우기
# num_list.clear()
# print(num_list)
#
# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)
#
# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)
#
# # 사전
# #cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet[100])
# #
# # print(cabinet.get(3))
# #print(cabinet.get(5))
# # print(cabinet.get(5))
# # print(cabinet.get(5, "사용가능"))
# # print("hi")
#
# # print(3 in cabinet)
# # print(5 in cabinet)
#
# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
#
# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)
#
# # 간 손님
# del cabinet["A-3"]
# print(cabinet)
#
# # key 들만 출력
# print(cabinet.keys())
#
# # value 들만 출력
# print(cabinet.values())
#
# # key, value 쌍으로 출력
# print(cabinet.items())
#
# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)
#
# # 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
#
# # menu.add("생선까스")
#
# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)
#
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)
#
# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
#
# # 교집합 (java 와 python 을 모두 할 수 있는 개발자
# print(java & python)
# print(java.intersection(python))
#
# # 합집합 (java 도 할 수 잇거나 python 할 수 있는 개발자
# print(java| python)
# print(java.union(python))
#
# # 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
#
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# # java 를 잊었어요
# java.remove("김태호")
# print(java)
#
# # 자료구조
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu. type(menu))
#
# menu = set(menu)
# print(menu. type(menu))
# if
weather = "비"
# if 조건:
#     실형 명령문
# weather = "맑아요"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")
# for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucke = ["아이언멘", "토르", "아이엠 그루트"]
# for customer in starbucke:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue와 break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#한줄 for문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#퀴즈5
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매친 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [0] 1번째 손님 (소요시간:15분)
# []  2번째 손님 (소요시간:50분)
# [0] 3번째 손님 (소요시간:5분)
# ...
# [] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분

# from random import *
# cnt = 0 # 총 답승 승객 수
# for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
#         print("[0] {0} 1번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#
# print("총 탑승 승객 : {0} 분".format(cnt))

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# open_account()

#전달값과 반환값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money
#
# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# print(balance)
#
# def withdraw(balance, money): # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.". format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
#
# def withdraw_nigth(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
#
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
#
# commission, balance = withdraw_nigth(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 기본값
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))
#
# profile("유재석")
# profile("김태호")

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호", )

# 가변인자
# def proflie(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
#

#지역변수와 전역변수
# gun = 10
#
# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#
# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구한느 프로그램을 작성하시오
#
# * 표준 체중 : 각 개인의 키에 적당한 체중
#
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
#
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 157cm 남자의 표준 체중은 67.8kg 입니다.

def std_weight(height, gender): # 키는 m 단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm 남자의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))



