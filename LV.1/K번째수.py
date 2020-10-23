
"""배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을때
    K번째에 있는 수를 구하려 합니다
    ex [1,5,2,6,3,7,4] i=2,j=5,k=3이면
    [5,2,6,3] return 값은 5"""


def solution(array,commands):
    answer=[]
    for c in commands:
        newArray=array[c[0]-1:c[1]]
        newArray.sort()
        answer.append(newArray[c[2]-1])

    return answer

array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]

# i=commands[0][0]
# j=commands[0][1]
# k=commands[0][2]
#
# print("***************")
# result=sorted((array[i-1:j]))
# print(result)
# print(result[k-1])
# print("***************")



print(solution(array,commands))