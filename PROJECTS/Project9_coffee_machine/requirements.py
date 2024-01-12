"""
        *****************COFFEE MACHINE REQUIREMENTS********************
1.      Ask from user for coffee type by prompting:
        "What would you like to have ?(latte/espresso/cappuccino)"
        Onece the drink is dispensed this prompt should  be shown to serve the next customer.
    
2.      When user enters "report" as an input then a report should be generated the shown the currnet resources value:
            eg: Water =200ml
                Milk =50ml
                Coffee =75g
                Money = Rs. 150

3       If user enters "off" as an input then your program should and execution.

4       Check sufficient resources are available or not.

5       If sufficient resources are available then machine should ask to insert coins and calculate total money received.
              [Coffee machine only receives  5rs, 10rs and 20rs coin]

6.      Check payment is successful or not
        If user has entered sufficient money, the cost of drink gets added to the machine as peofit.
        If user has entered too much money, machine should offer change to the user.
        If money is not suffient to purchase the drink user has selected, it shold print a message "Sorry! That's not enough money. Money refunded"

7.      Make coffee
        If payment is successful, ingredients to make the selected drink should be duducted from the cofee machine resourses. 
        And it will print a messageb "Here is your cappuccino." (If cappuccino was their choice)
"""