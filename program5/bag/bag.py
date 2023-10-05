class Bag:
    def __init__(self):
        self.A = []
        self.RaverageAge = 0
        self.Rsize = 0
        self.DaverageAge = 0
        self.Dsize = 0


    def Exists(self, x):
        for item in self.A:
            if x == item:
                return True
        
        return False
    
    def Insert(self, x):
        if self.Exists(x):
            return True
        self.A.append(x)


    def size(self):
        return len(self.A)
    
    def Traverse(self):
        totalAge = 0
        for item in self.A:
            totalAge += int(item.mAge)

        if self.size() == 0:
            return False 

        averageAge = totalAge / self.size()

        return averageAge

    
    def Delete(self, x):
        if not self.Exists(x):
            return False
        
        for i in range(len(self.A)):
            if self.A[i] == x:
                self.DaverageAge += int(self.A[i].mAge)
                self.Dsize += 1
                self.A.pop(i)
                return True
            
    
    def Retrieve(self, x):
        if not self.Exists(x):
            return False
        
        for i in range(len(self.A)):
            if self.A[i] == x:
                self.RaverageAge += int(self.A[i].mAge)
                self.Rsize += 1 
                return True
            


    def RetAge(self):
        return self.RaverageAge / self.Rsize
    

    def DelAge(self):
        return self.DaverageAge / self.Dsize
        