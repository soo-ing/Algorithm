def solution(n):
    answer=[0]*1000000  
    answer[0]=0
    answer[1]=1
    
    for i in range(2,n+2):
        answer[i]=(answer[i-1]+answer[i-2])%1234567
    
    return answer[n]