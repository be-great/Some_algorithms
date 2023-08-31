def dynamicArray(n, queries):
    result=[]
    init=0
    saqlist=[[] for i in range(n)]
    for i in range(len(queries)):
        if queries[i][0]==1:
            indexarray=((queries[i][1])^init)%n
            saqlist[indexarray].append(queries[i][2])
        else:
            indexarray=((queries[i][1])^init)%n
            index=queries[i][2]%len(saqlist[indexarray])
            init=saqlist[indexarray][index]
            result.append(init)  
    return result
dynamicArray(2,[[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])
