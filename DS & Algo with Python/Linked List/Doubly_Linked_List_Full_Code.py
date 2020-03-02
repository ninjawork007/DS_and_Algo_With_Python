# This program is written by Manendra Nath Shukla to under the basic concept of the
# how doubly linked list is working

# so let's begin our journey ...
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        
        
    def prepend(self,data):
        '''if self.head is None:
            new_node = Node(data)
            self.head = new_node
            #print("node inserted")
            return'''
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    
    def append(self,data):
        temp=self.head
        new=Node(data)
        if(temp is None):
            self.head=new
            return 
        while(temp.next is not None):
            temp=temp.next
        temp.next=new
        new.prev=temp
        new.next=None
        
            
        
    def deleteFirst(self):
        if(self.head is None):
            print("UnderFlow")
            return
        self.head=self.head.next

    def deleteLast(self):
        if(self.head is None):
            print("UnderFlow")
            return
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.prev.next=None
        
    def reverse(self):
        if(self.head is None):
            print("List is Empty")
            return
        temp=self.head
        while(temp is not None):
            temp.next,temp.prev=temp.prev,temp.next
            self.head=temp
            temp=self.head.prev
        
            
    def createNode(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
    def InsertAtPos(self,data,pos):
        pass
    def deletePos(self):
        pass
    def Length(self):
        cnt=1
        temp=self.head
        while(temp.next is not None):
            cnt+=1
            temp=temp.next
        print("List have %d nodes"%cnt)
    def sort(self):
        pass

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def Search(self,data):
        pass
    def displayRev(self):
                    


if __name__=="__main__":
    ch=True
    myLis=DoublyLinkedList()

    while(ch):
        print("#"*55)
        print(" "*13 + "Dashboard For Doubly LinkedList")
        print("#"*55)
        print("1.Create DoublyLinkedList")
        print("2.Insert at First")
        print("3.Insert at Position")
        print("4.Insert at Last")
        print("5.Display DoublyLinkedList")
        print("6.Search Node")
        print("7.Reverse the DoublyLinkedList")
        print("8.Display Reverse ")
        print("9.Length of DoublyLinkedList")
        print("10.Delete FirstNode")
        print("11.Delete Node at Pos")
        print("12.Delete LastNode")
        print("13.Sort The DoublyLinkedList")
        print("14.Exit")
        print("*"*55)
        c=(int(input("Enter Your Choice: ")))
        if(c==1):
            print("Creating DoublyLinkedList:")
            data=input("Enter the data :")
            myLis.createNode(data)
            print("Linked List Successfully Created")
        if(c==2):
            print("Inserting Node at First")
            data=input("Enter data to be inserted at First Pos")
            myLis.prepend(data)
            print("Node Successfully Inserted at Head")
        if(c==3):
            print("Inserting Postioned Node")
            pos=int(input("Enter postion: "))
            data=input("Enter data to be Inserted: ")
            myLis.InsertAtPos(data,pos)
            print("Node inserted at pos %d Successfully"%(pos))

        if(c==4):
            print("Inserting Node to last")
            data=input("Enter the data to be Inserted at Last: ")
            myLis.append(data)
        if(c==5):
            print("Your DoublyLinkedList Data Are :")
            myLis.display()
        if(c==6):
            print("Searching Node in List")
            data=input("Enter data to search in the list: ")
            myLis.Search(data)

        if(c==7):
            print("Reversing the DoublyLinkedList")
            myLis.reverse()
            print("List Reversed Successfully")
        if(c==8):
            print("Displaying the DoublyLinkedList Data Reversly")
            myLis.displayRev()
        if(c==9):
            print("Length of the DoublyLinkedList")
            myLis.Length()
        if(c==10):
            print("Deleting First Node ")
            myLis.deleteFirst()
            print("First Node Deleted Successfully")
        if(c==11):
            print("Deleting Positioned Node ")
            pos=int(input("Enter the Node Position to be Deleted: "))
            myLis.deletePos(pos)
            print("%d Node Deleted Successfully"%(pos))
        if(c==12):
            print("Deleting Last Node ")
            myLis.deleteLast()
            print("Last Node Deleted Successfully")

        if(c==13):
            print("Sorted DoublyLinkedList")
            myLis.Sort()
        if(c==14):
            ch=False

            
        
