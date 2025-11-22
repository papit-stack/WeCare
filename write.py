#Function to print and generate sale invoice
def print_save_sale_bill(customer_name,phone_number,date_and_time,user_sell_items,shipping_cost,total,formatted_date_and_time):
    
    """    
    The function displays the sales bill on the console and saves the same content
    to a text file named using the customer name and timestamp. The bill includes
    customer information, date and time, item details (name, quantity, free units, 
    unit price, and total per item), shipping cost (if applicable), and the grand total.
    """
        
    #Printing bill on screen
    print("\n\t \t \t \t\t Product Shop Bill ")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 011-4890709 ")
    print("\n")
    print("Customer Details:")
    print("====================================================")
    print("Customer Name : " + customer_name.capitalize())
    print("Contact number: " + phone_number)
    print("Purchase Date : " + str(date_and_time.date()))
    print("Purchase Time : "+  str(date_and_time.time()))
    print("====================================================")
    print("\n")
    print("-----------------------------------------------------------------------------")
    print("|\t\t\t\tPurchase Detail's\t\t\t    |")
    print("-----------------------------------------------------------------------------")
    print("Item Name \t\t Quantity \t Free \t Unit Price \t Total\t    |")
    print("-----------------------------------------------------------------------------")
    for i in user_sell_items:
        print(i[0] + "\t\t  " + str(i[1]) + "\t\t " + str(i[4]) + "\t  " + str(i[2]) + "\t\t" + " $" + str(i[3])+"\t    |")
    print("-----------------------------------------------------------------------------")
    if shipping_cost > 0:
       print("Shipping Cost: $" + str(shipping_cost)+"\t\t\t\t\t\t\t    |")
    print("Grand Total: $" + str(total)+"\t\t\t\t\t\t\t    |")
    print("-----------------------------------------------------------------------------")
    print("\n")
    #Saving bill to a text file
    filename="Sale_invoice_"+customer_name.capitalize()+"_"+ formatted_date_and_time
    file = open(filename + ".txt", "w")
    file.write("\n\t \t  Product Shop Bill \n")
    file.write("\n")
    file.write("\t  Kamalpokhari, Kathmandu | Phone No: 011-4890709 \n")
    file.write("\n")
    file.write("Customer Details:\n")
    file.write("====================================================\n")
    file.write("Customer Name : " + customer_name.capitalize()+"\n")
    file.write("Contact number: " + phone_number+"\n")
    file.write("Purchase Date : " + str(date_and_time.date())+"\n")
    file.write("Purchase Time : "+  str(date_and_time.time())+"\n")
    file.write("====================================================\n")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------\n")
    file.write("|\t\t\t\tPurchase Detail's\t\t\t    |\n")
    file.write("-----------------------------------------------------------------------------\n")
    file.write("Item Name \t\t Quantity \t Free \t Unit Price \t Total\t    |\n")
    file.write("-----------------------------------------------------------------------------\n")
    for i in user_sell_items:
       file.write(i[0] + "\t\t  " + str(i[1]) + "\t\t " + str(i[4]) + "\t  " + str(i[2]) + "\t\t" + " $" + str(i[3])+"\t    |\n")
    file.write("-----------------------------------------------------------------------------\n")
    if shipping_cost > 0:
       file.write("Shipping Cost: $" + str(shipping_cost)+"\t\t\t\t\t\t\t    |\n")
    file.write("Grand Total: $" + str(total)+"\t\t\t\t\t\t\t    |\n")
    file.write("-----------------------------------------------------------------------------\n")
    file.write("\n")
    file.close()
    print("Sale invoice generated successfully.Filename:",filename)




#Function to print and generate restock invoice file    
def print_save_restock_bill(supplier_name, phone_number, date_and_time, restock_item, total,formatted_date_and_time):

    '''
    The function displays the restocking bill on the console and saves the same 
    information to a text file named using the supplier name and a timestamp.
    It includes supplier details, date of restocking, and a list of items restocked 
    with their name, quantity, cost price, and total. The final section includes the grand total.
    '''
        
    # Printing bill on screen
    print("\n\t \t Product Restock Bill ")
    print("\n")
    print("\t Kamalpokhari, Kathmandu | Phone No: 011-4890709 ")
    print("\n")
    print("====================================================")
    print("Supplier Name : " + supplier_name.capitalize())
    print("Contact number: " + phone_number)
    print("Restock Date : " + str(date_and_time.date()))
    print("====================================================")
    print("\n")
    print("---------------------------------------------------------------")
    print("\t Restock Product Bill\t\t\t\t" + "      |")
    print("---------------------------------------------------------------")
    print("Item Name \t\tQuantity\tCost Price\tTotal |")
    print("---------------------------------------------------------------")
    for i in restock_item:
        print(i[0] + "\t\t  " + str(i[1]) + "\t\t " + str(i[2]) +"\t\t"+str(i[3])+"  |")
        print("---------------------------------------------------------------")
    print("Grand Total: $" + str(total)+"\t\t\t\t\t      |")
    print("---------------------------------------------------------------")
    print("\n")
    print("Product restocked successfully!\n")
    
    #Saving bill to a text file
    filename="Restock_invoice_"+supplier_name.capitalize()+"_"+ formatted_date_and_time
    file = open(filename + ".txt", "w")
    file.write("\n\t \t Product Restock Bill \n")
    file.write("\n")
    file.write("\t Kamalpokhari, Kathmandu | Phone No: 011-4890709\n ")
    file.write("\n")
    file.write("====================================================\n")
    file.write("Supplier Name : " + supplier_name.capitalize()+"\n")
    file.write("Contact number: " + phone_number+"\n")
    file.write("Restock Date : " + str(date_and_time.date())+"\n")
    file.write("====================================================\n")
    file.write("\n")
    file.write("---------------------------------------------------------------\n")
    file.write("\t Restock Product Bill\t\t\t\t" + "      |\n")
    file.write("---------------------------------------------------------------\n")
    file.write("Item Name \t\tQuantity\tCost Price\tTotal |\n")
    file.write("---------------------------------------------------------------\n")
    for i in restock_item:
        file.write(i[0] + "\t\t  " + str(i[1]) + "\t\t " + str(i[2]) +"\t\t"+str(i[3])+"  |\n")
        file.write("---------------------------------------------------------------\n")
    file.write("Grand Total: $" + str(total)+"\t\t\t\t\t      |\n")
    file.write("---------------------------------------------------------------\n")
    file.write("\n")
    file.close()
    print("Restock invoice generated successfully.Filename:",filename)
    
