class Stack:
    def __init__(self): #initializer
        self.items = []
 
    def is_empty(self): #for checking whether our stack is empty or not
        return self.items == []
 
    def push(self, data): #for adding element to our stack
        self.items.append(data)
 
    def pop(self): #for popping/removing an element from the stack
        return self.items.pop()
    
    def returnstack(self): #for returning our stack at the end
        return self.items
 
 
s = Stack() #class object
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        print(s.returnstack())
        break
        