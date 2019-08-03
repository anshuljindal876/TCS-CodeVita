numbers = input().split()
n1 = int(numbers[0])
n2 = int(numbers[1])

## Functon finds all prime numbers between n1 and n2
def generatePrime(n1, n2):
    ser = []
    for i in range(n1, n2 + 1): 
        k = 0
        for j in range(2, i):
            if (i % j) == 0: 
                k = k + 1
        if(k <= 0):
            ser.append(i)
    return ser

## Function looks for all prime numbers in a given sequence of numbers
def findPrime(arr):
    ser = []
    for i in arr: 
        k = 0
        for j in range(2, i):
            if (i % j) == 0: 
                k = k + 1
        if(k == 0):
            ser.append(i)
    return ser

## Function outputs all combinations of elements in a list
def combine(arr):
    o = []
    for a in arr:
        for b in arr:
            if(a != b):
                val = int(str(a) + str(b))
                done = False
                for i in o:
                    if(val == i):
                        done = True
                if(not done):
                    o.append(val)
    return o

## Function to generate fibonacci sequence
def getFibNum(a, b, n):
    for i in range(2, n):
        nex = a + b
        a = b
        b = nex
    return b    
    
## Function to sort the given array in ascending order (Using Insertion Sort)
def sort(arr):  
    for i in range(1, len(arr)):
        for j in range(0, i):                   ## Compare the ith element with all those behind it
            if(arr[i] <= arr[j]):               ## If next element is bigger, then swap. Replace '<' with '>' to get output as descending order
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

if __name__ == '__main__':
    out = generatePrime(n1, n2)
    out1 = combine(out)
    arr = sort(out1)
    out2 = findPrime(arr)
    arr2 = sort(out2)
    a = arr2[0]
    b = arr2[len(arr2) - 1]
    val = getFibNum(a, b, len(out2))
    print(val)
