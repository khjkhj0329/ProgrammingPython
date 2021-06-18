from information import Sick_part
def print_part():
    print('1. 강아지정보')
    print('2. 머리')
    print('3. 몸통')
    part = input('>> 메뉴를 선택하세요 : ')
    return part
def print_disease(disease_part):
    if disease_part == '1':
        pass
    elif disease_part == '2':
        print('1. 눈')
        print('2. 입')
        print('3. 귀')
        region = input('아픈 부위를 선택하세요 : ')
    elif disease_part == '3':
        print('1. 다리')
        print('2. 배')
        region = input('아픈 부위를 선택하세요 : ')
    return region

def main():
    disease = Sick_part()
    while True:
        selected_menu = print_part()
        if selected_menu == '1':
            pass
        elif selected_menu == '2': #머리
            part = print_disease('2')
            if part == '1': # 눈
                disease.check_eye()
            elif part == '2': # 입
                disease.check_mouth()
            elif part == '3': #귀
                disease.check_ear()
        elif selected_menu == '3': # 몸통
            part = print_disease('3')
            if part == '1': # 다리
                disease.check_leg()
            elif part == '2': # 배
                disease.check_stomach()

main()