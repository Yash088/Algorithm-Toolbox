def fibonacciNum(num):
        a,b = 0,1
        for _ in range(num):
            a,b = b%10,(a + b)%10
        print(a)
num=int(input())
fibonacciNum(num)