from database_functions import Database
from customer import Customer

DB = Database()
print("Welcome to Java_Coffee_House!\n\nPlease sign in!", end="\n\n")
email = input("Email: ")
customer = DB.execute_sql_statement(sql='proc_CUSTOMER_LOG_IN', arguments=(email,))
if customer: 
    customer = Customer(customer_record=customer[0])
    print(f"Welcome, {customer.get_first_name()}")
else: print("User Not Found!")