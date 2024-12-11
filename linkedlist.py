class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end="")
            if temp.next != None:
                print(" -> ",end="")
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return
        temp,i = self.head,0
        while i < index:
            temp = temp.next
            i += 1
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def  remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        else:
            pre_node = self.get(index-1)
            removed_node = pre_node.next
            pre_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node


    def reverse(self):
        if self.length==0 or self.length==1:
            return None
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            after = temp.next
            while temp is not None:
                after = temp.next
                temp.next = before
                before =temp
                temp = after
ll = LinkedList()

while True:
    
    print("""
          1.insert elementt at first: 
          2.insert element at last:
          3.insert element at specific place:
          4.remove element at last: 
          5.remove element at first:
          6.remove a specific element:
          7.fetch an element at a index:
          8.print the list:
          9.change value at a index:
          10.reverse the list:
          11.quit
          """)
    uip = input("Enter Your choice: ")
    match int(uip):
        case 1:
            ll.append(int(input("Enter a number: ")))
        case 2:
            ll.prepend(int(input("Enter a number: ")))
        case 3:
            index = int(input("Enter the index: "))
            num = int(input("Enter the number: "))
            ll.insert(index,num)
        case 4:
            ele = ll.pop()
            if ele is None:
                print("No element at last: ")
            else:
                print("removed element is : ", ele.value)
        case 5:
            ele = ll.pop_first()
            if ele is None:
                print("No element at first: ")
            else: 
                print("removed element is : ", ele.value)
        case 6:
            ele = ll.remove(int(input("Enter the index to remove an element: ")))
            if ele is None:
                print("No element at the given index: ")
            else:
                print("removed element is : ", ele.value)
        case 7:
            index = ll.get(int(input("Enter the index to get an element: ")))
            print("element is : ", ele," at index: ",index)
        case 8:
            ll.print_list()
        case 9:
            index = int(input("Enter the index: "))
            num = int(input("Enter the new number: "))
            ll.set_value(index,num)
        case 10:
            ll.reverse()
        case 11:
            break
        case _:
            print("Invalid option")


            


