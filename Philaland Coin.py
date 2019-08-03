T = int(input())                                ## Test cases
N = [int(input()) for i in range(T)]            ## N cases
O = [-1 for i in range(T)]                      ## OUTPUT Array

def func():
    for i in range(T):
        s = 0                                   ## Sums upto N                          
        for j in range(N[i]):
            s = s + j
            if(s >= N[i]):                      ## Once we get the value, go to next test case
                O[i] = j
                break
    return O

def main():
    val = func()
    for i in range(len(val)):
        print(val[i])

main()
