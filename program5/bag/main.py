import bag
import student
import time


def main():
    t1 = time.time()
    b = bag.Bag()

    fin = open("Fakenames.txt", "r")

    for line in fin:
        words = line.split()
        s = student.Students(words[0], words[1], words[2], words[3], words[4])
        ok = b.Insert(s)
        if ok:
            print("Error: ", words[1], "not inserted because it's a duplicate")

    
    fin.close()

    t2 = time.time()

    print("Inserting time was ", t2-t1)


    t1 = time.time()

    averageAge = b.Traverse()

    print("The average age is: ", averageAge)
    print()
    t2 = time.time()
    print("Traverse time was ", t2-t1)


    fin = open("DeleteNames.txt", "r")
    for line in fin:
        ssn = line.strip()
        s2 = student.Students("","",ssn,"","")
        ok = b.Delete(s2)

        if not ok:
            print(s2.mSSN, "Could not be deleted")


    print("Average age for deletion is", b.DelAge())


    fin.close()


    fin = open("RetrieveNames.txt", "r")
    
    for line in fin:
        ssn = line.strip()

        s3 = student.Students("", "", ssn, "", "")

        ok = b.Retrieve(s3)

        #if ok == True:
        #    print(s3.mSSN)

        if not ok:
            print("Error:", s3.mSSN, "Could not be retrieved")

    
    print("Average age for retrieve is", b.RetAge())





if __name__ == '__main__':
    main()