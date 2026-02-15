#decending

arr=[4,50,444,55,5550]

def selectionsort(arr):
    n=len(arr)
    for i in range(0,n):
        maxidx=i
        for j in range(i+1,n):
            if arr[j]>arr[maxidx]:
                maxidx=j
        arr[i],arr[maxidx]=arr[maxidx],arr[i]
    return arr

selectionsort(arr)
print(arr)