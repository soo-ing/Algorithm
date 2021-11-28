def solution(s):
    num=''
    arr=['zero','one','two','three','four','five','six','seven','eight','nine']
    answer=''
    for i in range(len(s)):
        if s[i].isdigit():
            answer+=s[i]
        else:
            num+=s[i]
            if num in arr:
                answer+=str(arr.index(num))
                num=''
            
    return int(answer)