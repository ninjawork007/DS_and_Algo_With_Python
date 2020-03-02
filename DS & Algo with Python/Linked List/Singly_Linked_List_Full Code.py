'''program is written by Manendra Nath Shukla
ADT for Linked List All operation is included in it to understand the
operations of the linked list easily

'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None


    def createNode(self,data):
        self.head=Node(data)


    def display(self):
        temp=self.head
        if(temp is None):
            print("Empty Linked List")
        else:
            l=[]
            while(temp is not None):
                l.append(temp.data)
                temp=temp.next
            print(*l,sep=" ")

    def Length(self):
        cnt=0
        temp=self.head
        while(temp is not None):
            cnt+=1
            temp=temp.next
        print(cnt)


    def prepend(self,data):
        new_node=Node(data)
        temp=self.head
        self.head=new_node
        new_node.next=temp


    def append(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
        else:
            temp=self.head

            while(temp.next is not None):
                temp=temp.next

            temp.next=new_node


    def displayRev(self):
        temp=self.head
        if(temp is None):
            print("Empty Linked List")
        else:
            l=[]
            while(temp is not None):
                l.append(temp.data)
                temp=temp.next
        for i in l[::-1]:
            print(i,end=' ')
        print()


    def Reverse(self):
        prev=None
        curr=self.head
        while(curr.next):
            temp= curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr.next=prev
        self.head=curr
        



    def InsertAtPos(self,data,pos):
        temp=self.head;cnt=0;prev=Node(data)
        new=Node(data)
        if (pos==0):
            self.head=Node(data)
        while(temp):
            cnt+=1
            prev=temp
            temp=temp.next
            if(cnt==pos):
                prev.next=new
                new.next=temp
            
            
            


    def Search(self,data):
        temp=self.head
        cnt=1;flag=0
        while(temp.next is not None):
            if(temp.data==data):
                print("Searched data Found at %d Node"%(cnt))
                flag=1
                break
            else:
                temp=temp.next
                cnt+=1
        if(flag==0):
            print("Data Not Found  in the list")



    def DeleteFirst(self):
        if(self.head is None):
            print("Underflow")
        if(self.head.next is None):
            self.head=None
        else:
            self.head=self.head.next 



    def DeletePos(self,pos):
        temp=self.head;
        if(pos==0):
            self.head=self.head.next
        while(pos-1>0):
            self.head=self.head.next
            pos-=1
        self.head.next=self.head.next.next



    def DeleteLast(self):
        temp=self.head
        if(temp is None):
            print("Underflow")
        if(self.head.next is None):
            self.head=None
        else:
            while(temp.next is not None):
                prev=temp
                temp=temp.next
            prev.next=None
            
                
        
        
    def Sort(self):
        temp1=self.head
        cnt=0
        while(temp1.next is not None):
            cnt+=1
            temp1=temp1.next
        print(cnt)   
        for i in range(0,cnt):
            temp=self.head
            for j in range(0,cnt-i):
                if(temp.data>temp.next.data):
                    temp.data,temp.next.data=temp.next.data,temp.data
                temp=temp.next
                
        
            
            
        
        



if __name__=="__main__":
    ch=True
    myLis=LinkedList()

    while(ch):
        print("-"*50)
        print(" "*13 + "Dashboard For LinkedList")
        print("-"*50)
        print("1.Create LinkedList")
        print("2.Insert at First")
        print("3.Insert at Position")
        print("4.Insert at Last")
        print("5.Display LinkedList")
        print("6.Search Node")
        print("7.Reverse the LinkedList")
        print("8.Display Reverse ")
        print("9.Length of LinkedList")
        print("10.Delete FirstNode")
        print("11.Delete Node at Pos")
        print("12.Delete LastNode")
        print("13.Sort The LinkedList")
        print("14.Exit")
        print("*"*50)
        c=(int(input("Enter Your Choice: ")))
        if(c==1):
            print("Creating LinkedList:")
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
            print("Your LinkedList Data Are :")
            myLis.display()
        if(c==6):
            print("Searching Node in List")
            data=input("Enter data to search in the list: ")
            myLis.Search(data)

        if(c==7):
            print("Reversing the Linked List")
            myLis.Reverse()
            print("Linked List Reversed Successfully")
        if(c==8):
            print("Displaying the LinkedList Data Reversly")
            myLis.displayRev()
        if(c==9):
            print("Length of the Linked List")
            myLis.Length()
        if(c==10):
            print("Deleting First Node ")
            myLis.DeleteFirst()
            print("First Node Deleted Successfully")
        if(c==11):
            print("Deleting Positioned Node ")
            pos=int(input("Enter the Node Position to be Deleted: "))
            myLis.DeletePos(pos)
            print("%d Node Deleted Successfully"%(pos))
        if(c==12):
            print("Deleting Last Node ")
            myLis.DeleteLast()
            print("Last Node Deleted Successfully")

        if(c==13):
            print("Sorted LinkedList")
            myLis.Sort()
        if(c==14):
            ch=False
