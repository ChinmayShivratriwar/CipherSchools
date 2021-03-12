global lst
lst = []

def start():
    try:
        budget = int(input("Enter the Budget: "))


        print("1.Add Item")

        print("2.Exit")
        while True:
            option = int(input("\nEnter your option : "))
            if option == 1:
                budget = addItem(budget)

            elif option == 2:
                printLst(lst)
                break

    except ValueError:
        print("Enter Integer Value and Try Again ")
        exit(0)

def addItem(budget):
    amount_left = budget
    try:
        product = input("Enter Product: ").strip()
        quantity = float(input("Enter Quantity: "))
        price = int(input("Enter Price : "))

        if  amount_left == 0:
            print("Budget is 0 , you cannot buy anymore ")
            return


        if price > amount_left:
            print("You cant buy that item")
        else:
            lst.append([product,quantity , price])


            amount_left = budget - price

        print("Budget Left : " + str(amount_left))
        return amount_left

    except ValueError:
        print("Enter Proper Values and Try Again")
        exit(0)

def printLst(lst):
    print("Product          Quantity           Price")
    for i in lst:
        print()
        for j in i:
            print(j , end="          ")

start()