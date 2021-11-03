def solution(x):
    num=list(str(x))
    sum=0

    for n in num:
        sum+=int(n)

    return x%sum==0