"""배열 arr가 주어집니다.
배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
ex arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다."""

def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])

    return answer

arr=[1,1,3,3,0,1,1]
print(solution(arr))