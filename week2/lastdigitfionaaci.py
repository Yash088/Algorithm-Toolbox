def fibonacciNum(num):
    start = 0
    next = 1
    for i in range(1,num+1):
        next += start 
        start = next-start
    print(start % 10)
num=int(input())
fibonacciNum(num)