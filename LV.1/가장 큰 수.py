

numbers= [6,10,2]
numbers = list(map(str, numbers))
numbers.sort(key=lambda x:x*3,reverse=True)

# 666,101010,222
print(numbers)