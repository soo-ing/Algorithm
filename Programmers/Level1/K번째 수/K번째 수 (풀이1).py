def solution(array, commands):
    new=[]
    answer=[]

    for command in commands:
        new=array[command[0]-1:command[1]]
        new.sort()
        answer.append(new[command[2]-1])

    return answer