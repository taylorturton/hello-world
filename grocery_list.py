# Create an empty dictionary 
grocery_list = {}

# Add items to the dictionary with quantities
grocery_list["Apples "] = 5
grocery_list["Chocolate "] = 2
grocery_list["Cereal "] = 10

# Print the initial grocery list
print("Initial Grocery List: ")
for item, quantity in grocery_list.items():
    print(item, quantity)

# Display a message for the user
print("Compile your grocery list. Type 'stop' when you are finished.")

# Keep adding items until the user decides to stop
while True:
    new_item = input("Enter new item: ")
    if new_item.lower() == 'stop':
        break

    new_quantity = input("Enter quantity: ")
    if new_quantity.lower() == 'stop':
        break
    
    new_quantity = int(new_quantity)

    # Add the new item and quantity to the grocery_list dictionary
    grocery_list[new_item] = new_quantity
    

# Print the updated grocery list
print("Updated Grocery List: ")
for item, quantity in grocery_list.items():
    print(item, quantity)
