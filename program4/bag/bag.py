class Bag:
    def __init__(self):
        self.A = []


    def Exists(self, x):
        for item in self.A:
            if x == item:
                return True
        
        return False
    
    def Insert(self, x):
        if self.Exists(x) == False:
            return False
        self.A.append(x)


    def size(self, x):
        return len(self.A)