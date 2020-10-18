class StrReverse:
    def __init__(self,string):
        self.string=string
    def __iter__(self):
        return ReverseIterator(self)
class ReverseIterator:
    def __init__(self,source):
        self.string=source.string
        self.index = len(self.string)
    def __next__(self):
        if(self.index<=0):
            raise StopIteration
        else:
            self.index=self.index-1
            return self.string[self.index]
