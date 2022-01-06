def binary_search(L,k):
    begin = 0  # first element of list
    end = len(L)-1 # last element of a list
    true_statement = "Element found in list"
    false_statement = "Oops! Element not found"

    while(end-begin>1):
        mid = (begin+end)//2

        if(L[mid]==k):
            return true_statement

        if(L[mid]>k):
            end = mid-1

        if(L[mid]<k):
            begin = mid +1

    if (L[begin]==k) or (L[end]==k):
        return true_statement
    else :
        return false_statement


if __name__ == '__main__':
    L = list(range(100000000))
    print(binary_search(L,5000))