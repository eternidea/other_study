#First write a "helper" function with two extra parameters
# left, right that ddedscribes the search region as shown below
def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # Here is the key property we would like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    
    # your code here
    mid = (left+right)//2
    # if middle index = left then we found crossover
    if(mid == left):
        return mid
    # if middle index elements has x > y
    # then we need to change left to mid
    if(x[mid] >= y[mid]):
        return findCrossoverIndexHelper(x, y, mid, right)
    # if middle index elements has x < y
    # then we need to change right to mid
    elif (x[mid] < y[mid]):
        return findCrossoverIndexHelper(x, y, left, mid)
    
#Define the function findCrossoverIndex that wil 
# call the helper function findCrossoverIndexHelper
def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?
    # your code here
    return findCrossoverIndexHelper(x,y,0,len(y)-1)
