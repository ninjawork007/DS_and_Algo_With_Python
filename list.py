

"""
Written By: Manendra Nath Shukla
Program Name: List Example Program

""" 
# first of all create a empty list 
print("Creating a List")
mylist = []
# append some values in empty list using append() method
print("Appending some values in list")
mylist.append(5);mylist.append(2);mylist.append(10)

print("Printing mylist : ",mylist) # [5,2,10]
#insert() method can be used to insert value at begining 
print("inserting value at begining")
mylist.insert(0,15)
print("After inserting at begining")
print(mylist) # [15,5,2,10]

# len() used to find the length of list 
print("Length of the list : %d"%(len(mylist))) # 4

# display list elements 
print("Printing all elements of list one by one ")
for i in mylist:
    print(i)

#count() returns occurrences of element in a list 

print("No of 2 in List : %d"%(mylist.count(2))) # 1

# insert() Inserts Element to The List at particular position 

print("inserting")
mylist.insert(len(mylist),25)
print(mylist)

# sort() return sorted list
print("Sorting the list") 
mylist.sort()  # [2,5,10,15,25]
print(mylist)
# remove() Remove item from list
print("removing 5 from list")
mylist.remove(5)
print(mylist)
# reverse() Reverses a list
print("Reversing the list ") 
mylist.reverse()

print("Reversed list :") 
print(mylist) # [25,15,10,2]

print("Sum of the list Elements:%d"%(sum(mylist)))

print("Largest Element of of the List :%d"%(max(mylist)))
print("Smallest Element of of the List :%d"%(min(mylist)))

#list() used to convert obejct into list 
print("list created using list() method by passing a string")
s="MyThingsWork"
print(list(s))  #['M','y','T','h','i','n','g','s','W','o','r','k']




