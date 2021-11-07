import numpy as np

def solution(arr1, arr2):
    a=np.array(arr1)
    b=np.array(arr2)

    answer=a+b

    return answer.tolist()

"""
numpy 사용
array 단위로 데이터를 다뤄 연산 수행
array는 간단하게 행렬이라고 생각
마지막에 tolist() 함수는 같은 레벨(위치)에 있는 데이터끼리 묶어주는 함수
잠시 array로 바꿔주었던 것을 다시 list로 변환해주어야 하기 때문에 사용
"""