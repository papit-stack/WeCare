#function to get product
def get_product():
    """
    Reads product data from a file and returns it as a dictionary.

    The function attempts to open a file named 'product.txt' in read mode.
    Each line in the file is expected to contain product information 
    separated by commas. These lines are read and split into lists, and stored in a dictionary with incremental integer keys 
    starting from 1 and returns a dictionary
    """
    try:
        file = open("product.txt", "r") #open file in read mode
    except FileNotFoundError:
        print("Error: 'product.txt' file not found.")    #when file not found
    dlist={}                        #Dictionary to hold product data
    data=file.readlines()
    p_id=1                          #Product ID counter
    for line in data:
        line = line.replace("\n","").split(",")
        dlist[p_id] = line  # Store each line as list in dictionary
        p_id=p_id+1
    return dlist
