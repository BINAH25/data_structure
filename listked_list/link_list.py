class Node:
    def __init__(self, data=None,next=None):
        self.next = next
        self.data = data
        
        
           
class Linked_list:
    def __init__(self):
        self.head = None
        
        
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)
        
    def print(self):
        if self.head is None:
            print('there is no head')
            return
        
        itr = self.head
        linked = ''
        while itr:
            linked += str(itr.data) + "-->"
            itr = itr.next
            print(linked)
            
    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_beginning(data)
        
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)    

if __name__ == '__main__':
    linked_list = Linked_list()
    #linked_list.insert_at_beginning(9)
    #linked_list.insert_at_beginning(13)
    #linked_list.insert_at_end(20)
    linked_list.insert_value(["Louis","Seyram","Blessing","Binah"])
    linked_list.print()
    linked_list.get_lenght()