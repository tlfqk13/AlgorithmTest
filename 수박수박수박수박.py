"""
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는
문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 수박수박을 리턴하고 3이라면
수박수를 리턴하면 됩니다.
"""

n=4
str="수박수박수박수박"

def solution(n):
    answer="수박수박수박수"
    answer=answer[0:n]
    return answer

def solution1(n):
    return ('수박'*n)[:n]

print(solution1(n))

