import json
def add():
    fd = open("record.json",'r')
    r = fd.read()
    fd.close()
    record = json.loads(r)
    c = int(input("Enter your choice:\n_____________________\n(1)- Add new item\n(2)- Restock\n"))
    if c == 1:  
    prod_id = str(input("Enter product id:"))
    name = str(input("Enter name:"))
    pr = int(input("Enter price:"))
    qn = int(input("Enter quantity:"))

    record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
      
    print("New item added successfully!")

    elif c == 2:
    prod_id = str(input("Enter product id:"))
    qn = int(input("Enter quantity:"))

    record[prod_id]['qn'] = record[prod_id]['qn'] + qn

    print("Restock successful!")
    
    data = json.dumps(record)
    fd = open("record.json",'w')
    fd.write(data)
    fd.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
        main()
    else:
        exit()
        
ef update():
    fd = open("record.json",'r')
    r = fd.read()
    fd.close()
    record = json.loads(r)
    prod_id = str(input("Enter the product ID of the item to be updated:"))
    name = str(input("Enter new name:"))
    pr = int(input("Enter new price:"))
    qn = int(input("Enter new quantity:"))

    record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
        
    print("Updated successfully!")

    js = json.dumps(record)

    fd = open("record.json",'w')
    fd.write(js)
    fd.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
        main()
    else:
        exit()
        
def delet():
    fd = open("record.json",'r')
    r = fd.read()
    fd.close()
    record = json.loads(r)
    d = str(input("Enter the product ID of the item to be deleted:\n"))
    del record[d]

    print("Deletion succesful!")

    js = json.dumps(record)

    fd = open("record.json",'w')
    fd.write(js)
    fd.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
        main()
    else:
        exit()
        
def purchase():
    fd = open("record.json",'r')
    record_data = fd.read()
    fd.close()
    records= json.loads(record_data)
    ui_prod  = input("Enter the product_Id: ")
    ui_quant = int(input("Enter the quantity: "))

    if (records[ui_prod]['qn']>=ui_quant):
        print("Product: ", records[ui_prod]['name'])
        print("Price: ", records[ui_prod]['pr'])
        print("Billing Amount: ", records[ui_prod]['pr'] * ui_quant)
        print("Please Visit Again ")
        records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant

        fd = open("record.json",'w')
        data = json.dumps(records)
        fd.write(data)
        fd.close()

        sales_file = open("sale.json",'r')
        sales_data= sales_file.read()
        sales_file.close()
        record= json.loads(sales_data)
        # sales = {}
        sales[len(sales)+1] = {'id' : ui_prod, 'name' : records[ui_prod]['name'], 'pr' : records[ui_prod]['pr'], 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}
        
        sales_file = open("sale.json",'w')
        sales_data= json.dumps(sales)
        sales_file.write(sales_data)
        sales_file.close()
        CHOICE = input('Enter y to continue or n to exit: ')
        if CHOICE == 'y':
            main()
        else:
            exit()
    else:
        print(" Sorry! We have only "+str(records[ui_prod]['qn'])+" Products")

def viewProducts():
    fd = open("record.json",'r')
    record= fd.read()
    records= json.loads(record)
    print("*********** ALL PRODUCTS **************")
    print("Product Id\t" ,"Product Name\t","Price\t","Quantity\t")
    for i in records.keys():
        print(i,"\t\t",records[i]['name'],"\t\t",records[i]['pr'],"\t\t",records[i]['qn'],"\t")
    fd.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
        main()
    else:
        exit()
        
def salesReport():
    sales = open("sale.json",'r')
    data = sales.read()
    records= json.loads(data)
    print("************SOLD PRODUCTS***************")
    print("Sl No.\tProduct Id\tProduct Name\t\tPrice\t\tQuantity\tTotal Amount")
    for i in records.keys():
      print(i,"\t",records[i]['id'],"\t\t",records[i]['name'],"\t\t",records[i]['pr'],"\t\t",records[i]['qn'],"\t\t",records[i]['amount'])

    sales.close()
    CHOICE = input('Enter y to continue or n to exit: ')
    if CHOICE == 'y':
        main()
    else:
        exit()
        
def main():
    print('===============================')
    print('= Inventory Management System =')
    print('===============================')
    print('(1) Add New Item')
    print('(2) Update Item')
    print('(3) Delete Item')
    print('(4) Buy Item')
    print('(5) View All Items')
    print('(6) Print Sales Report')
    print('(7) Quit')
    CHOICE = int(input("Enter choice: "))
    if CHOICE == 1:
        add()
    elif CHOICE == 2:
        update()    
    elif CHOICE == 3:
        delet()    
    elif CHOICE == 4:
        purchase()
    elif CHOICE == 5:
        viewProducts()      
    elif CHOICE == 5:
        salesReport()
    elif CHOICE == 5:
        exit()
    else:
        print("Invalid Choice!")
        
main()