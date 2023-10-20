class Node:
    def __init__(self, item, n):
        self.mItem = item
        self.mNext = n


class LinkedList:
    def __init__(self):
        self.mFirst = None
        self.InsertAge = 0
        self.DeleteAge = 0
        self.DelAmount = 0
        self.RetrieveAge = 0
        self.RetAmount = 0

    
    def getAverageAge(self):
        if self.size() == 0:
            return 0
        return self.InsertAge/self.size()
    

    def getRetAverageAge(self):
        if self.RetAmount == 0:
            return 0
        return self.RetrieveAge/self.RetAmount 
    
    def getDelAverageAge(self):
        if self.DelAmount == 0:
            return 0
        return self.DeleteAge/self.DelAmount

    def Insert(self, item):
        if self.Exists(item):
            return False 
        n = Node(item, None)
        self.InsertAge += int(item.mAge)
        n.mNext = self.mFirst
        self.mFirst = n
        return True  


    def Exists(self, item):
        current = self.mFirst

        while current is not None:
            if current.mItem == item:
                return True
            
            current = current.mNext

        return False
    
    def size(self):
        current = self.mFirst
        count = 0

        while current:
            count += 1
            current = current.mNext

        return count
    


    def Retrieve(self, item):
        current = self.mFirst

        while current:
            if current.mItem == item:
                self.RetrieveAge += int(current.mItem.mAge)
                self.RetAmount += 1
                return True
            current = current.mNext

        
        return False
    

    def __iter__(self):
        current = self.mFirst

        while current:
            yield current.mItem
            current = current.mNext


    def Delete(self, item):
        '''if not self.Exists(item):
            return False 
        
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                break 
            current = current.mNext

        self.DeleteAge += int(current.mItem.mAge)
        self.DelAmount += 1

        current.mNext = current.mNext.mNext

        return True'''

        if self.Exists(item):
            if self.mFirst.mItem == item:
                self.mFirst = self.mFirst.mNext
                return True
            
            current = self.mFirst

            while current:
                if current.mNext.mItem == item:
                    break

                current = current.mNext

            self.DeleteAge += int(current.mItem.mAge)
            self.DelAmount += 1
            current.mNext = current.mNext.mNext
            return True
        
        else:
            return False
        
        


    def PrintList(self):
        current = self.mFirst

        while current is not None:
            print(current.mItem.mFirst)
            current = current.mNext   

    


