import itertools as it
import operator



"""2016년 1월1일은 금요일입니다
   2016년 a월b일은 무슨 요일일까용?
   두 수 a,b를 입력받아 2016년 a월 b일이 무슨 요일인지
   리턴하는 함수 완성하세요 !!"""


def solution(a,b):
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]

    return day[(sum(mon[:a - 1]) + b) % 7]

a=input()
b=input()

a=int(a)
b=int(b)
print(solution(a,b))
