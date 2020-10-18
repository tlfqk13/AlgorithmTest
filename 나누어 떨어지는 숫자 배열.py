
"""array의 각 element 중 divisor로 나누어 떨어지는 값을
오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요"""


# arr=[5,9,7,10]
# arr=[2,36,1,3]
arr=[3,2,6]
divisor=10

def solution(arr,divisor):
    answer=[]
    for i in range(len(arr)):
        if(arr[i]%divisor==0):
            answer.append(arr[i])
        elif(arr[i]%divisor==arr[i]):
            answer=[-1]
    return sorted(answer)

print(solution(arr,divisor))

