def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    answer=0
    for i in lottos:
        if i in win_nums:
            answer+=1 
    return [rank[answer+lottos.count(0)],rank[answer]]