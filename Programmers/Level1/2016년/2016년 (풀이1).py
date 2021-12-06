def solution(a, b):
    sum=0
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,a-1):
        sum+=month[i]
    sum+=b
    return day[sum%7]