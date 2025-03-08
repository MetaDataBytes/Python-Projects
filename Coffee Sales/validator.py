class Validator:
    def is_customer(self, customer_record: list) -> bool:
        """
        PURPOSE: Confirm there is only one customer in the customer_record\n
        ARGUMENT: customer_record: the attributes of all customers that share the provided email\n
        RETURN: True: There is one and only one customer record, False: there are zero or more than one customer records\n
        """
        if len(customer_record) == 1: return True
        elif len(customer_record) == 0: return False
        else: return self.duplicate_emails_found_error()

    def duplicate_emails_found_error(self) -> bool:
        """
        PURPOSE: print the error that more than one customer share the same email\n
        ARGUMENT: None\n
        RETURN: False: do not allow the user to login\n
        """
        print("ERROR: Email belongs to more than one user. Contact admin")
        return False