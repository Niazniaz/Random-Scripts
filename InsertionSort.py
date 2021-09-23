#insertion Sort
'''l=[77,7,78,9,1,2,3,44,88]
for i in range(1,len(l)): #First Element Sorted
    key=l[i]

    j=i-1
    while j>=0 and key<l[j]:
        #SWAP
        l[i],l[j]=l[j],l[i] FAILURE
        key=l[j]
        j-=1
        print j
        print key
        print l
print l'''
arr=[6,1,33,455,7,878,9]
for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                print arr
        arr[j+1] = key
print arr

