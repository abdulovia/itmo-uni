def merge(l, m, r):
    it1, it2 = 0, 0
    res = [0]*(r-l+1)
    L = sorted(arr[l:m])
    R = sorted(arr[m:r+1])
    
    while it1 < len(L) and it2 < len(R):
        if L[it1] < R[it2]:
            res[it1+it2] = L[it1]
            it1 += 1
        else:
            res[it1+it2] = R[it2]
            it2 += 1
            
    while it1 < len(L):
        res[it1+it2] = L[it1]
        it1 += 1
    while it2 < len(R):
        res[it1+it2] = R[it2]
        it2 += 1
        
    it = l
    for x in res:
        arr[it] = x
        it += 1
    print(res)

def merge_sort(l, r):
    global step
    if l < r:
        mid = l + (r - l) // 2
        
        merge_sort(l, mid)
        merge_sort(mid+1, r)
        
        merge(l, mid, r)
        
        

step = 1
m = {}
arr = [6, 5, 12, 10, 9, 1]
m[step] = [arr]
step += 1
merge_sort(0, len(arr)-1)
m[step] = [arr]
for k, v in m.items():
    print(f'{k}: {v}')