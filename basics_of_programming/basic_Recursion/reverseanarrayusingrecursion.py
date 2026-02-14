def func(l,r,arr):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    func(l+1,r-1,arr)

arr=[1,2,3,4,5,6,7,8]
func(2,5,arr)
print(arr)
