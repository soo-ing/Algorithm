def solution(answers):
    answer1=[1,2,3,4,5]
    answer2=[2,1,2,3,2,4,2,5]
    answer3=[3,3,1,1,2,2,4,4,5,5]
    
    result=[0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answer1[i%5]==answers[i]:
            result[0]+=1
        if answer2[i%8]==answers[i]:
            result[1]+=1
        if answer3[i%10]==answers[i]:
            result[2]+=1

    for i,j in enumerate(result):
        if j == max(result):
            answer.append(i+1)
    return answer