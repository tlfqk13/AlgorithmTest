

arr=[6,10,2]
arr1=[3,30,34,5,9]

list1=[]
list2=[]
for i in range(0,len(arr1)):
    if arr1[i]:
        a=arr1[i]%10
        list1.append(a)

for i in range(0,len(arr)):
    if arr[i]:
        a=arr[i]%10
        list2.append(a)

list1.sort(reverse=True)
list2.sort(reverse=True)

print(list1)
print(list2)

