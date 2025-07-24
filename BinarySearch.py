def binary_search(elem, k):
    for i in range(len(elem)):
        for j in range(i, len(elem)):
            if elem[i] > elem[j]:
                elem[i], elem[j] = elem[j], elem[i]
    print(elem)
    '''
    now i need to check the mid point, for even its len/2, if odd (len+1)/2 and (len-1)/2
    '''
    low = 0
    high = len(elem)
    while  low < high:
        mid = (low + high) // 2
        if elem[mid] == k:
            return mid
        elif elem[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return -1

elements = list(map(int, input("Enter integers separated by space: ").split(" ")))
key = int(input("Enter the key element to search: "))
res = binary_search(elements, key)
print(res)