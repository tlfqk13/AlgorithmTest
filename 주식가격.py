


"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요
"""
from collections import deque
#
# def solution1(prices):
#     answer = [0 for _ in range(len(prices))]
#     stack = []
#     for i in range(len(prices)):
#         while len(stack) != 0 and prices[i] < prices[stack[len(stack) -1]]:
#             temp = stack.pop()
#             answer[temp] = i - temp
#         stack.append(i)
#     while len(stack):
#         temp = stack.pop()
#         answer[temp] = len(prices) - temp - 1
#
#     return answer
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        cnt = 0
        price = prices.popleft()

        for v in prices:
            cnt += 1
            if price > v:
                break
        answer.append(cnt)

    return answer

prices=[1,2,3,2,3]

print(solution(prices))