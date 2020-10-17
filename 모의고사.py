"""1번 문제부터 마지막 문제까지의 정답이 순서대로 들은
배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지
배열에 담아 return 하도록 solution 함수를 작성해주세요."""

# first=[1,2,3,4,5]
# second=[2,1,2,3,2]
# third=[3,3,1,1,2]
# answer=[1,3,2,4,2]
# count=0
# count1=0
# count2=0
#
# for i in range(len(answer)):
#     if(first[i]==answer[i]):
#         count+=1
#
#     if(second[i]==answer[i]):
#         count1+=1
#
#     if(third[i]==answer[i]):
#         count2+=1
#
# result=[count,count1,count2]
#
# for person, score in enumerate(result):
#     if score == max(result):
#         answer.append(person+1)

def solution(answers):
    answer=[]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2]
    third = [3, 3, 1, 1, 2]

    count=[0.,0,0]
    for i in range(len(answers)):
        if (first[i] == answers[i%len(first)]):
            count[0]+= 1

        if (second[i] == answers[i%len(second)]):
            count[1]+= 1

        if (third[i] == answers[i%len(third)]):
            count[2]+= 1

    max_count=max(count)

    for i in range(3):
        if(count[i]==max_count):
            answer.append(i+1)
    return answer

a=[1,2,3,4,5]
print(solution(a))