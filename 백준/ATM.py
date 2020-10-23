def solution(n):
    n=sorted(n)
    wait_time=0
    total_time=0
    for i in range(len(n)):
        wait_time=wait_time+n[i]
        total_time+=wait_time

    return total_time

n=[3,1,3,4,2]
print(solution(n))