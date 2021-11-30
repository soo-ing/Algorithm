from collections import Counter

def solution(N, stages):
    fail = [0] * (N+1)
    num=len(stages)
    result=[]
    for i in range(1,N+1):
        count=Counter(stages)[i]
        if num:
            fail[i]=(count/num)
        num-=count
    for key, value in enumerate(fail[1:],start=1):
        result.append([key,value])
    result.sort(key=lambda a:a[1],reverse=True) 
    
    return [i[0] for i in result]