class Node():
    data = None
    link = None
    follow = None

class DblLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def insertAtEnd(self, data):
        node = Node()
        node.data = data
        node.link = None

        if self.head == None:
            node.follow = None
            self.head = node
            self.tail = node
            self.size += 1 

        else:
            n = self.head
            while(n.link != None):
                n = n.link
            n.link = node
            node.follow = n
            self.tail = node
            self.size += 1 

    def show(self, pos='all'):
        if self.size == 0:
            print("Link is empty")
            return

        if(pos == "all"):
            n = self.head
            while(n.link != None):
                print(n.data)
                n = n.link
            print(n.data)

        elif pos == 'rev':
            n = self.tail
            while(n.follow != None):
                print(n.data)
                n = n.follow
            print(n.data)


        else:
            n = self.head
            for i in range(pos):
                n = n.link
            print(n.data)

    def delete(self,pos='last'):
        if pos==0:
            self.head=self.head.link
            self.head.follow = None

        if pos=='last':
            return self.delete(self.size-1)

        elif pos==1:
            n=self.head
            d=self.head.link
            n.link=d.link
            n.link.follow = n

        elif pos==self.size-1:
            n=self.head
            for i in range(pos+1):
                n=n.link
                if i==pos-2:
                    d=n
                if i==pos-1:
                    d.link = n.link
                    # d.follow = n.follow
                    self.tail = d
                    # n.link.follow = d
            self.size-=1

        else:
            n=self.head
            for i in range(pos+1):
                n=n.link
                if i==pos-2:
                    d=n
                if i==pos-1:
                    d.link=n.link
                    d.link.follow = d 
            self.size-=1

    def insertAtPos(self,data,pos):
        node = Node()
        node.data = data

        if self.head == None and pos==0:
            node.data=data
            node.link=self.head
            self.head = node
            self.tail = node
            self.size += 1  

        elif pos==0 and self.head!=None:
            node.data=data
            node.link=self.head
            self.head.follow = node
            self.head = node
            self.size += 1 

        elif pos>=self.size:
            n = self.head
            while(n.link != None):
                n = n.link
            n.link = node
            node.follow = n
            self.tail = node
            self.size += 1 

        elif pos == 1:
            n=self.head
            n.link.follow = node
            node.follow = n
            node.link = n.link
            n.link = node             

        else:
            n=self.head
            for i in range(pos+1):
                n = n.link
                if i==pos-2:
                    d=n
                if i == pos-1:
                    d.link.follow = node
                    node.link = d.link
                    d.link= node
                    node.follow = d
                    self.size+=1