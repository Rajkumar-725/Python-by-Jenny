"""
sets :stores data of same or different data_type.
     :same as list or tuple.
     :It uses curly braces {}
     :repetation of element is not allowed
     :It is unordered in nature.{maybe it change the element sequence while printed}
     :Indexing is not allowed (b/c indexing order )
     :Set elements are unchangable, but complete set can be mdified


"""

n1={"Raj", 34, True, 1}     #      Note: True and 1 are same.
n2 = { }        #empty set is not allowed like this.

# set is defined by 2 types: by curly braces or by set function.
n3=set()        #Here, you can make empty set like this (by using set function)     
n4=set("Geetu")     #It is also defined like this
print(n1)
print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))



print('\n\n\n')
#     :Set elements are unchangable, but complete set can be mdified
# n1[1]=40        #we can't modify
n1.add(99)      #Adds element in the selected set randomly

n1.add([1,2,3])     #We can't add list to a set b/c lists are mutable and sets are not.{we can add only immutable data}
print(n1)

print(len(n1))      #gives length of the set, it counts only unique value not repeated element.

n1.remove(99)       #used to delete the element. {If target value not present it gives Key Error}
n1.discard(98)       #used to delete the element. {If target value not present it doesn't gives any Key Error}

print(f"Value after remove {n1}")

print(n1.clear())   #deletes all the element in the set.
print(n1)


print('\n\n\n')
new_set={12, "Raj", "Geetu", "Ritu", "situ"}
print(new_set)
new_set.pop()       #deletes any ramdom item from the set, and also returns a value.
print(f"After removing {new_set}")
print(new_set.pop())    #It delets the element and also shows the deleted element