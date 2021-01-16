def fibonacciNum(num,m):
    start = 0
    next = 1
    for i in range(1,num+1):
        next += start 
        start = next-start
    print(start)
num,m=map(int,input().split())
fibonacciNum(num,m)