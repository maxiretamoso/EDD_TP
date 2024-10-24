from linked_queue_ext import LinkedQueueExt

class Iter(LinkedQueueExt):
    def __iter__(self):
        self.actual = self.front 
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration 
        
        dato = self.actual.element
        self.actual = self.actual.next  

        return dato