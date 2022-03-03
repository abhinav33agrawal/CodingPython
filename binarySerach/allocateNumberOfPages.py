def isValid(arr, students, mid, k):
    students = 1
    sume = 0
    for i in arr:
        sume += i
        # print(sume, mid, "AA")
        if sume > mid:
            # print(sume, mid, "BB")
            students += 1
            sume = i
            # print('students: ', students, mid)
        if students > k:
            return False
    return True


def allocate(arr, students):
    if len(arr) < students:
        return -1
    start = max(arr)
    end = sum(arr)
    res = -1
    while start <= end:
        mid = (start+end)//2
        # print(start, end, mid)

        # print('isValid(arr, students, mid): ', isValid(arr, students, mid))
        if isValid(arr, students, mid, students):
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res


arr = [10, 20, 30, 40]
students = 4

print(allocate(arr, students))
