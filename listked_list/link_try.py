class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # FUNCTION TO ADD DATA AT THE BEGINING OF THE LINKEDLIST    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    # FUNCTION TO ADD DATA AT THE END OF THE LINKEDLIST    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
    # FUNCTION TO INSERT VALUES
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
            
    # FUNCTION TO GET THE LENTGH OF THE LINKED LIST
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        
    # FUNCTION TO PRINT  THE LINKEDLIST       
    def print(self):
        if self.head is None:
            print("the list is empty")
            return
        
        lists = ''
        itr = self.head
        while itr:
            lists += str(itr.data) + "-->"
            itr = itr.next
        print(lists)
    
    # FUNCTION TO REMOVE ELEMENT FROM THE LINKED LIST
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Index out of bound")
            
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
linked_list = LinkedList()
#linked_list.insert_at_beginning(7)
#linked_list.insert_at_beginning(9)
#linked_list.insert_at_end(18)
linked_list.insert_values([1,2,3,45,6,7])
linked_list.print()
print(linked_list.get_length()) 
linked_list.remove_at(3)
linked_list.print()
print(linked_list.get_length()) 
