from time import *

def countZeros(bin):
    zer = 0
    for item in bin:
        if item == '0':
            zer += 1
    return zer

def countOnes(bin):
    one = 0
    for item in bin:
        if item == '1':
            one += 1
    return one

start = time()
num = int(input())
binary = ''
while num !=1:
    temp = num % 2
    binary = binary + str(temp)
    num = num // 2
binary += '1'
print(binary[::-1])
print(countZeros(binary))
print(countOnes(binary))
end = time()
print(f'elapsed time: {end - start}')