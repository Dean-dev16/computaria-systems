#           Computaria Systems

print(" Welcome to Computaria Systems! ")

material = 0

while True:
    print(" Select the desired option: ")
    print("      1. Buy:  ")
    print("      2. Production: ")
    print("      3. Sale:    ")

    option = int(input("Choose an option from 1 to 3: "))

    if option == 0:
        break

    if option == 1:
        materials = {
            "sheets": 100, 
            "wires": 45,
            "cardboard": 60
        }

        print("Available Materials: ") 
        for item in materials:
            print("-", item) 
         
        purchase = input(" Which material do you want to buy: ").strip().lower()

        if purchase in materials:
            print(purchase, "selected")
        
            amount = int(input("Enter the quantity to buy: "))

            if amount <= materials[purchase]:
                print("Selected quantity: ", amount)
            else: 
                print('Insufficient stock!')

    if option == 2:
        product = int(input("Enter the quantity: "))

        if product > stock:
            print("Insufficient stock!!!")
        else:
            stock -= product
            product_stock += product
            print(f"Product quantity: {product_stock}")

    if option == 3:
        products = {
            "Notebook 1": 23, 
            "Notebook 2": 32
        }

        print(product)

        purchase1 = input(" How many products do you want to buy: ").strip().title()

        if purchase1 in products:
            print(purchase1, "selected")
        
            quantity = int(input("Enter the quantity to buy: "))

            if quantity <= products[purchase1]:
                print("Selected quantity: ", quantity)
            else: 
                print('Insufficient stock!')
        else:
            print("Product does not exist!") 

        finalized = input("Confirm purchase? ")

        if finalized.lower() == "yes":
            print("Purchase completed! Come back anytime.")
        else:
            print("Purchase canceled. Ending program...")
