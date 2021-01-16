def pisano_length(m):
    a,b = 0,1
    for i in range(m*m):
        a,b = b,(a + b)%m
        if( a == 0 and b == 1 ):
            return i+1  

def fibonacciNum(num,m):
    repeat_length = pisano_length(m)
    num = num % repeat_length
    a,b = 0,1
    for _ in range(num):
        a,b = b,(a + b)
    print(a%m)
num,m=map(int,input().split())
fibonacciNum(num,m) 