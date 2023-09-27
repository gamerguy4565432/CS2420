class Students:
    def __init__(self, last, first, snn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = snn 
        self.mEmail = email
        self.mAge = age


    def __eq__(self, rhs):
        return self.mSSN == rhs.mSSN