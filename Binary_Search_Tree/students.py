class Students:
    def __init__(self, first, last, ssn, email, age):
        self.mFirst = first
        self.mLast = last
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    def __eq__(self, rhs):
        return self.mSSN == rhs.mSSN
    
    def __lt__(self, rhs):
        return self.mSSN < rhs.mSSN
    
    def __le__(self, rhs):
        return self.mSSN <= rhs.mSSN
    
    def __gt__(self, rhs):
        return self.mSSN > rhs.mSSN
    
    def __ge__(self, rhs):
        return self.mSSN >= rhs.mSSN
    

    def __ne__(self, rhs):
        return self.mSSN != rhs.mSSN
