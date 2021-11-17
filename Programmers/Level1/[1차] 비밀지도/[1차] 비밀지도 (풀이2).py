def solution(n, arr1, arr2):
    answer = []
    
    for i,j in zip(arr1,arr2):
        space=str(bin(i|j)[2:])
        space=space.zfill(n)
        space=space.replace('1','#')
        space=space.replace('0',' ')
        answer.append(space)
    return answer