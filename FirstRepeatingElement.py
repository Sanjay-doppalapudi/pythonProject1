from time import *

def repeating(element):

    # for i in range(len(element)):
    #     for j in range(i,len(element)):
    #         if element[i] > element[j]:
    #             element[i], element[j] = element[j] , element[i]
    #             #Sorted List
    # print(element)
    # for i in range(len(element)-1):
    #     if element[i]  ==  element[i+1]:
    #         return element[i]
    #
    # return 'Found None'

    # Time taken to find 3 4 2 5 8 1 3 is 7.309783220291138
    #Time taken to find 100 elements 4.077674388885498
    # Time taken to find 500 elements 6.566758155822754 ----->>>> This is way high because I've sorted the elements before so its causing more time

    for i in range(len(element)):
        for j in range(i+1,len(element)):
            if element[i] == element[j]:
                return element[i]
    return 'Found None'
    #
    # Time taken to find 3 4 2 5 8 1 3 is 7.187041759490967
    # Time taken to find 100 elements 4.017812490463257
    # Time taken to find 500 elements 3.2182505130767822



startTime = time()
ele = list(map(int, input("Enter the numbers separated by spaces: ").split(" ")))
print(repeating(ele))
endTime = time()
print(endTime - startTime)