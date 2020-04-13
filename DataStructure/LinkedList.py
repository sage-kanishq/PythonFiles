class Node(object):
    data = None
    link = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtEnd(self, data):
        node = Node()
        node.data = data
        node.link = None

        if self.head == None:
            self.head = node
            self.size += 1 

        else:
            n = self.head
            while(n.link != None):
                n = n.link
            n.link = node
            self.size += 1 

    def show(self, pos='all'):
        if self.size == 0:
            print("Link is empty")
            return

        if(pos == "all"):
            n = self.head
            print("[",end="")
            while(n.link != None):
                print(f"{n.data}",end = ",")
                n = n.link
            print(n.data,end="")
            print("]")

        else:
            n = self.head
            for i in range(pos):
                n = n.link
            print(n.data)

    def delete(self,pos='last'):
        if pos==0:
            self.head=self.head.link

        if pos=='last':
            return self.delete(self.size-1)
        elif pos==1:
            n=self.head
            d=self.head.link
            n.link=d.link
            
        n=self.head
        for i in range(pos+1):
            n=n.link
            if i==pos-2:
                d=n
            if i==pos-1:
                d.link=n.link
        self.size-=1

    def insertAtPos(self,data,pos):
        node = Node()
        node.data = data
        node.link = None

        if self.head == None and pos==0:
            node.data=data
            node.link=self.head
            self.head = node
            self.size += 1  

        elif pos==0 and self.head!=None:
            node.data=data
            node.link=self.head
            self.head = node
            self.size += 1 

        elif pos>=self.size:
            n = self.head
            while(n.link != None):
                n = n.link
            n.link = node
            self.size += 1 

        elif pos == 1:
            n=self.head
            for i in range(pos+1):
                n = n.link
                if i == pos-1:
                    node.link=n
                    self.head.link= node
                    self.size+=1
                    
        else:
            n=self.head
            for i in range(pos+1):
                n = n.link
                if i==pos-2:
                    d=n
                if i == pos-1:
                    node.link=n
                    d.link= node
                    self.size+=1

a = LinkedList()
a.insertAtEnd(2)
a.insertAtEnd(2)
a.show()
