def solution(n):
    return n + sum([i for i in range(1,(n//2)+1) if n%i==0])

"""
자기 자신을 제외한 약수는 반보다 아래인 것을 이용하여 구현
"""