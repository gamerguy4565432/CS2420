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
        if not ok:
            print("Error: ", words[1], "not inserted because it's a duplicate")

    
    fin.close()

    t2 = time.time()

    print("Inserting time was ", t2-t1)




if __name__ == '__main__':
    main()