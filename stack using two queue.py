# Stack using two queues
#push method costly
class stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []


    def push(self, x):
        self.queue2.append(x)
        while len(self.queue1) != 0:
            c = self.queue1.pop(0)
            self.queue2.append(c)
        self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self):
        return self.queue1.pop(0)
    def get_stack(self):
        return self.queue1
c = stack()
c.push(1)
c.push(3)
c.push(4)
c.push(100)
print(c.get_stack())
print(c.pop())

    
        
    
