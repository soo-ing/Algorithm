def solution(phone_number):
    for i in range(len(phone_number)-4):
        phone_number=phone_number.replace(phone_number[i],'*',1)

    return phone_number

"""
replace() 함수 사용
replace(old, new, count) / old: 기존 값, new: 바꿀 값, count: 바꿀 횟수

"""