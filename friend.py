

def print_all_friends(g,start):

    qu=[]
    done=set()

    # qu.append(start)
    # print(qu)
    # done.add(start)
    # print(done)

    qu.append((start,0))
    done.add(start)



    while qu:
        (p,d) = qu.pop(0)
        print("p", p,d)
        for x in g[p]:
            # print(x)
            if x not in done:
                qu.append((x,d+1))
                done.add(x)

fr_info={
    'Summer':['John','Justin','Mike'],
    'John':['Summer','Justin'],
    'Justin':['John','Summer','Mike','May'],
    'Mike':['Summer','Justin'],
    'May':['Justin','Kim'],
    'Kim':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom']
}
print_all_friends(fr_info,'Summer')
print()
print_all_friends(fr_info,'Jerry')

