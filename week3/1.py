def minimumCoin(num,length):
    count=0
    length1 = length - 2
    if( length == 1 ):
        if( int(num) > 5 ):
            count+= 1 + ( int(num) - 5 )
        else:
            count +=  int(num)
    else:
        for i in range(length):
            if(  i == length - 2 ):
                count += int(num[i])
            elif( i == length - 1 ):
                if( int(num[i]) >= 5 ):
                    count  = count + 1 + ( int(num[i]) - 5 )
                else:
                    count += int(num[i])
            else:
                count += int(num[i])*( 10 ** ( length1 - i  ))
    print(count)

num=input()
minimumCoin(num,len(num))