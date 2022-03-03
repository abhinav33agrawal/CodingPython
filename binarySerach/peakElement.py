def findPeak(arr):
    n = len(arr)
    # start = 0
    # end = len(arr)-1
    if n <= 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return n-1

    start = 1
    end = n-2

    while start <= end:
        mid = start + (end-start)//2
        print(mid, arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1])
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
        if arr[mid] > arr[mid+1]:
            end = mid-1
        else:
            start = mid+1


arr = [1, 8, 3, 2, 1, 0]

print(findPeak(arr))
arr = [1, 2, 1, 3, 5, 6, 4]
print(findPeak(arr))
