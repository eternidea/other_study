def testIfPartitioned(a, k):
    # TODO : test if all elements at indices < k are all <= a[k]
    #         and all elements at indices > k are all > a[k]
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    # your code here
    
    dum1=True
    dum2=True
    stand=a[k]
    
    for x in range(k):
        if a[x]<=stand:
            dum1*=dum1
        else:
            dum1=False
    for y in range(-1,k-len(a),-1):
        if a[y]>stand:
            dum2*=dum2
        else:
            dum2=False
    if dum1*dum2==1:
        return True
    else:
        return False
    