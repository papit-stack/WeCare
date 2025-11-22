from write import print_save_sale_bill,print_save_restock_bill
from datetime import datetime


#Function to display product information
def display_product(product_data,double_price=False):
    
    '''
    Displays the product details from the provided dictionary.
    Depending on the double_price flag, it either shows the original cost price (for restocking)
    or the selling price (double the cost price, for sales).
    '''
    
    id=1        #product id counter
    print("\n------------------------------       Product  Detail's   -------------------------------\n")
    print("ID      Name                     Brand             Quantity         Price           Country\n")
    for id,product in product_data.items():
        product_id=id
        Name=product[0]
        Brand=product[1]
        Quantity=product[2]
        if double_price==True:
            Price=int(product[3])*2        #Displaying for sale_product
        else:
            Price=int(product[3])          #Displaying for restock product 
        Country=product[4]
        print(  product_id,"\t"+Name+"\t\t"+Brand+"\t     "+Quantity+"\t    "+str(Price)+"\t    "+Country+"\n")
        

#Function to update product detail in 'product.txt'
def update_product_detail(product_data):
    file=open('product.txt','w')
    for values in product_data.values():
        file.write(values[0] + "," + values[1] + "," + str(values[2]) + "," + str(values[3]) + "," + values[4] + "\n")  #writes in file
    file.close()


#Function to sale product
def sale_product(product_data):
    """
    Handles the product sale process for a customer.

    Allows the admin to:
    - View available products with selling prices
    - Select products to sell
    - Apply a "Buy 3, Get 1 Free" offer
    - Automatically deduct stock based on sales
    - Optionally include shipping costs
    - Collect and validate customer details
    - Generate and save a sales invoice
    """
    
    user_sell_items = []    #List to hold items purchased by customer
    total = 0.0               # Total bill
    shipping_cost = 0       #initialize shipping cost
    while True:
        display_product(product_data,True)    # Show product list with selling price

        #Product ID input and validation
        try:
            product_id=int(input("Please, Enter a  product Id to sell or 0 to exit: "))
        except:
            print("\nInvalid Input.Please Enter a Number")
            continue
        if product_id==0:
            break
        if product_id<0 or product_id>len(product_data):
            print("\nPlease provide a valid product ID !!!")
            continue

        #Product quantity input and validation
        try:
            product_quantity=int(input("Enter product quantity you want to sale: "))
            if product_quantity<0:
                print("Quantity must be positive.")
                continue
            elif product_quantity==0:
                print("Quantity cannot be zero.")
                continue
        except:
            print("\nInvalid Input.Please enter a number")
            continue
        
        # Calculating free items (Buy 3 get 1 free offer)
        item_quantity=int(product_data[product_id][2])
        free_item=int(product_quantity/3)
        total_quantity=product_quantity+free_item

        #check if quantity is sufficient
        if total_quantity>item_quantity:
            print("Insufficient quantity.Try again")
            continue
        
        #Updating stock
        product_data[product_id][2] = str(int(product_data[product_id][2]) - total_quantity)

        #Calculating amount
        name_of_product = product_data[product_id][0]
        unit_price = int(product_data[product_id][3]) * 2
        total_price = unit_price *  product_quantity
        total+=total_price
        
        # Inform customer about free items
        print("We are having buy 3 get one free offer,hence you have received",free_item,"("+name_of_product+") items for free.")

        # Storing purchased items
        user_sell_items.append([name_of_product, product_quantity, unit_price, total_price, free_item])#2D list

        
        # Asking if customer wants to buy more
        sell_option = input("\nDo you want to sale more items? (Y/N): ").lower()
        print("\n")
        if sell_option== "y" or sell_option == "yes":
            continue
        else:
            break
        
    #if any item is sold
    if len(user_sell_items)!=0:
        #customer name validation
        while True:
            customer_name=input("Enter Customer Name: ")
            if not customer_name:#if customer name is empty
                print("Customer name cannot be empty. Please enter a valid name.")

            else:
                break
        #phone number validation
        while True:
            phone_number = input("Enter Phone Number: ")
            if not phone_number:
                print("Phone number cannot be empty. Please enter a valid phone number.")
            elif not phone_number.isdigit():
                print("Phone number must contain only digits. Please enter a valid phone number.")
            elif len(phone_number)!=10:
                print("Phone number must be 10 digits. Please enter a valid phone number.")
            else:
                break
        
        #shipping process
        ship_option=input("Do you want your products to be shipped? (Y/N): ").lower()
        if ship_option=="y"or ship_option=="yes":
            customer_location=input("Enter location: ").lower()
            if customer_location=="kathmandu":
                shipping_cost=500
            else:
                shipping_cost=1000
            total+=shipping_cost
            
        #updating stocks in file
        update_product_detail(product_data)
        
        #date and time
        date_and_time = datetime.now()
        formatted_date_and_time=str(date_and_time.year)+str(date_and_time.month)+str(date_and_time.day)+"_"+str(date_and_time.hour) +str(date_and_time.minute)+str(date_and_time.second)
        
        print_save_sale_bill(customer_name,phone_number,date_and_time,user_sell_items,shipping_cost,total,formatted_date_and_time)

#Function to restock product
def restock_product(product_data):
    '''
    Manages restocking of existing products or addition of new products.

    Allows the admin to:
    - Add stock to existing products
    - Introduce new products with full details
    - Optionally update cost prices
    - Validate user inputs throughout the process
    - Collect and validate supplier details
    - Generate and save a restock invoice
    '''
    
    restock_item=[]
    total=0.0
    new_product=False
    display_product(product_data,False)
    while True:
        # Taking product ID to restock
        try:
            restock_id = int(input("Enter the ID of the product you want to restock or 0 to exit: "))
        except ValueError:
            print("Invalid Restock Id")
            continue
        
        if restock_id==0:
            if not restock_item:  # Nothing restocked yet
                return
            else:
                break
        
        if restock_id<0:
            print("\nPlease provide a valid restock ID !!!")
            continue
        
        if restock_id not in product_data:
            name = input("Enter product name: ")
            brand = input("Enter brand: ")
            new_product=True
            #product quantity validation
            while True:
                try:
                    restock_quantity=int(input("Enter product quantity: "))
                    if restock_quantity<=0:
                        print("Quantity must be greater than zero.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    
            #cost price validation       
            while True:
                try:
                    cost_price=int(input("Enter cost price: "))
                    if cost_price<=0:
                        print("Price must be greater than zero")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number")
                    
            country=input("Enter country: ")
            product_data[restock_id]=[name.capitalize(),brand.capitalize(),str(restock_quantity),cost_price,country.capitalize()]




        #product id exist    
        else:
            new_product=False
            #quantity to restock
            try:
                restock_quantity=int(input("Enter  quantity you want to restock: "))
                if restock_quantity<0:
                    print("Quantity must be positive.")
                    continue
                elif restock_quantity==0:
                    print("Quantity cannot be zero.")
                    continue
            except:
                print("\nInvalid Input.Please enter a number")
                continue
            while True:    
                #cost option
                cost_option=input("Do you want to update cost price? (Y/N): ").lower()
                print("\n")
                if cost_option== "y" or cost_option == "yes":
                    #new cost price
                    try:
                       new_price_input = input("Enter new cost price (press Enter to keep current): ")
                       if new_price_input=="":
                           break
                       #new price
                       new_price=int(new_price_input)
                       if new_price>0:
                         product_data[restock_id][3]=new_price
                       break
                    except:
                       print("\nInvalid Input.Please enter a number.")
                       continue
                else:
                  break
        #if not new product then update stock        
        if new_product==False:
            product_data[restock_id][2] = str(int(product_data[restock_id][2]) +restock_quantity )
            
        total_price=int(product_data[restock_id][3])*restock_quantity
        total+=total_price
        restock_item.append([product_data[restock_id][0],restock_quantity,product_data[restock_id][3],total_price,total])
        #restock option
        restock_option=input("Do you want to restock more item? (Y/N): ").lower()
        if restock_option=="y" or restock_option=="yes":
            continue
        else:
            break
    
    
    #suplier name validation
    while True:
        supplier_name=input("Enter Supplier Name: ")
        if not supplier_name:#if customer name is empty
            print("Supplier name cannot be empty. Please enter a valid name.")
        else:
            break
    
    #phone number validation
    while True:
        phone_number = input("Enter Phone Number: ")
        if not phone_number:
            print("Phone number cannot be empty. Please enter a valid phone number.")
        elif not phone_number.isdigit():
            print("Phone number must contain only digits. Please enter a valid phone number.")
        elif len(phone_number)!=10:
            print("Phone number must be 10 digits. Please enter a valid phone number.")
        else:
            break
    
    #date and time
    date_and_time = datetime.now()
    formatted_date_and_time=str(date_and_time.year)+str(date_and_time.month)+str(date_and_time.day)+"_"+str(date_and_time.hour) +str(date_and_time.minute)+str(date_and_time.second)


    #updating value in file   
    update_product_detail(product_data)
    print_save_restock_bill(supplier_name, phone_number, date_and_time, restock_item, total,formatted_date_and_time)

