def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1
    reverse = 1 if start <= end else -1
    while start <= end:

        mid = start + int((end-start)/2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-reverse
        else:
            start = mid+reverse


arr = [1, 4, 5, 6, 7, 8, 9]
target = 7
print(arr[::-1])
for i in arr[::-1]:

    print(BinarySearch(arr, i), i)
for i in arr:

    print(BinarySearch(arr, i), i)
