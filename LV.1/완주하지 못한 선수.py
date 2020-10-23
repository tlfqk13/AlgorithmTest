import collections
"""단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다
   완주하지 못한 선수 이름을 return 하세용"""

"""제한사항 경기에 참여한 선수 1~100,000명이하
    완주한 선수들의 이름이 담긴 배열 completion이
    participant의 길이보다 1작습니다"""


# def solution(participant,completion):
#     answer=''
#
#     for i in range (len(participant)):
#         for j in range (i+1,len(completion)):
#             if(participant[i] not in completion[j]):
#                 answer=participant[i]
#
#     return answer

def solution(participant,completion):
    answer=collections.Counter(participant)-collections.Counter(completion)
    return list(answer.keys())[0]

participant=["leo","kiki","eden"]
completion=["eden","kiki"]

print(solution(participant,completion))