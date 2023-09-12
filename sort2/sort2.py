import random


def createRandomList(N):

    newlist = []

    for i in range(N):
        r = random.randrange(1, N)
        newlist.append(r)

    
    return newlist


def QuickSort(A, low, high):
    if (high - low) <= 0:
        return
    
    lmgt = low + 1

    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1


    pivot = lmgt - 1

    A[low], A[pivot] = A[pivot], A[low]


    QuickSort(A, low, pivot - 1)
    QuickSort(A, pivot + 1, high)


def ModifiedQuickSort(A, low, high):
    if (high - low) <= 0:
        return
    
    mid = (low + high) // 2
    A[low], A[mid] = A[mid], A[low]

    lmgt = low + 1

    for i in range(low + 1, high + 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1

    
    pivot = lmgt - 1

    A[low], A[pivot] = A[pivot], A[low]


    ModifiedQuickSort(A, low, pivot - 1)
    ModifiedQuickSort(A, pivot + 1, high)




def MergeSort(A):
    if len(A) <= 1:
        return
    
    L = A[0:len(A)//2]
    R = A[len(A)//2:len(A)]
    MergeSort(L)
    MergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            k += 1
            i += 1

        
        else:
            A[k] = R[j]
            k += 1
            j += 1

    while i < len(L):
        A[k] = L[i]
        k += 1
        i += 1

    
    while j < len(R):
        A[k] = R[j]
        k += 1
        j += 1



def main():
    list1 = createRandomList(20)
    A = list1
    A.sort()
    print(A)
    QuickSort(list1, 0, len(list1) - 1)
    print(list1)


    print()

    list2 = createRandomList(20)
    B = list2
    B.sort()
    print(B)
    ModifiedQuickSort(list2, 0, len(list2) - 1)
    print(list2)

    print()

    list3 = createRandomList(20)
    C = list3
    C.sort()
    print(C)
    MergeSort(list3)
    print(list3)



    print()





if __name__ == '__main__':
    main()