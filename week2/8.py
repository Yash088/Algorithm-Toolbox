def fibonacciNum(num):
    num = num % 60
    a,b = 0,1
    sum=0
    for _ in range(num):
        a,b = b%10,(a + b)%10
        sum+=(a*a)%10
    print(sum%10)
num=int(input())
fibonacciNum(num)
