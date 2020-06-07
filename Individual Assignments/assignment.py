lastname = input("Enter your surname: ")
firstname = input("Enter your firstname: ")
Othername = input("Enter your other name: ")
gender = input("Your gender, If 'Male' type 'M' and for 'Female' type 'F': ")
phonenum = (input("Enter your phone number here: "))

#fullname = lastname + ' ' + firstname + ' ' + Othername

age = int(input("How old are you?: "))
if age>18:
    print("{} your are welcome to Fashion Designer Mini Store".format(firstname.upper()))
else:
    print("Sorry, you didn't meet our requirement.")

# Products and their prices
product = {
            "Perfume": 3800,"Gel": 450,"Soft8": 240,
            "Shampoo": 3000,"Hair drier":10000,
            "Makeup Kits":30000,"Releaser":1000,
            "Hair Grower":5000, "Eyelashes":2500,"Lotion":4000
}
'''
# Request for user's entry
a =input("Select the product you want to purchase: ")
if a in product:
    print("They price is {} {}".format(product,product[a]))
    print("{} thank you for your patronage".format(lastname.upper()))
else:
    print("Product is not available for now. Please Check back in 2days time")
'''
total = 0
item = "Y"
#the loop will repeat while the user types Y when asked if they want to 
#enter another item
while item == "Y":
    #asks the user to enter an item
    number = input("Enter an item to add to the total: ")
    if number in product:
        print("They price is {} {}".format(product,product[number]))
        print("{} thank you for your patronage".format(lastname.upper()))
    else:
        print("Product is not available for now. Please Check back in 2days time")
    
    #adds the item entered to the total cost
    total = total + product[number]
    #asks the user if they want to enter another item
    item = input("Do you want to enter another item? Y/N ")
#after the loop ends it outputs the total
print("The total cost of the items selected is " + str(total))
print("{} thanks for patronage".format(lastname.upper()))