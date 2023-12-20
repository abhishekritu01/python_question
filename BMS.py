
import pandas as pd
from datetime import datetime
import os

class BakeryManagementSystem:

    def __init__(self):
        self.inventory = pd.DataFrame(columns=['Product', 'Quantity', 'Price'])
        self.sales = pd.DataFrame(columns=['Date', 'Product', 'Quantity', 'Total'])


    def display_menu(self):
        print("\n===== Bakery Management System Menu =====")
        print("1. Add Product to Inventory")
        print("2. Display Inventory")
        print("3. Make Sale")
        print("4. Display Sales Records")
        print("5. Export Inventory to Excel")
        print("6. Export Sales Records to Excel")
        print("7. Delete Product from Inventory")
        print("8. Update Product in Inventory")
        print("9. Search Product in Inventory")
        print("10. Exit")

    def add_product_to_inventory(self, product, quantity, price):
        # Add a new product to the inventory
        try:
            new_product = pd.DataFrame({'Product': [product], 'Quantity': [quantity], 'Price': [price]})
            self.inventory = pd.concat([self.inventory, new_product], ignore_index=True)
            print(f"{product} added to the inventory.")
        except Exception as e:
            print(f"Error adding product to inventory: {e}")


    def display_inventory(self):
        # Display the current inventory
        print("\nCurrent Inventory:")
        print(self.inventory)

    def make_sale(self, product, quantity):
        # Check if the product is available in the inventory
        if product not in self.inventory['Product'].values:
            print(f"{product} is not available in the inventory.")
            return

        # Check if there is enough quantity in the inventory
        available_quantity = self.inventory.loc[self.inventory['Product'] == product, 'Quantity'].values[0]
        if quantity > available_quantity:
            print(f"Insufficient quantity of {product} in the inventory.")
            return

        # Calculate the total cost of the sale
        price_per_unit = self.inventory.loc[self.inventory['Product'] == product, 'Price'].values[0]
        total_cost = quantity * price_per_unit

        # Update the inventory
        self.inventory.loc[self.inventory['Product'] == product, 'Quantity'] -= quantity

        # Record the sale
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_sale = pd.DataFrame({'Date': [date], 'Product': [product], 'Quantity': [quantity], 'Total': [total_cost]})
        self.sales = pd.concat([self.sales, new_sale], ignore_index=True)

        print(f"Sale recorded: {quantity} units of {product} for a total of ${total_cost}.")

    def display_sales(self):
        # Display the sales records
        print("\nSales Records:")
        print(self.sales)

    def export_inventory_to_excel(self, filename='inventory.xlsx'):
        # Ensure the filename has a proper extension
        _, file_extension = os.path.splitext(filename)
        if not file_extension:
            filename += '.xlsx'

        # Export the inventory to an Excel file
        try:
            self.inventory.to_excel(filename, index=False)
            print(f"Inventory exported to {filename}.")
        except Exception as e:
            print(f"Error exporting inventory to Excel: {e}")

    def export_sales_to_excel(self, filename='sales.xlsx'):
        # Ensure the filename has a proper extension
        _, file_extension = os.path.splitext(filename)
        if not file_extension:
            filename += '.xlsx'

        # Export the sales records to an Excel file
        try:
            self.sales.to_excel(filename, index=False)
            print(f"Sales records exported to {filename}.")
        except Exception as e:
            print(f"Error exporting sales records to Excel: {e}")

    def delete_product_by_id(self, product_id):
        # Delete a product from the inventory by its index
        try:
            index = int(product_id)
            product_name = self.inventory.loc[index, 'Product']
            self.inventory = self.inventory.drop(index)
            print(f"{product_name} deleted from the inventory.")
        except KeyError:
            print("Invalid product ID. Product not found.")
        except ValueError:
            print("Invalid product ID. Please enter a valid numeric ID.")
        except IndexError:
            print("Invalid product ID. Index out of range.")

    def update_product_by_id(self, product_id, new_quantity, new_price):
        # Update quantity and price of a product in the inventory by its index
        try:
            index = int(product_id)

            # Validate new_quantity
            if not new_quantity.isdigit():
                print("Invalid input for quantity. Please enter a valid integer.")
                return

            self.inventory.at[index, 'Quantity'] = int(new_quantity)
            self.inventory.at[index, 'Price'] = new_price
            print(f"Product updated in the inventory.")
        except (KeyError, ValueError, IndexError):
            print("Invalid product ID.")

    def search_product_by_id(self, product_id):
        # Search for a product in the inventory by its index
        try:
            index = int(product_id)
            product_info = self.inventory.loc[index]
            print(f"Product found in the inventory:\n{product_info}")
        except (KeyError, ValueError, IndexError):
            print("Invalid product ID.")

# Example Usage:
bakery_system = BakeryManagementSystem()

while True:
    bakery_system.display_menu()
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per unit: "))
        bakery_system.add_product_to_inventory(product, quantity, price)
    elif choice == '2':
        bakery_system.display_inventory()
    elif choice == '3':
        product = input("Enter the product name for the sale: ")
        quantity = int(input("Enter the quantity for the sale: "))
        bakery_system.make_sale(product, quantity)
    elif choice == '4':
        bakery_system.display_sales()
    elif choice == '5':
        filename = input("Enter the filename for the inventory export (default: inventory.xlsx): ") or 'inventory.xlsx'
        bakery_system.export_inventory_to_excel(filename)
    elif choice == '6':
        filename = input("Enter the filename for the sales export (default: sales.xlsx): ") or 'sales.xlsx'
        bakery_system.export_sales_to_excel(filename)
    elif choice == '7':
        product_id = input("Enter the product ID to delete: ")
        bakery_system.delete_product_by_id(product_id)
    elif choice == '8':
        product_id = input("Enter the product ID to update: ")
        new_quantity = input("Enter the new quantity: ")
        new_price = float(input("Enter the new price per unit: "))
        bakery_system.update_product_by_id(product_id, new_quantity, new_price)
    elif choice == '9':
        product_id = input("Enter the product ID to search: ")
        bakery_system.search_product_by_id(product_id)
    elif choice == '10':
        print("Exiting the Bakery Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
