def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:

        mid = start + int((end-start)/2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1


arr = [1, 4, 5, 6, 7, 8, 9]
target = 7
for i in arr:
    print(BinarySearch(arr, i), i)
