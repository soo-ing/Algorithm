n,m = map(int,input().split())

for i in range(m):
    for j in range(n):
        print('*',end='')
    print()

"""
input() : 한 줄의 표준 입력을 받아 문자열로 반환

list(map(int, input().split())) : 공백을 기준으로 구분된 데이터를 입력받을 때 사용

a,b = map(int, input().split()) 
"""