def linear_search(element, keys):
    pos = 0
    for items in element:
        if items == keys:
            pos =  element.index(keys)
            break
        else:
            pos =  -1
    return pos

elements = list(map(str, input("Enter the elements separated by ',': ").split(",")))
key = input("Enter the Key: ")
res = linear_search(elements, key)
print(res)