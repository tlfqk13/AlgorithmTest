

"""
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
"""

p=[2,1,3,2]

def solution(priorities,location):
    answer=0
    loc=[i for i in range(len(priorities))]
    final_loc=[]

    while priorities:
        if priorities[0]==max(priorities):
           final_loc.append(loc.pop(0))
           priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    return final_loc.index(location)+1



print(solution(p,1))