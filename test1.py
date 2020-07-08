import time
import random


def sel_sort(a):
    n=len(a)

    for i in range(0,n-1):
        min_idx=i

        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j

        a[i],a[min_idx]=a[min_idx],a[i]

def random_number(a):
    n=a
    random_number_list=[]

    while len(random_number_list) !=n:
        a=random.randint(1,n)
        if a not in random_number_list:
            random_number_list.append(a)

    return random_number_list

def find_min(a):
    n=len(a)
    min_idx=0
    for i in range(0,n):
        if a[i]<a[min_idx]:
            min_idx=i

    return a[min_idx]

start=time.time()

d=random_number(10000)

#sel_sort(d)

min=find_min(d)


#print("sort",d)
#print("len",len(d))

print("find_min",min);

print("time : ",time.time()-start);