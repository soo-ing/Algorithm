def solution(x, n):
    answer=[]
    
    for i in range(n):
        answer.append(x*(i+1))
    return answer

"""
배열 요소 추가 함수 append() 사용
append()는 리스트 형태에서 마지막에 요소를 추가하는 함수
"""