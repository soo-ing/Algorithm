import math

def solution(n):
    temp=math.sqrt(n)

    if temp-(int)temp==0:
        return (temp+1)*(temp+1)
    else:
        return -1