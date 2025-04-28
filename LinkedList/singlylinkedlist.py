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

    #Add elements in linked list
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
        new_node = Node(value)
        if index < 0  and index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                pass

    
    #Traversal of linked list
    def Travers(self):
        current = self.head
        while current is not None:
            print("Current value of linked list",current)
            current = current.next


    def Search(self,target):
        current = self.head
        while current is not None:
            if current.value == target:
                print("value found in list")
                return True 
            current = current.next
        print("value not found in list")
        return False
    
    def Get(self,ind):
        current = self.head
        if ind < 0 and ind >= self.length:
            return None
        if ind == -1:
            return self.tail.value
        for _ in range(ind):
            current = current.next

        return current.value
    
    #update the LL using set
    # def Set(self,ind,value):
    #     temp= self.Get(ind)
    #     if temp:
    #         temp.value = value
    #         return True
    #     return False
    
    #Delete nodes
    #pop_first - remove first node from LL
    def pop_first(self):
        popped_node = self.head
        self.head = self.head.next
        popped_node.next=None
        self.length -= 1
        return popped_node
    
    #delete last node from LL
    def pop(self):
        popped_node = self.tail
        temp= self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = temp
        temp.next = None
        self.length -= 1
        return popped_node
    
    #remove elements in particualr index 
    def Remove(self,index):
        if index == 0:
            return self.pop_first()
        prev_node = self.Get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all_node(self):
        self.head = None
        self.tail = None
        self.length = 0

LL= LinkedList()
#append node
LL.append(10)
LL.append(20)
LL.prepand(50)
LL.insert(20,3)
print(LL.Travers())
print(LL.Search(20))
print(LL.Get(0))
# print(LL.Set(0,70))
print(LL.pop_first())
print(LL.pop())
print(LL.Remove(1))
print(LL.delete_all())
print(LL)


