class Customer:
    def __init__(self, customer_record: list[str]) -> None:
        """
        PURPOSE: initilize the customer object
        ARGUMENT: customer_record: list of customer attributes
        RETURN: None
        """
        self.__customer_id = customer_record[0]
        self.__first_name = customer_record[1]
        self.__last_name = customer_record[2]
        self.__email = customer_record[3]
        self.__phone_number = customer_record[4]
        self.__street_address = customer_record[5]
        self.__city_id = customer_record[6]
        self.__loyalty_status = customer_record[7]
    
    def get_customer_id(self) -> str:
        """
        PURPOSE: get the customer's id\n
        ARGUMENT: None\n
        RETURN: The customer id\n
        """
        return self.__customer_id
    
    def set_first_name(self, first_name: str) -> None:
        """
        PURPOSE: set the customer's first name\n
        ARGUMENT: the customer's first name\n
        RETURN: None\n
        """
        self.__first_name = first_name

    def get_first_name(self) -> str:
        """
        PURPOSE: get the customer's first name\n
        ARGUMENT: None\n
        RETURN: The customer's first name\n
        """
        return self.__first_name

    def set_last_name(self, last_name: str) -> None:
        """
        PURPOSE: set the customer's last name\n
        ARGUMENT: the customer's last name\n
        RETURN: None\n
        """
        self.__last_name = last_name
     
    def get_last_name(self) -> str:
        """
        PURPOSE: get the customer's last name\n
        ARGUMENT: None\n
        RETURN: The customer's last name\n
        """
        return self.__last_name
    
    def set_email(self, email: str) -> None:
        """
        PURPOSE: set the customer's email\n
        ARGUMENT: the customer's email\n
        RETURN: None\n
        """
        self.__email = email
    
    def get_email(self) -> str:
        """
        PURPOSE: get the customer's email\n
        ARGUMENT: None\n
        RETURN: The customer's email\n
        """
        return self.__email
    
    def set_phone_number(self, phone_number: str) -> None:
        """
        PURPOSE: set the customer's phone number\n
        ARGUMENT: the customer's phone number\n
        RETURN: None\n
        """
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        """
        PURPOSE: get the customer's phone number\n
        ARGUMENT: None\n
        RETURN: The customer's phone number\n
        """
        return self.__phone_number
    
    def set_address(self, street_address) -> None:
        """
        PURPOSE: set the customer's street address\n
        ARGUMENT: the customer's street address\n
        RETURN: None\n
        """
        self.__street_address = street_address

    def get_street_address(self) -> str:
        """
        PURPOSE: get the customer's street address\n
        ARGUMENT: None\n
        RETURN: The customer's street address\n
        """
        return self.__street_address
    
    def get_city_id(self) -> str:
        """
        PURPOSE: get the customer's city id\n
        ARGUMENT: None\n
        RETURN: The customer's city id\n
        """
        return self.__city_id
    
    def set_loyalty_card(self, loyalty_status: bool) -> None:
        """
        PURPOSE: set the customer's loyalty status\n
        ARGUMENT: the customer's loyalty status\n
        RETURN: None\n
        """
        self.__loyalty_status = str(int(loyalty_status))
    
    def get_loyalty_status(self) -> bool:
        """
        PURPOSE: get the customer's loyalty status\n
        ARGUMENT: None\n
        RETURN: The customer's loyalty status\n
        """
        return bool(self.__loyalty_status)
