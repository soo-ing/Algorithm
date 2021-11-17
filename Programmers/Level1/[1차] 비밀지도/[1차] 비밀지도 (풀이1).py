def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        space=''
        for j in range(n):
            if arr1[i]%2 or arr2[i]%2:
                space+='#'
            else:
                space+=' '
            arr1[i]//=2
            arr2[i]//=2
        
        answer.append(space[::-1])
     
    return answer