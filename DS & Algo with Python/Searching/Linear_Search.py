
"""Linear Search is a Sequential Search in Which one key is given to use to find it in the array or List of elements.
Linear Search Approach is nothing but it is a technique of comparing one by one element to the key that given to use,
while comaparing the list elements if key found in list, then position or index of the
founded elements will be returned as output """

#This code is written by Manendra Nath Shukla
#Let's cook our code for Linear Search Algorithm

class LinearSearch:
    def __init__(self):
        self.arr=[]

    def append(self,data):
        self.arr.append(data)

    def find(self,key):
        f=0                      #flag variable to activate if found else remains same if not 
        for i in range(len(self.arr)):
            if(self.arr[i]==key):       #comparing one by one element of list to key 
                f=1
                return ("Element found at %d position"%(i))     #if found return index with some msg
        if(f==0):
            return "Element Not Found"
    def show(self):
        print(*self.arr,sep=" ")
        

if __name__=="__main__":            #driver program for LinearSearch 
    myArr=LinearSearch()
    t=True
    while t:
        print("*"*50)
        print("               Linear Search Dashboard")
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
    
    
            
