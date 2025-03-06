from collections import deque

n,k = map(int, input().split())
n_list = [i+1 for i in range(n)]

result = []*n
cnt = 0


for i in range (1, n):    
    if i*k <= len(n_list) :
        result.append(n_list[i*k-1])
        # del n_list[index-1]
    else:
        index = i*k - n
        result.append(n_list[index-1])
        


print(result)

#7 3 
#<3, 6, 2, 7, 5, 1, 4>
