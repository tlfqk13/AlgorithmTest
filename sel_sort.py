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



start=time.time()

d=random_number(10000);

sel_sort(d)

print("sort",d)
print("len",len(d))

print("min",d[0])

print("time : ",time.time()-start);


#data 5000개
# 1.5309326648712158
# 2.7188620567321777

#data 10,000개
# 4.920722007751465
# 10.388967275619507
