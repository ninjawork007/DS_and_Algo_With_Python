"""Implementaion of  Queue using Linked List
   Working principle of the Queue is FIFO (First In First Out)
"""
#This program is Witten by Manendra Nath Shukla

#Now Let's cook our code for Queue

class QueueNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None


    def Enqueue(self,data):
        new=QueueNode(data)
        if(self.head is None):
            self.head=new
        else:
            new.next=self.head
            self.head=new

    def Dequeue(self):
        if(self.head is None):
            print("Queue Underflow")
            return False
        t=self.head.next
        if(t is None):
            self.head=None
            return True
        else:
            prev=None
            temp=self.head
            while(temp is not None):
                prev=temp
                temp=temp.next
            prev.next=None
            return True
            
            
    def get_Queue(self):
        if(self.head is None):
            print("Queue is Empty")
            return 
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
    def Length(self):
        cnt=1
        temp=self.head
        while(temp.next is not None):
            cnt+=1
            temp=temp.next
        print("Queue have %d Elements"%cnt)
        
        
if __name__ == "__main__":          #driver program
    t=True

    myQueue=Queue() #Creating Queue object to perform action on it
       
   # ch=True
    while(t):   #iterating always
        print("*"*50)                                   #Designing Dashboard for Queue for Easy Access of Operation
        print("                  Queue Dashboard          ")
        print("*"*50)
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Display Queue Elements")
        print("4.Length")
        print("5.Exit")
        ch=int(input("Enter Your Choice:"))
        if(ch==1):
            d=input("Enter Element to be Enqueue in Queue:")
            myQueue.Enqueue(d)
            print("Data inserted in queue Successfully")
        if(ch==2):
            d=myQueue.Dequeue()
            if(d==True):
                print("Data removed from queue Sucessfully")
                
        if(ch==3):
            print("Queue Elements are:")
            myQueue.get_Queue()
        if(ch==4):
            myQueue.Length()
        if(ch==5):
            t=False
            
