import random
import sys
import time
import math

class Counter:
    def __init__(self):
        self.compares = 0



def GenList(N):
    newlist = []

    for i in range(N):
        r = random.randint(1, N)
        newlist.append(r)

    
    return newlist



def GenMostList(N):
    l = GenList(N)
    l.sort()
    l[0], l[-1] = l[-1], l[0]
    return l



def BubbleSort(A, c):
    
    changes = True

    while changes:
        changes = False


        for i in range(0, len(A) - 1):
            c.compares += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                changes = True


# o(n^2)


def ShakerSort(A, c):

    changes = True
    
    while changes:
        changes = False

        for i in range(0, len(A) - 1):
            c.compares += 1
            if A[i] > A[i + 1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True

        
        for j in range(len(A) - 2, -1, -1):
            c.compares += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                changes = True




def CountingSort(A, c):

    F = [0] * (len(A) + 1)

    for v in A:
        c.compares += 1
        F[v] += 1

    

    k = 0

    for i in range(len(F)):
        c.compares += 1
        v = i
        count = F[i]

    
        for j in range(count):
            c.compares += 1
            A[k] = v
            k += 1



def QuickSortRecursive(A, low, high, modified, c):
    if (high - low) <= 0:
        return
    

    if modified:
        c.compares += 1
        mid = (low + high) // 2
        A[low], A[mid] = A[mid], A[low]
    
    lmgt = low + 1

    for i in range(low + 1, high + 1):
        c.compares += 1
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1


    pivot = lmgt - 1

    c.compares += 1

    A[low], A[pivot] = A[pivot], A[low]


    QuickSortRecursive(A, low, pivot - 1, modified, c)
    QuickSortRecursive(A, pivot + 1, high, modified, c)


def QuickSort(A, m, c):
    QuickSortRecursive(A, 0, len(A) - 1, m, c)




def MergeSort(A, c):
    if len(A) <= 1:
        return
    
    L = A[0:len(A)//2]
    R = A[len(A)//2:len(A)]
    MergeSort(L, c)
    MergeSort(R, c)

    i = j = k = 0

    while i < len(L) and j < len(R):
        c.compares += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            k += 1
            i += 1

        
        else:
            A[k] = R[j]
            k += 1
            j += 1

    while i < len(L):
        c.compares += 1
        A[k] = L[i]
        k += 1
        i += 1

    
    while j < len(R):
        c.compares += 1
        A[k] = R[j]
        k += 1
        j += 1








def main():

    sys.setrecursionlimit(5000)

    print("     Bubble  Shaker  Counting   Quick   MQuick  Merge")

    SortingAlgorithms = [BubbleSort, ShakerSort, CountingSort, "QuickSort", "QuickSortR", MergeSort]

    for s in range(3, 13):

        print()
        s = 2 ** s
        print(s, end="\t")


        for sort in SortingAlgorithms:
            A = GenList(s)
            B = A[:]
            B.sort()
            c = Counter()
            if sort != "QuickSort" and sort != "QuickSortR":
                sort(A, c)
                print(round(math.log(c.compares, 2), 2), end="\t")

            elif sort == "QuickSort":
                QuickSort(A, False, c)
                print(round(math.log(c.compares, 2), 2), end="\t")

            elif sort == "QuickSortR":
                QuickSort(A, True, c)
                print(round(math.log(c.compares, 2), 2), end="\t")

            if A != B:
                print("error")




    '''c = Counter()
    list1 = GenList(20)
    print(list1)
    A = list1
    BubbleSort(list1, c)
    print(list1)
    A.sort()
    print(A)

    print()
    print(c.compares)
    print()

    c1 = Counter()
    list2 = GenList(20)
    B = list2
    ShakerSort(list2, c1)
    print(list2)
    B.sort()
    print(B)

    print()
    print(c1.compares)
    print()


    c2 = Counter()
    list3 = GenList(20)
    C = list3
    CountingSort(list3, c2)
    print(list3)
    C.sort()
    print(C)

    print()
    print(c2.compares)
    print()


    c3 = Counter()
    list4 = GenList(20)
    D = list4
    D.sort()
    print(D)
    QuickSort(list4, 0, len(list4) - 1, c3)
    print(list4)


    print()
    print(c3.compares)
    print()

    c4 = Counter()
    list5 = GenList(20)
    E = list5
    E.sort()
    print(E)
    ModifiedQuickSort(list5, 0, len(list5) - 1, c4)
    print(list5)

    print()
    print(c4.compares)
    print()

    c5 = Counter()
    list6 = GenList(20)
    F = list6
    F.sort()
    print(F)
    MergeSort(list6, c5)
    print(list6)



    print()
    print(c5.compares)
    print()'''













if __name__ == '__main__':
    main()
