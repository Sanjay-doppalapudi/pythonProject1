def floorSorted(arr, n):
    print(arr)
    pos = 0
    for i in range(len(arr)):
        if (arr[i] < n or arr[i] > n) or arr[i] == n:
            return arr.index(arr[i-1])
    return -1




arr = list(map(int, input("Enter elements separated by space: ").split(" ")))
num = int(input("Enter a number: "))
print(floorSorted(sorted(arr),num))