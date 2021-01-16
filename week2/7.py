def fibonacciNum(num,m):
    m = m % 60
    a,b = 0,1
    sum=0
    for i in range(m+1):
        if( i >= num ):
            sum = sum + a
        a,b = b%10 ,(a + b)%10 
    print(sum%10)
num,m=map(int,input().split())
fibonacciNum(num,m) 