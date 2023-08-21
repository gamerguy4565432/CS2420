import random


def GenList(N):
    newlist = []

    for i in range(N):
        r = random.randint(0, 10)
        newlist.append(r)

    
    return newlist



def BubbleSort(A):
    
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]


    return A



def ShakerSort(A):

    swapt = True
    start = 0
    stop = len(A) - 1

    while swapt:
        swapt = False
        for i in range(start, stop):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapt = True


        if swapt == False:
            break


        for i in range(start, stop):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapt = True

        
        if swapt == False:
            break

    return A



def CountingSort(A):

    m = max(A)

    list1 = []

    for i in range(m + 1):
        for j in range(len(A)):
            if i == A[j]:
                list1.append(i)
                

    return list1






def main():
    list1 = GenList(20)
    A = list1
    list1 = BubbleSort(list1)
    print(list1)
    A.sort()
    print(A)

    print()


    list2 = GenList(20)
    B = list2
    list2 = ShakerSort(list2)
    print(list2)
    B.sort()
    print(B)

    print()


    list3 = GenList(20)
    C = list3
    list3 = CountingSort(list3)
    print(list3)
    C.sort()
    print(C)









main()