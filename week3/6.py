def maxPrice(num):
    current,previous = [],0
    if(num > 2):
        for i in range(1,num):
            if( previous + i + i+1 > num ):
                current.append(num - previous)
                break
            else:
                current.append(i)
                previous += i 
    else:
        current.append(num)
    return current
num = int(input())
result = maxPrice(num)
print(len(result))
for i in range(len(result)):
    print(result[i],end=" ")