def maxAdvertise(x,y):
    x,y = sorted(x,reverse= True),sorted(y,reverse= True)
    sum=0
    for i in range(len(x)):
        sum+=x[i]*y[i]
    return sum
placeholder = input()
x = list(map(int,input().split()))
y = list(map(int,input().split()))
print(maxAdvertise(x,y))