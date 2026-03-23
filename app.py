
import csv
import os

# this list will store all customers. We create an empty list , which we will
customers = []        # keep all customers in this list.




# Function to add customers
def add_customer():
    name = input("Enter name: ").strip()
    # strip / lower =>  Remove extra spaces and convert the email to lowercase
    email = input("Enter email: ").strip().lower()

    if name == "":              # Make sure the customer name is not empty
        print("Name can not be empty.\n")
        return                   # Stop the function if the name is empty

    if "@" not in email or "." not in email:    # Validate the email format before saving the customer
        print("Invalid email address.\n")
        return                                  # Stop the function if the email is invalid

    for c in customers:
        if c["email"] == email:
            print("A customer with this email already exists.")
            return                              # Stop the function if the email is already in the list

    # this is an dictionary.  this is an information of a customer.
    customer = {"name": name, "email": email}

    # append() => add new item or customer to the end of the list.
    customers.append(customer)

    save_to_csv()     # save data after adding a customer

    print("Customer added!\n")


# Function to display all customers
def show_customers():
    if len(customers) == 0:
        print("No customers found.")
    else:
        count = 1                  # Start numbering customers from 1

        for c in customers:
            print(count, ". Name: ", c["name"], "| Email:", c["email"], sep="")
            count += 1               # Increase the counter for the next customer

    print("show customers\n")


# Function to search for a customer by name
def search_customer():
    search_name = input("Enter name to search: ").strip().lower()

    found = False         # it's flag.   use to track a condition.

    for c in customers:
        if c["name"].lower() == search_name:
            print("Found: ", c["name"], "|", c["email"])
            found = True    # it's flag.   use to track a condition.

    if not found:
        print("Customer not found")

    print("Search Customer\n")


# Function to update customer
def update_customer():
    search_name = input("Enter name to update: ").strip().lower()

    found = False     # it's flag.   use to track a condition.

    for c in customers:
        if c["name"].lower() == search_name:
            new_email = input("Enter new email: ").strip().lower()

            # Validate email format
            if "@" not in new_email or "." not in new_email:
                print("Invalid email address.")
                return            # Stop if email is invalid

             # Check duplicate email
            for other in customers:
                if other["email"] == new_email:
                    print("This email is already in use. ")
                    return        # Stop if email already exists

            c["email"] = new_email

            save_to_csv()     # save data after update

            print("Customer updated! \n")
            found = True     # it's flag.   use to track a condition. if found True means if name found,
            # it exit from loop. otherwise it will still searching inside the loop until find the name
            break

    if not found:
        print("Customer not found.\n")


# Function to delete a customer by name
def delete_customer():
    search_name = input("Enter name to delete: ").strip().lower()

    found = False

    for c in customers:
        if c["name"].lower() == search_name:
            # Delete: Remove data (e.g., delete a customer)
            customers.remove(c)

            save_to_csv()     # save after delete

            print("Customer deleted!\n")
            found = True
            break

    if not found:
        print("customer not found.\n")


# Function to print a separator line
def print_separator():
    print("-" * 30)


# Function to save customers to CSV file
def save_to_csv():
    with open("customers.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email"])

        writer.writeheader()  # write column names

        writer.writerows(customers)  # write all customer data


# Function to load customers from CSV file
def load_from_csv():
    if not os.path.exists("customers.csv"):
        return     # If file does not exist, do nothing

    with open("customers.csv", mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            customers.append(row)


load_from_csv()


while True:

    print("\nCustomer Campaign Manager")
    print("Total Customers:", len(customers))
    print_separator()
    print("1. Add Customer")
    print_separator()
    print("2. Show Customer")
    print_separator()
    print("3. Search Customer")
    print_separator()
    print("4. Update Customer")
    print_separator()
    print("5. Delete Customer")
    print_separator()
    print("6. Exit\n")

    # print(choice)
    choice = input("Select an option: ").strip()

    # Make sure the menu choice is valid before processing
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please enter a valid option from1 to 6. ")
        continue

    if choice == "1":    # create

        add_customer()

    elif choice == "2":  # Read     show customers

        show_customers()

    elif choice == "3":    # Read.     ##  search data   ##

        search_customer()

    # Update: Modify existing data (e.g., edit customer info)
    elif choice == "4":

        update_customer()

    elif choice == "5":       # Delete: Remove data (e.g., delete a customer)

        delete_customer()

    elif choice == "6":
        print("Exit program")
        break

    else:
        print("Invalid Option")


#                               ######  CRUD  ######
# Create: Add new data (e.g., add a new customer)
# Read: View or display existing data. search existing data (e.g., show customers)
# Update: Modify existing data (e.g., edit customer info)
# Delete: Remove data (e.g., delete a customer)
