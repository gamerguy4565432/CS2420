class Node:
    def __init__(self, item):
        self.mItem = item
        self.R = None
        self.L = None

    

class Bag:
    def __init__(self):
        self.mRoot = None

    def Insert(self, item):
        if self.Exists(item):
            return False
        
        
        n = Node(item)

        if self.mRoot is None:
            self.mRoot = n
            return

        self.InsertR(n, self.mRoot)
        return True
    
    def InsertR(self, n, current):
        if current is None:
            current = n

        else:
            if n.mItem < current.mItem:
                current.L = self.InsertR(n, current.L)
            #self.InsertR(n, current.L)

            else:
                current.R = self.InsertR(n, current.R)
            #self.InsertR(n, current.R)
        
        return current

    def __iter__(self):
        yield from self.IterRecursive(self.mRoot)

    def IterRecursive(self, current):
        if current is not None:
            yield from self.IterRecursive(current.L)
        
            yield current.mItem

            yield from self.IterRecursive(current.R)


    def Exists(self, item):
        e = self.ExistsR(self.mRoot, item)
        return e
    
    def ExistsR(self, current, item):
        if current is None:
            return False
        
        elif item < current.mItem:
            return self.ExistsR(current.L, item)
        
        elif item > current.mItem:
            return self.ExistsR(current.R, item)
        

        elif item == current.mItem:
            return True
        


    def size(self):
        if self.mRoot is None:
            return 0
        
        return 1 + self.sizeR(self.mRoot)
    

    def sizeR(self, current):
        count = 0

        if current.L is not None:
            count += 1 + self.sizeR(current.L)

        if current.R is not None:
            count += 1 + self.sizeR(current.R)

        return count
    
    def Delete(self, item):
        if not self.Exists(item):
            return False
        self.DeleteR(item, self.mRoot)
        return True
    

    def DeleteR(self, item, current):
        if item < current.mItem:
            self.DeleteR(item, current.L)

        elif item > current.mItem:
            self.DeleteR(item, current.R)

        else:
            if current.L is None and current.R is None:
                current = None

            elif current.L is not None and current.R is None:
                current = current.L

            elif current.L is None and current.R is not None:
                current = current.R
                

            else:
                s = current.R
                while s.L:
                    s = s.L
                    current.mItem = s.mItem
             
                    self.DeleteR(s.mItem, current.R)

        return current
    

    def Traverse(self):
        self.TraverseR(self.mRoot)

    def TraverseR(self, current):
        print(current.mItem.mFirst) 
        if current.L is not None:
            self.TraverseR(current.L)

        if current.R is not None:
            self.TraverseR(current.R)

    

