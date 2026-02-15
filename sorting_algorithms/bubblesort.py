arr=[4,50,444,55,5550]

def bubblesort(arr):
    n=len(arr)
    is_swap= False
    for i in range(n-2,0):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_swap=True
        if is_swap==False:
            return arr
    return arr

bubblesort(arr)
print(arr)
            