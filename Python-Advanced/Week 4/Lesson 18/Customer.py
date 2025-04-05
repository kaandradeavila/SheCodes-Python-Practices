class Customer:
  """
  This class initializes a new customer object with the given customer data.
  """

  def __init__(self, customer):
    """
    This method initializes a new customer object with the given customer data.
    """
    self.customer = customer
    self.customer_id = customer[0]
    self.customer_first_name = customer[2]
    self.customer_last_name = customer[3]
    self.customer_email = customer[9]

  def format_customer_info(self):
    """
    This method returns a string with the customer's information formatted with the customer's ID, first name, last name, and email.
    """
    customer_info = f"Customer #{self.customer_id}, {self.customer_first_name} {self.customer_last_name}, {self.customer_email}"
    return customer_info
