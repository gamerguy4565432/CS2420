import students
import bag
import time

t1 = time.time()
b = bag.LinkedList()

#fin = open("FN.txt", "r")
fin = open("FakeNames.txt", "r")


for line in fin:
    words = line.split()
    s = students.Students(words[0], words[1], words[2], words[3], words[4])
    ok = b.Insert(s)
    if not ok:
        print("Error: ", words[1], "not inserted because it's a duplicate")

    
fin.close()

t2 = time.time()

print("Inserting time was ", t2-t1)
print()
print("Inserting Average Age is", b.getAverageAge())

print(b.size())

t1 = time.time()

#fdel = open("DN.txt", "r")
fdel = open("DeleteNames.txt", "r")

for line in fdel:
    words = line.split()
    s = students.Students("", "", words[0], "", "")
    ok = b.Delete(s)
    if not ok:
        print("Error: ", words[0], "could not be found")



fdel.close()

t2 = time.time()

print(b.size())

print("Deleting time was ", t2-t1)
print()
print("Deleting Average Age is", b.getDelAverageAge())

t1 = time.time()


#fret = open("RN.txt", "r")
fret = open("RetrieveNames.txt", "r")

for line in fret:
    words = line.split()
    s = students.Students("", "", words[0], "", "")
    ok = b.Retrieve(s)
    if not ok:
        print("Error: ", words[0], "no finding")


fret.close()

t2 = time.time()

print("Retrieving time was ", t2-t1)
print()
print("Retrieve Average Age is", b.getRetAverageAge())


