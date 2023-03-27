from typing import List

def remove_duplicates(arr: List[int]) -> int:
    """
    * ii: current index that is unique
    * jj: current index that is being evaluated isUnique
    * isUnique: arr[ii]==arr[jj]
    * true -> arr[jj] is unique -> copy arr[jj] to arr[ii+1]
    * false -> arr[jj] is duplicate -> keep moving
    """
    ii=0
    jj=0
    N=len(arr)
    for jj in range(N):
        if arr[jj]!=arr[ii]: #arr[jj] is unique
            ii+=1 # move ii to next to take new value
            arr[ii]=arr[jj]
    return ii+1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))
