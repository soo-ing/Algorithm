def solution(d, budget):
    d.sort()
    answer=0
    for i in range (len(d)):
        answer+=d[i]
        if answer>budget:
            return i
        
    return len(d)