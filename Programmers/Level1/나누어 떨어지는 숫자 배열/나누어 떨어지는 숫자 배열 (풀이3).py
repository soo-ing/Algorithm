def solution(arr, divisor):
    return sorted([x for x in arr if x%divisor]) or [-1]
"""
앞이 거짓일 경우 뒤에 것 호출
"""