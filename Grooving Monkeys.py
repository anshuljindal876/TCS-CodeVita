T = int(input())
N = [-1 for i in range(T)]
P = [-2 for i in range(T)]

for i in range(T):
    N[i] = int(input())
    temp = input().split()
    P[i] = [int(temp[j]) - 1 for j in range(len(temp))]    

def getCount(n, p, m):
    t = 1
    now = [0,1,2,3,4,5]
    
    while True:
        prev = now
        now = [prev[j] for j in p]
        if(now == m):
            break
        t = t + 1
    return t

if __name__ == '__main__':
    count = 0
    
    for i in range(T):
        monk = [i for i in range(N[i])]
        count = getCount(N[i], P[i], monk)
        print(count)
