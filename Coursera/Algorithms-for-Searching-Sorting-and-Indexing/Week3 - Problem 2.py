
def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def simplePartition(a, pivot):
    ## To do: partition the array a according to pivot.
    # Your array must be partitioned into two regions - <= pivot followed by elements > pivot
    ## If an element at the beginning of the array is already <= pivot in the beginning of the array, it should not
    ## be moved by the algorithm.
    
    i=-1
    j=0
    n=len(a)
    
    for j in range(n):
        if a[j]<=pivot:
            swap(a,i+1,j)
            i+=1
   
            
def boundedSort(a, k):
    for j in range(1, k):
        simplePartition(a, j)
