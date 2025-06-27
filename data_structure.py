#data structures include:
#list()
#dict()
#linked list           مجموعه ای از گره ها لیست پیوند گفته میشود     
#node گره:هر گره حاوی داده هست که هرجای حافظه ram ممکنه قرار گرفته باشه و 

# فرایند اپند کردن روی لینکد لیست

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head =None

    def append(self,value):
        """Append the given value to the existing linked list"""
        new_node = Node(value)   #a new node was made
        print(id(new_node))  
        if not self.head:       #زمانیکه من هیچ نودی نداشتم اولین نود رو بزار هد
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 

    def search(self,value):
        """Search for a value from all existing nodes"""
        current = self.head
        counter = 0
        while current:
            if current.value ==value:
                return counter
            current = current.next
            counter += 1
        return -1    

    def display(self): 
        """Display all items in the existing linked list"""  
        current =self.head
        while current:   
            print(current.value,end ="->") 
            current = current.next
        print("None") 

    def __getitem__(self,index):
        """Return the corresponding item withing the list""" 
        if not index < len(self):
            raise IndexError("Your index is out of range") 
        
        counter = 0
        current = self.head
        while current:
            if counter == index:
                return current.value
            counter += 1
            current =current.next

    def __len__(self):
        """count all nodes in the existing linked list"""
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter    
         


my_linked_list = LinkedList()  
my_linked_list.append(4)    # head of list
my_linked_list.append(24)
my_linked_list.append(46)

my_linked_list.display()   
#print(len(my_linked_list)) 
#print(my_linked_list.search(24))  
print(my_linked_list[6])       
