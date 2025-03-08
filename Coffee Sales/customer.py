from product import Product

class Customer:
    def __init__(self, customer_record: list) -> None:
        """
        PURPOSE: initilize the customer object
        ARGUMENT: customer_record: list of customer attributes
        RETURN: None
        """
        self.__set_customer_id(customer_id=customer_record[0])
        self.__set_first_name(first_name=customer_record[1])
        self.__set_last_name(last_name=customer_record[2])
        self.__set_email(email=customer_record[3])
        self.__set_phone_number(phone_number=customer_record[4])
        self.__set_member_status(member_status=customer_record[5])
        self.__set_street_address(street_address=customer_record[6])
        self.__set_city(city=customer_record[7])
        self.__set_zip_code(zip_code=customer_record[8])
        self.__set_shopping_cart()

    def get_customer_id(self) -> str:
        """
        PURPOSE: get the customer's id\n
        ARGUMENT: None\n
        RETURN: The customer id\n
        """
        return self.__customer_id

    def get_first_name(self) -> str:
        """
        PURPOSE: get the customer's first name\n
        ARGUMENT: None\n
        RETURN: The customer's first name\n
        """
        return self.__first_name
     
    def get_last_name(self) -> str:
        """
        PURPOSE: get the customer's last name\n
        ARGUMENT: None\n
        RETURN: The customer's last name\n
        """
        return self.__last_name
    
    def get_email(self) -> str:
        """
        PURPOSE: get the customer's email\n
        ARGUMENT: None\n
        RETURN: The customer's email\n
        """
        return self.__email
    
    def get_phone_number(self) -> str:
        """
        PURPOSE: get the customer's phone number\n
        ARGUMENT: None\n
        RETURN: The customer's phone number\n
        """
        return self.__phone_number
    
    def get_member_status(self) -> bool:
        """
        PURPOSE: get the customer's membership status\n
        ARGUMENT: None\n
        RETURN: The customer's membership status\n
        """
        return bool(self.__member_status)

    def get_street_address(self) -> str:
        """
        PURPOSE: get the customer's street address\n
        ARGUMENT: None\n
        RETURN: The customer's street address\n
        """
        return self.__street_address

    def get_city(self) -> str:
        """
        PURPOSE: get the customer's city\n
        ARGUMENT: None\n
        RETURN: The customer's city\n
        """
        return self.__city

    def get_zip_code(self) -> str:
        """
        PURPOSE: get the customer's zip code\n
        ARGUMENT: None\n
        RETURN: the customer's zip code\n
        """
        return self.__zip_code

    def get_shopping_cart(self) -> list:
        """
        PURPOSE: get the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: the customer's shopping cart\n
        """
        return self.__shopping_cart

    def add_to_shopping_cart(self, product: Product) -> None:
        """
        PURPOSE: add a product to the customer's shopping cart\n
        ARGUMENT: product: the product to add to the shopping cart\n
        RETURN: None\n
        """
        self.__shopping_cart.append(product)

    def remove_from_shopping_cart(self, product: Product) -> None:
        """
        PURPOSE: remove a product from the customer's shopping cart\n
        ARGUMENT: product: the product to remove from the shopping cart\n
        RETURN: None\n
        """
        self.__shopping_cart.remove(product)

    def clear_shopping_cart(self) -> None:
        """
        PURPOSE: clear the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.__shopping_cart.clear()

    def goodbye(self) -> None:
        """
        PURPOSE: display a goodbye message to the member\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        print(f"Thank you for visiting Justin's Coffee House! Have a wonderful day!")

    def __set_customer_id(self, customer_id: int) -> None:
        """
        PURPOSE: set the customer's id\n
        ARGUMENT: customer_id: the customer's id
        RETURN: None
        """
        self.__customer_id = customer_id

    def __set_first_name(self, first_name: str) -> None:
        """
        PURPOSE: set the customer's first name\n
        ARGUMENT: the customer's first name\n
        RETURN: None\n
        """
        self.__first_name = first_name

    def __set_last_name(self, last_name: str) -> None:
        """
        PURPOSE: set the customer's last name\n
        ARGUMENT: the customer's last name\n
        RETURN: None\n
        """
        self.__last_name = last_name

    def __set_email(self, email: str) -> None:
        """
        PURPOSE: set the customer's email\n
        ARGUMENT: the customer's email\n
        RETURN: None\n
        """
        self.__email = email

    def __set_phone_number(self, phone_number: str) -> None:
        """
        PURPOSE: set the customer's phone number\n
        ARGUMENT: the customer's phone number\n
        RETURN: None\n
        """
        self.__phone_number = phone_number

    def __set_member_status(self, member_status: bool) -> None:
        """
        PURPOSE: set the customer's membership status\n
        ARGUMENT: the customer's membership status\n
        RETURN: None\n
        """
        self.__member_status = member_status

    def __set_street_address(self, street_address: str) -> None:
        """
        PURPOSE: set the customer's street address\n
        ARGUMENT: the customer's street address\n
        RETURN: None\n
        """
        self.__street_address = street_address

    def __set_city(self, city: str) -> None:
        """
        PURPOSE: set the customer's city\n
        ARGUMENT: city: the customer's city\n
        RETURN: None\n
        """
        self.__city = city

    def __set_zip_code(self, zip_code: str) -> None:
        """
        PURPOSE: set the customer's zip_code
        ARGUMENT: zip_code: the customer's zip code
        RETURN: None
        """
        self.__zip_code = zip_code

    def __set_shopping_cart(self) -> None:
        """
        PURPOSE: set the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.__shopping_cart = list()