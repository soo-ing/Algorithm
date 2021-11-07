def solution(n):
    return int("".join(sorted(str(n),reverse=True)))

"""
sorted 함수를 사용하면 자동으로 리스트로 반환하기 때문에 따로 리스트로 변환하지 않아도 된다.
"""