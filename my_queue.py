#from collections import deque

#my_queue = deque()
#my_queue.append(10)
#my_queue.append(20)
#my_queue.append(30)

#print(my_queue.popleft())


class Queue:
    def __init__(self):
        self.data =list()

    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self):
        if len(self.data):
            return self.data[0]
        return None

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
print(my_queue.dequeue())


        

        