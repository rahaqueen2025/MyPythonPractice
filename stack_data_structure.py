#my_stack =list()

#my_stack.append(2)    # متد دیدن لیست یا به عبارتی push
#my_stack.append(8)
#my_stack.append(7)
#my_stack.append(1)



#print(my_stack.pop())   #برای برداشتن داده که آخری رو برمیداره
#print(my_stack)


class Stack:
    def __init__(self):
        self.data =list()

    def push(self,value):
        """Push a new item to the end of stack"""
        self.data.append(value)

    def pop(self):
        """Return the last item from stack""" 
        return self.data.pop()
    
    def peek(self):
        """Visit the last item from stack"""
        return self.data[-1]
    
my_stack=Stack()
my_stack.push(10)
#my_stack.push(30)

print(my_stack.pop())


