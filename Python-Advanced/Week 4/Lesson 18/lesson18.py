import csv

from Customer import Customer

# Opening CSV file with customer data and reading it
with open('Python-Advanced/Week 4/Lesson 18/customers.csv', 'r') as file:
  customers = csv.reader(file)

  # Printing the information of each customer in the CSV file
  for customer in customers:
    new_customer = Customer(customer)
    customer_information = new_customer.format_customer_info()
    print(customer_information)
