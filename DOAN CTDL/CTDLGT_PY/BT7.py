class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next 
        self.prev = prev  
        self.data = data 
        
    
    def push(self, new_data): 
      
       
        new_node = Node(data = new_data)  
        new_node.next = self.head 
        new_node.prev = None
       
        if self.head is not None: 
            self.head.prev = new_node 
      
        self.head = new_node 
      
    def insertAfter(self, prev_node, new_data): 
      
            if prev_node is None: 
                print("This node doesn't exist in DLL") 
                return
       
            new_node = Node(data = new_data) 
      
            new_node.next = prev_node.next
      
            prev_node.next = new_node 

            new_node.prev = prev_node 
 
            if new_node.next is not None: 
                new_node.next.prev = new_node