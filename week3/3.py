def minCarFuel(basekm,gasStation,length):
    count=0
    prevdiff = 0
    totalKm = basekm
    coverindex = -1
    diff = 0
    for i in range(len(gasStation)):
        if( gasStation[i] < totalKm and i > coverindex  and totalKm < length ):
            diff = totalKm - gasStation[i]
            prevdiff = diff
            for j in range(i+1, len(gasStation)):
                if( gasStation[j] < totalKm and ( totalKm - gasStation[j] ) < diff ):
                    diff =  totalKm - gasStation[j]
                    totalKm += gasStation[j]
                    coverindex = j 
                    count += 1
                if ( j == len(gasStation)-1 and prevdiff == diff ):
                    totalKm += gasStation[i]
                    count += 1
        else:
            count=0
    return -1 if(count == 0 ) else count
maxKm = 400
length=950
gasStation = [200,375,550,750]
print(minCarFuel(maxKm,gasStation,length))