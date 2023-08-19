#operation on stack using list with limit

class Stack:
    def __init__(self,maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return'\n'.join(values)
    
    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
  
    def push(self,value):
        if self.isFull():
            return True
        else:
            self.list.append(value)
            return "Inseted"
    
    def pop(self):
        if self.isEmpty():
            return "List is empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "List is empty"
        else: 
            # self.list.pop()
            return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None


stackResult = Stack(4)
stackResult.push(1)
stackResult.push(2)
stackResult.push(3)
print(stackResult.isEmpty())
print(stackResult.isFull())
# print(stackResult)
# print(stackResult.pop())
# print(stackResult.peek())
# print(stackResult.delete())
print(stackResult)
