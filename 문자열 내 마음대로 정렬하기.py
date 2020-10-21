
"""
문자열로 구성된 리스트 strings와,
정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를
기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 [sun, bed, car]이고 n이 1이면
각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
"""

strings=["sun","bed","car"]
# strings=["abce", "abcd", "cdx"]
n=1

def solution(strings, n):

    #answer=sorted(strings,key=lambda x:x[n])
    #print(answer)
    #for i in range(len(strings)-1):
    #    if answer[i][n]==answer[i+1][n]:
    #        answer=sorted(answer)
    #return answer
    #return sorted(sorted(strings),key=lambda x:x[n])
    return sorted(sorted(strings),key=lambda x:x[n])

print(solution(strings,n))

sorted(sorted(strings),key=lambda x:x[n])