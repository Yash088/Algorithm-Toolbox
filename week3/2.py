def maxvalueLoot(dict1,dic_fraq,knapsack_cap):
    sorted_knapsack = []
    sum=0
    for i in sorted (dic_fraq.keys(), reverse= True) : 
      sorted_knapsack.append(dic_fraq[i])
    for i in sorted_knapsack:
        if( i == knapsack_cap ):
            sum += dict1[i]
            break
        elif( i > knapsack_cap ):
            sum += dict1[i] / (i//knapsack_cap)
            break
        else:
            sum += dict1[i]
            knapsack_cap = knapsack_cap - i
    print(sum)
n = input().split()
main_knapsack = {}
fraction_knapsack={}
for _ in range(int(n[0])):
    m = input().split()
    main_knapsack[int(m[1])] = int(m[0])
    fraction_knapsack[ int(m[0])/int((m[1])) ] = int(m[1]) 

maxvalueLoot( main_knapsack, fraction_knapsack, int(n[1]) )