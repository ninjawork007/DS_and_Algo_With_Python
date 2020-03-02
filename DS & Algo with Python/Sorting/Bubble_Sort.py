"""
    Bubble Sort is a simplest sorting technique in which it compare the adjacent
    elements by making as bubble as theortically.
    If adjacent are in wrong order then they will get swapped each other
    it will complete the sorting process in passess ...
    Time Complexity:O(N^2)
    Space Complexity:O(1)
"""
#This code is Written by Manendra Nath Shukla

#Let's Cook Our Code for Bubble Sort

class BubbleSort:
    def __init__(self):         #creating a empty list to store the data in it
        self.lis=[]

1

    def append(self,data):
        self.lis.append(data)


        #Bubble Sorting algorithm implementation
    def sort(self):
        n=len(self.lis)
        for j in range(0,n):
            for i in range(0,n-j-1):
                if(self.lis[i]>self.lis[i+1]):# If they are in wrong order ....
                    self.lis[i+1],self.lis[i]=self.lis[i],self.lis[i+1]     #swapping the adjacent elements
        
        
    def show(self):
        print(*self.lis,sep=" ")
        

if __name__=="__main__":            #driver program for Bubble Sorting 
    Arr=BubbleSort()
    t=True
    while t:
        print("-"*50)
        print("               Bubble Sorting Dashboard")
        print("-"*50)
        print("1.Insert Elements in List")
        print("2.Sort using Bubble Sort")
        print("3.Print List")
        print("4.Exit")
        ch=int(input("Enter your choice:"))
        if(ch==1):
            d=input("Enter data to be inserted in List:")
            Arr.append(d)
            print("Data inserted successfully")
        if(ch==2):
            Arr.sort()
            print("List is sorted Successfull")

        if(ch==3):
            Arr.show()
        if(ch==4):
            t=False
    
    
            

