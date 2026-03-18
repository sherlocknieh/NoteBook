def MostElementIn(A):
    hashTable = {}
    mostElement = None
    mostCount = 0
    for x in A:
        hashTable[x] = hashTable.get(x, 0) + 1
        if hashTable[x] > mostCount:
            mostCount = hashTable[x]
            mostElement = x
    print(mostElement, mostCount)


A = [1, 2, 3, 2, 4, 2, 5]
MostElementIn(A)