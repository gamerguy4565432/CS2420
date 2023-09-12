import random


def GenList(N):
    newlist = []

    for i in range(N):
        r = random.randint(1, N)
        newlist.append(r)

    
    return newlist



def BubbleSort(A):
    
    changes = True

    while changes:
        changes = False


        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                changes = True


# o(n^2)


def ShakerSort(A):

    changes = True
    
    while changes:
        changes = False

        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True

        
        for j in range(len(A) - 2, -1, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                changes = True




def CountingSort(A):

    F = [0] * (len(A) + 1)

    for v in A:
        F[v] += 1

    

    k = 0

    for i in range(len(F)):
        v = i
        count = F[i]

    
        for j in range(count):
            A[k] = v
            k += 1






def main():
    list1 = GenList(20)
    print(list1)
    A = list1
    BubbleSort(list1)
    print(list1)
    A.sort()
    print(A)

    print()


    list2 = GenList(20)
    B = list2
    ShakerSort(list2)
    print(list2)
    B.sort()
    print(B)

    print()


    list3 = GenList(20)
    C = list3
    CountingSort(list3)
    print(list3)
    C.sort()
    print(C)








if __name__ == '__main__':
    main()
