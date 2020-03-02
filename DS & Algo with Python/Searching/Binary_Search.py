"""Binary Search is a divide and conquer Searching technique to find the element in a list or array with
    O(LogN) time complexity.
    it only works on sorted array or list
    -->> Dividig the problem in two half part , searching the key based on the median value,
        if median value >  key , searching element may be present in 1st part  else in 2nd part.
        else Not present in the list.

"""
#This Code is Written by Manendra Nath Shukla

#Let's Cook our code for Binary Search

class BinarySearch:
    def __init__(self):
        self.arr=[]

    def append(self,data):
        self.arr.append(data)

    def find(self,key):
        
        flag=0            #flag variable to activate if found else remains same if not 
        l=0;r=len(self.arr)-1  # assigning left and right index variable to iterate over list list

        while(r>=l):
            m=(l+r)//2      #finding median index of list 
            if(self.arr[m]<key):     #comparing median value with key 
                l=m+1
            if(self.arr[m]==key):
                flag=1
                return("Element found at position %d"%m)        #if found then it will return msg 
            if(self.arr[m]>key):
                r=m-1
        if(flag==0):
            return("Element not found in List")             #if not found it will return msg 
                
        
    def show(self):
        print(*self.arr,sep=" ")
        

if __name__=="__main__":            #driver program for LinearSearch 
    myArr=BinarySearch()        
    t=True
    while t:
        print("*"*50)
        print("               Binary Search Dashboard")
        print("*"*50)
        print("1.Insert Elements in List")
        print("2.Search your Data")
        print("3.Print List")
        print("4.Exit")
        ch=int(input("Enter your choice:"))
        if(ch==1):
            d=input("Enter data to be inserted in List:")
            myArr.append(d)
            print("Data inserted successfully")
        if(ch==2):
            k=input("Enter data to search in list:")
            print(myArr.find(k))
        if(ch==3):
            myArr.show()
        if(ch==4):
            t=False
    
