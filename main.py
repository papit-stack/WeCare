from read import get_product
from operation import sale_product,restock_product

#Initial welcome print statements
print("\n")
print("                              WeCare Wholesale                                   \n")
print("                Kamalpokhari, Kathmandu | Phone: 011-4890709                     ")
print("\n         Welcome to the system, Admin! Wishing you a productive day.             ")
print("\n")

#Main function to run program
def main():
    """
    Main function to run the WeCare Wholesale inventory management system.
    This function displays a welcome message and presents a menu with options 
    for the admin.
    """
    product_data=get_product()
    while True:
        print("\n---- WeCare Skin ----")
        print("1. Sale Product")
        print("2. Restock Product")
        print("3. EXIT")

        try:
            choice = int(input("Enter from above option: "))
        except ValueError:
            print("Invalid input Please enter number")
            continue
        
        if choice==1:
            sale_product(product_data)
        elif choice==2:
            restock_product(product_data)
        elif choice==3:
            print("Thanks for using the system. Wishing you a great day, Admin!")
            break
        else:
            print("Invalid input! Please choose a valid option from the menu.\n")

#Run the main function
main()

