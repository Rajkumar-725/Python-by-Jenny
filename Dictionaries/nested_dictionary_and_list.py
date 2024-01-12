'''
                NESTED LIST AND DICTIONARIES
        nest list into dictionary as well as nest dictionary into dictionary

nested dictionary: dictionary within a dictionary.

'''

name={
    'college':{"kcc":5657, "cse":7777, "electrical":8888},      #dictionary within a dictionary.
    "Geeta": {"section":1111, "subject":8888, "age":40}         #dictionary within a dictionary.
}
print(name)     #accessing whole elements of dictionary 'name
print(name["Geeta"])    #access the value of 'geeta' only
print(name["Geeta"]["age"])   #accessing dictionary within a dictionary

print('\n\n\n')
name["Geeta"]["phone"]=9153864      #adding into dictionary
print(name)

del name["college"]["electrical"]       #deleting the value inside dicionary
print(name)



#LIST WITHIN A DICTIONARY
print('\n\n\n\n')
travel_data={
    "gujarat": ["dwaraka","somnath", "statue"], #list within a dictionary.
    "rajasthan": ["jaipur","udaipur"]
}
print(travel_data)
print(travel_data["gujarat"])   


print('\n\n\n\n')
#DICTIONARY WITHIN LIST
name1=[
    {'name':"kcc", 
     "roll":0000, 
     "cse":7777, 
     "electrical":8888
    },
    {'name':"Geeta", 
     "section":1111, 
     "subject":8888, 
     "age":40
    }         #dictionary within a dictionary.
]
print(name1)    #accessing list
print(name1[0])     #accessing individual element of list by indexing.
print(name1[1])     #accessing individual element of list by indexing.
print(name1[1]["subject"])     #accessing individual element of dictionary.
