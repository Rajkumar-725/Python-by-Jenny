# SILENT AUCTION PROGRAM
# note: the bid is not known anyone until the winner announces

bidder_data={}

print("***********WELCOME TO SILENT AUCTION PROGRAM************")
name = input("Enter your name: \t")
price = int(input("Enter your bid amount: \t"))

key = input("Any other bider data! Type 'yes' or 'no'")
while key=='yes':
    name = input("Enter your name: \t")
    price = int(input("Enter your bid amount: \t"))

    bidder_data[name] = price   #adding the values to dictionary (in key and value type)

    key = input("Any other bider data! Type 'yes' or 'no'")


# print(bidder_data)

# for i in bidder_data:
        
print(bidder_data)