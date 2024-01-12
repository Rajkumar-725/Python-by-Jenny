'''
list :collection of elements, separated by comma
     :It is just like dynamically sized array.
     :It can stores elements of same as well as of different data_types
     :duplicates are also allowed (2 elements--> same)
    
     
     :mutable in nature; after creating list we can modify it.
'''

name = ["Raj","Rahul"]
roll_no = [1,45,2,6,]
mixed = ["Raj", 32, True, 10.10]    #mixed list

print(name)
print(name[1])
print(roll_no[3])
print(roll_no[-1])      #it starts from end point
print(roll_no[-2])

print("\n\n\n")


                                            # LIST SLICING
    #       syntax:    list_name[starting_index : upto_length]
    
numbers=[1,2,3,4,5,6,7,8,9,20,12,29,34,15,11]
print(numbers[0:5])
print(numbers[2:4])
print(numbers[:4])      #default starting_index=0
print(numbers[3:])      #default upperlength=total length of list


print("\n\n\n")
    #       syntax:    list_name[starting_index : upto_length : skip_steps]       
print(numbers[::1])         #jump 1 step
print(numbers[::2])         #jump 2 step
print(numbers[1:5:2])


print("\n\n\n")
                                        #SORTING
#   .sort   :used to sort the given list in ascending order
#           :doesn't apply on mixed list.
print(numbers.sort())       #it prints nothing as it doesn't return anyhthing.
numbers.sort()
print(numbers)


print('\n\n\n')
                                        #REVERSE
#   .reverse    :reverses the list.
numbers.reverse()
print(numbers)


print('\n\n\n')
                                    #MAXIMUM AND MINIMUM
#   max  :finds maximum among list.
#   min  :finds minimum among list.
print(max(numbers))
print(min(numbers))



print('\n\n\n\n\n')
                                #   ADDING IN LIST
'''
append  :It adds element at the end of the list (one element at a time)
         syntax:   listname.append(element_to_add)

insert  :It adds element at a specific index in list.   (one element at a time)
        syntax:    listname.insert(index_no, element_to_add)

extend  :It adds multiple element at the end of the list at a time
        syntax:    listname.extend([elements_to_add_separated_by_comma])
'''                                
num=[1,2,3,4,5]
print(num)

num.append(23)
print(f"list after append {num}")

num.insert(2, 40)
print(f"list after insert {num}")

num.extend([101,102,103,104])
print(f"list after extend {num}")



print('\n\n\n\n')
                                    #MODIFY LIST
                            # syntax:   list_name[index_to_change]=new_value
num1=[1,2,3,4,5,6,7]
print(num1)

num1[1]=100     #replace 1st index value by 100
print(num1)

num1[2:5]=[201,202,203]     #it replces 3 elements starting from 2nd index upto length 5
print(num1)


print('\n\n\n\n\n')
'''             #REMOVING OR DELETION OF ELEMENT
   .remove() :used to remove elements from the list
   syntax  :list_name.remove(item_you_wnt_to_remove)
           note: It removes only 1 letter at a time

    .pop()    :it remove the last element (it also return the removed element)       
'''
num2=[501,502,503,504,505,506]
print(num2)

num2.remove(502)
print(f"remove function {num2}")

num2.pop()
print(f"pop function {num2}")
print(num2.pop())       #It deletes and shows the element that is deleted

num2.pop(2)         #It removes by indexing (removes the element that is at 2nd index)
print(num2)
print(num2.pop())
print(num2)



print('\n\n\n')
#   .count  :It counts how many times the target value is +nt in the list.
num3=[0,1,1,2,2,4,4,4,4,4,6,6]
n=num3.count(4) 
print(n)


