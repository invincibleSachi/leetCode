class Fib:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        return FibIterator(self)

class FibIterator:
    def __init__(self,obj):
        self.max=obj.max
        self.current=0
        self.next=1
    def __next__(self):
        if(self.current>self.max):
            raise StopIteration
        else:
            self.current=self.current+self.next
            nextFib=self.current+self.next
            self.current=self.next
            self.next=nextFib
            return nextFib