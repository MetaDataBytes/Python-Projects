class Product:
    def __init__(self, product_record: list) -> None:
        """
        PURPOSE: initilize a product object\n
        ARGUMENT: product_record: list of product attributes\n
        RETURN: None\n
        """
        self.__set_product_id(product_id=product_record[0])
        self.__set_coffee_type(coffee_type=product_record[1])
        self.__set_roast_type(roast_type=product_record[2])
        self.__set_size(size=product_record[3])
        self.__set_price(price=product_record[4])

    def get_product_id(self) -> int:
        """
        PURPOSE: get the product id\n
        ARGUMENT: None\n
        RETURN: the product id\n
        """
        return self.__product_id

    def get_coffee_type(self) -> str:
        """
        PURPOSE: get the coffee type\n
        ARGUMENT: None\n
        RETURN: the coffee type\n
        """
        return self.__coffee_type

    def get_roast_type(self) -> str:
        """
        PURPOSE: get the roast type\n
        ARGUMENT: None\n
        RETURN: the roast type\n
        """
        return self.__roast_type

    def get_size(self) -> str:
        """
        PURPOSE: get the size\n
        ARGUMENT: None\n
        RETURN: the size\n
        """
        return self.__size
    
    def print_product(self) -> None:
        """
        PURPOSE: print the product details\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        print(f"{self.get_product_id()}\t\t{self.get_coffee_type()} \t{self.get_roast_type()}\t\t{self.get_size()}\t\t${self.get_price()}")

    def get_price(self) -> str:
        """
        PURPOSE: get the price\n
        ARGUMENT: None\n
        RETURN: the price\n
        """
        return self.__price

    def __set_product_id(self, product_id: int) -> None:
        """
        PURPOSE: set the product id\n
        ARGUMENT: product_id: the product id\n
        RETURN: None\n
        """
        self.__product_id = product_id

    def __set_coffee_type(self, coffee_type: str) -> None:
        """
        PURPOSE: set the coffee type\n
        ARGUMENT: coffee_type: the coffee type\n
        RETURN: None\n
        """
        self.__coffee_type = coffee_type

    def __set_roast_type(self, roast_type: str) -> None:
        """
        PURPOSE: set the roast type\n
        ARGUMENT: roast_type: the roast type\n
        RETURN: None\n
        """
        self.__roast_type = roast_type

    def __set_size(self, size: int) -> None:
        """
        PURPOSE: set the size\n
        ARGUMENT: size: the size\n
        RETURN: None\n
        """
        self.__size = size

    def __set_price(self, price: float) -> None:
        """
        PURPOSE: set the price\n
        ARGUMENT: price: the price\n
        RETURN: None\n
        """
        self.__price = price