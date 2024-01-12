
menu ={
    "latte":
    {
        "ingredients":{
            'water':80,
            'milk':30,
            'coffee':10,
        },
    'cost': 150
    },

    "espresso":
    {
        "ingredients":{
            'water':100,
            'milk':60,
            'coffee':30,
        },
    'cost': 150
    },

    "latte":
    {
        "ingredients":{
            'water':60,
            'milk':40,
            'coffee':20,
        },
    'cost': 150
    }
}

resources = {
    'water': 500,
    'milk': 400,
    'coffee':100,
}

profit =0       #initially profit is set to zero
is_machine_on = True
while is_machine_on==True:
    choice = input("What would you like to have? (latte/ espresso/ cappuccino)")
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        print(f"Water = {resources['water']} ml")
        print(f"Milk = {resources['milk']} ml")
        print(f"Coffee = {resources['coffee']} g")
        print(f"Total money = Rs. {profit}")
