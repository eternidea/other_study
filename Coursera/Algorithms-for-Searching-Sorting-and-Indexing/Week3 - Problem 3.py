from random import random

def dot_product(lst_a, lst_b):
    and_list = [elt_a * elt_b for (elt_a, elt_b) in zip(lst_a, lst_b)]
    return 0 if sum(and_list)% 2 == 0 else 1

# encode a matrix as a list of lists with each row as a list.
# for instance, the example above is written as the matrix
# H = [[0,1,0,1],[1,0,0,0],[1,0,1,1]]
# encode column vectors simply as a list of elements.
# you can use the dot_product function provided to you.
def matrix_multiplication(H, lst):

    temp=[]
    for x in H:
        temp.append(dot_product(x,lst))
    return temp
    

# Generate a random m \times n matrix
# see the comment next to matrix_multiplication for how your matrix must be returned.\
def return_random_hash_function(m, n):
    import numpy as np
    # return a random hash function wherein each entry is chosen as 1 with probability >= 1/2 and 0 with probability < 1/2
    return np.random.randint(0,2,size=(m,n))
    
    
    
