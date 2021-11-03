def solution(x):
    num=list(map(int,list(str(x))))
    num=sum(num)

    return x%num==0