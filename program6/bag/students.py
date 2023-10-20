class Students:
    def __init__(self, first, last, ssn, email, age):
        self.mFirst = first
        self.mLast = last
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    
    def __eq__(self, rhs):
        return self.mSSN == rhs.mSSN
    

    def __ne__(self, rhs):
        return self.mSSN != rhs.mSSN