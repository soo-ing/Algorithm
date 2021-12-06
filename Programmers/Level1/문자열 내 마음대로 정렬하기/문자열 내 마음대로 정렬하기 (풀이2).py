def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])

"""
일회성 함수인 람다함수 사용
"""