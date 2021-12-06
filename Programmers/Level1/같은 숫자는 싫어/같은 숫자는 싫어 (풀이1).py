def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if not arr[i-1]== arr[i]:
            answer.append(arr[i])
    
    return answer