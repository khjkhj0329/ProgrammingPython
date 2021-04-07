# #Quiz) 변수를 이용하여 다음 문장을 출력하시오
#
# # 변수명 : station
# # 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# # 출력 문장 : XX 행 열차가 들어오고 있습니다
#
# '''station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")'''
#
# #Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# # 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인을 하기로 했습니다
# # 아래 조건에 맞는 오프라인 모임 날자를 정해주는 프로그램을 작성하시오
# #
# # 조건1 : 랜덤으로 날짜를 뽑아야 함
# # 조건2 : 월별 날자는 다름을 감안하고 최소 일수인 28 이내로 정함
# # 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# #
# # (출력문 예제)
# # 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
#
# # from random import *
# # date = randint(4, 28)
# # print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")
#
# # Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# # 예) http://naver.com
# # 규칙1 : http:// 부분은 제외 => naver.com
# # 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성\
# #                 (nav)       (5)                 (1)         (!)
# # 예) 생성된 비밀번호 " nav51!"
#
# # url = "http://naver.com"
# # url = "http://youtube.com"
# # my_str = url.replace("http://", "") # 규칙1
# # #print(my_str)
# # my_str = my_str[:my_str.index(".")]
# # # # my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# # # print(my_str)
# # password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# # print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
#
# # Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# # 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# # 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# # 추첨 프로그램을 작성하시오.
# #
# # 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# # 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# # 조건3 : random 모듈의 shuffle 과 sample 을 활용
# #
# # (출력 예제)
# # -- 당첨자 발표 --
# # 치킨 담청자 : 1
# # 커피 담청자 : [2, 3, 4]
# # -- 축하합니다 --
# # (활용 예제)
# # from random import *
# # lst = [1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# # print(sample(lst, 1))
#
# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# # print(type(users))
# users = list(users)
# # print(type(users))
#
# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4) # 4명 중 1명은 치킨, 3명은 커피
#
# print(" -- 당첨자 발표 -- ")
# print("치킨 담청자 : {0}".format(winners[0]))
# print("커피 담청자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")

# id_number = "020316"
# year = id_number[0:2] #[:2], [-6:-4]
# month = id_number[2:6] #[2:] [-4]:
# print("생년 : " + year)
# print("월일 : " + month)
# print(int(year)*int(month))

# phone_number = "02-1234-5678"
# print(phone_number[0:2])        #[:2]
# print(phone_number[-4:])        #[:8]
#
#
# phone_number2 = "032-9876-4321"
# print(phone_number2[0:3])        #[:3]
# print(phone_number2[-4:])        #[:9]

# 3-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321

# 출력 예시
# 02 또는 032
# 5678 또는 4321
# phone_number = "02-1234-5678"
# phone_number2 = "032-9876-4321"
# print(phone_number[0:2])
# print(phone_number2[0:3])
# print(phone_number[8:])
# print(phone_number2[9:])

# print("------------2번째 시간-------------")
# # Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# # 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# # student_number = '2100' 또는 student_number = '2000'
# # <출력 예시>
# #
# # 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
# print("--------1번---------")
# student_number = "2100"
# ban = int(student_number[1:2])
# if (ban >= 7) or (0 > ban):
#     print("잘못 입력했습니다.")
# if(ban == 1)or(ban == 2):
#     print("{0}반 뉴미디어소프트웨어과".format(ban))
# elif(ban == 3)or(ban == 4):
#     print("{0}반 뉴미디어웹솔루션과".format(ban))
# elif(ban == 5)or(ban == 6):
#     print("{0}반 뉴미디어디자인과".format(ban))
#
#
# # Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# print("--------2번---------")
# def get_major(argument):
#     hakbun = "뉴미디어소프트웨어과 2"
#
#     major = hakbun[0:]
#     grade = hakbun[:0]
#     print(major, grade)
#
# get_major = get_major('2100')
#
#
# # <함수 호출>
# # grade, major = get_major('2100')
# # print(major, grade) #뉴미디어소프트웨어과 2
#
# # Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# print("--------3번---------")
# def average(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     avg = sum/len(num)
#     print(avg)
# average(10, 20, 30)
# average(4, 23)
# # <함수 호출>
# # print(average(10, 20, 30)) #20.0
# # print(average(4, 23)) #13.5
#
# # Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# # (소수 첫째자리까지 반올림)
# # * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# # 18.5 미만: 저체중
# # 18.5 이상 23 미만: 보통
# # 23 이상 25 미만: 과체중
# # 25 이상: 비만
# print("--------4번---------")
# def get_bmi(height, weight):
#     height = height * 0.01
#     calculate = weight / (height * height)
#     if calculate < 18.5:
#         print("저체중")
#     elif 18.5<=calculate<23.0:
#         print("보통")
#     elif 23.0 <= calculate < 25.0:
#         print("과제충")
#     else:
#         print("비만")
#     return calculate
#
# bmi=get_bmi(176, 69)
# print('%0.01f' % bmi)

# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3
print("----3번째 시간----")
# Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
# def n_sum(argument):
#     result = 0
#     if((len(str(argument))) <= 10):
#         for i in str(argument):
#             result = result + int(i)
#         return result
#     elif((len(str(argument))) >= 10):
#         print(-1)
# result = n_sum(10)
# print(result)
# result = n_sum(331)
# print(result)
# result = n_sum(408)
# print(result)
# result = n_sum(1000000000)
# print(result)
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(resuresult = n_sum(1000000000)
# # print(result)lt)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# def get_subway_fare(fare):
#     value = 0
#     if(10>fare):
#         print("720원")
#     elif(10<=fare<50):
#         print(value+100)
#     elif(50>fare):
#         print()
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
def get_three_six_nine(result):
    f = int(result/10);
    s = int(result%10);
    if(f%3==0 and s%3 == 0):
        if(f%3 == 0 or f != 0):
            print("짝")
            if(s%3 == 0 or s != 0):
                print("짝")
    elif(s%3 ==0 or s != 0):
        print("짝")
    else:
        print("없음")
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

# 'Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# 1. 함수의 이름을 정해준다.
# 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# 3. 리턴하는 것을 말해준다.
# 4. 출력 예시를 보여준다.
# 5. 내가 낸 문제의 답안을 제출한다.



