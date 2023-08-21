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





        













def main():
    list1 = [5,4,2,7,1,2,0,9]
    print(ShakerSort(list1))






main()