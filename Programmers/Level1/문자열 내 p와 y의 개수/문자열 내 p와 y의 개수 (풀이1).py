def solution(s):
    num1=0
    num2=0
    for i in range(len(s)):
        if s[i]=='p' or s[i]=='P':
            num1+=1
        elif s[i]=='y' or s[i]=='Y':
            num2+=1
    
    return num1==num2