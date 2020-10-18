
class cubes:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return cubesIterator(self)

class cubesIterator:
    def __init__(self,source):
        self.current=source.start
        self.source=source
    def __next__(self):
        if(self.current>self.source.stop):
            raise StopIteration
        else:
            x=self.current
            self.current+=1
            return x*x*x