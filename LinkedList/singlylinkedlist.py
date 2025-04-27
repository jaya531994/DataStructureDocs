class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result += ' ->'
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length +=1

    def prepand(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length +=1

    def insert(self,value,index):
        new_node = None(value)
        if index < 0  and index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                pass



LL= LinkedList()
#append node
LL.append(10)
LL.append(20)
LL.prepand(50)
print(LL)


