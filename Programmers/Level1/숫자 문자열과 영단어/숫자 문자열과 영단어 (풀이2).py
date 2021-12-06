def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


    for i in range(len(words)):
        s=s.replace(word[i],str(i))

    return int(s)