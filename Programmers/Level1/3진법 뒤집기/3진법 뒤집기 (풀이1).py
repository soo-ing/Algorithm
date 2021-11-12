def solution(n):
    three = []
    answer=0
    while n:
        three.append(n%3)
        n//=3
    mul=1
    for i in range(len(three)-1,-1,-1):
        answer+=three[i]*mul
        mul*=3
    return answer