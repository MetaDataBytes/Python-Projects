from validator import Validator
from customer import Customer
from database import Database
from product import Product
from member import Member
import sys

class app:
    def __init__(self):
        """
        PURPOSE: initilize and run the coffee sales application\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.validator = Validator()
        self.database = Database()
        self.customer = self.__get_customer()
        self.products = self.__get_products()
        self.__main_menu()
        self.__quit()
    
    def __get_customer(self) -> Customer:
        """
        PURPOSE: initilize the customer object\n
        ARGUMENT: email: the customer's email\n
        RETURN: the customer object\n
        """
        print("Enter your email to sign in: ")
        if (email := input("Email: ").strip().lower()) != "quit":
            if self.validator.is_customer(customer_record=(customer_record := self.database.get_customer(email=email))): 
                if customer_record[0][5]: return Member(customer_record=customer_record[0])
                else: return Customer(customer_record=customer_record[0])
            else: print("User Not Found!")
        self.__quit()

    def __get_products(self) -> list[Product]:
            """
            PURPOSE: get the products from the database\n
            ARGUMENT: None\n
            RETURN: a list of product objects\n
            """
            return [Product(product_record=product_record) for product_record in self.database.get_products()]

    def __main_menu(self) -> None:
        """
        PURPOSE: display the main menu to the user\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        print(f"\nWelcome to Justin's Coffee House, {self.customer.get_first_name().title()} {self.customer.get_last_name().title()}!")
        main_menu = {"0": "quit",
                     "1": "view sorted products",
                     "2": "view searched products",
                     "3": "manage shopping cart"}
        
        self.__get_menu_selection(menu_name="Main Menu", menu=main_menu)

    def __sorting_menu(self) -> None:
        """
        PURPOSE: display the sorting menu to the user\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        sorting_menu = {"0": "return to main menu",
                        "1": "view products by id",
                        "2": "view products by coffee type",
                        "3": "view products by roast type",
                        "4": "view products by size",
                        "5": "view products by price"}
        
        self.__get_menu_selection(menu_name="Sorting Menu", menu=sorting_menu)

    def __searching_menu(self) -> None:
        """
        PURPOSE: display the searching menu to the user\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        searching_menu = {"0": "return to main menu",
                          "1": "search for products by coffee type",
                          "2": "search for products by roast type"}
        self.__get_menu_selection(menu_name="Searching Menu", menu=searching_menu)

    def __shopping_menu(self) -> None:
        """
        PURPOSE: display the shopping menu to the user\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        shopping_menu = {"0": "return to main menu",
                         "1": "add product to cart",
                         "2": "remove product from cart",
                         "3": "view cart",
                         "4": "checkout"}

        self.__get_menu_selection(menu_name="Shopping Menu", menu=shopping_menu)

    def __get_menu_selection(self, menu_name: str, menu: dict) -> str:
        """
        PURPOSE: get the user's menu selection\n
        ARGUMENT: menu_name: the name of the menu to display, menu: the menu to display\n
        RETURN: the user's selection\n
        """
        while True:
            print(f"\n\n{menu_name}")
            for key, value in menu.items(): print(f"Enter {key}: {value}")
            if (user_selection := input("Enter the number of the desired option: ").strip()) not in menu: print("ERROR: Invalid input provided.")
            elif user_selection  == "0": break
            else: self.__execute_menu_selection(selection=menu[user_selection])

    def __execute_menu_selection(self, selection: str) -> None:
        """
        PURPOSE: execute the selected menu option\n
        ARGUMENT: selection: the selected action\n
        RETURN: None\n
        """
        match selection:
            case "quit": self.__quit()
            case "view sorted products": self.__sorting_menu()
            case "view products by id": self.__sort_products_by_attribute(attribute="__product_id")
            case "view products by coffee type": self.__sort_products_by_attribute(attribute="__coffee_type")
            case "view products by roast type": self.__sort_products_by_attribute(attribute="__roast_type")
            case "view products by size": self.__sort_products_by_attribute(attribute="__size")
            case "view products by price": self.__sort_products_by_attribute(attribute="__price")
            case "view searched products": self.__searching_menu()
            case "search for products by coffee type": self.__display_products(products=self.__search_products_by_attribute(attribute="__coffee_type"))
            case "search for products by roast type": self.__display_products(products=self.__search_products_by_attribute(attribute="__roast_type"))
            case "manage shopping cart": self.__shopping_menu()
            case "add product to cart": self.__add_product_from_shopping_cart()
            case "remove product from cart": self.__remove_product_from_shopping_cart()
            case "view cart": self.__view_shopping_cart()
            case "checkout": self.__checkout()

    def __sort_products_by_attribute(self, attribute: str) -> None:
            """
            PURPOSE: sort the products by the provided attribute\n
            ARGUMENT: attribute: the attribute to sort by\n
            RETURN: None\n
            """
            self.products = sorted(self.products, key=lambda product: getattr(product, f"_Product{attribute}"))
            self.__display_products(products=self.products)

    def __search_products_by_attribute(self, attribute: str, attribute_value: str = None, shopping_cart: bool = False) -> list[Product]:
        """
        PURPOSE: search for products by the provided attribute\n
        ARGUMENT: attribute: the attribute to search by\n
        RETURN: a list of products that match the search criteria\n
        """
        if not attribute_value: attribute_value = input(f"Enter the {attribute.replace("_", " ").strip()} you would like to search for: ").strip().upper()
        if shopping_cart: return list(filter(lambda product: getattr(product, f"_Product{attribute}") == attribute_value, self.customer.get_shopping_cart()))
        else: return list(filter(lambda product: getattr(product, f"_Product{attribute}") == attribute_value, self.products))

    def __add_product_from_shopping_cart(self) -> None:
        """
        PURPOSE: add a product to the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        product_id = int(input("Enter the product ID of the product you would like to add to your cart: ").strip())
        if not (product := self.__search_products_by_attribute(attribute="__product_id", attribute_value=product_id)): print("Product not found!")
        else: 
            self.customer.add_to_shopping_cart(product=product[0])
            print("The following product has been added to your cart!")
            self.__display_products(products=self.customer.get_shopping_cart())

    def __remove_product_from_shopping_cart(self) -> None:
        """
        PURPOSE: remove a product from the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        product_id = int(input("Enter the product ID of the product you would like to remove from your cart: ").strip())
        if not (product := self.__search_products_by_attribute(attribute="__product_id", attribute_value=product_id, shopping_cart=True)): print("Product not found in shopping cart!")
        else: 
            self.customer.remove_from_shopping_cart(product=product[0])
            print("The following product has been removed from your cart!")
            self.__display_products(products=list(product))

    def __view_shopping_cart(self) -> None:
        """
        PURPOSE: display the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.__display_products(products=self.customer.get_shopping_cart())

    def __checkout(self) -> None:
        """
        PURPOSE: checkout the customer's shopping cart\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.database.check_out(customer_id=self.customer.get_customer_id(), products=[(product.get_product_id(),) for product in self.customer.get_shopping_cart()])
        self.customer.clear_shopping_cart()
        print("Thank you for shopping with us! Your order has been placed.")

    def __display_products(self, products: list) -> None:
            """
            PURPOSE: display the products to the user\n
            ARGUMENT: None\n
            RETURN: None\n
            """
            print("\nProduct ID \tType\t\tRoast\t\tSize (oz)\tPrice")
            for product in products: product.print_product()
            print()

    def __quit(self) -> None:
        """
        PURPOSE: Close the application\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        self.customer.goodbye()
        sys.exit()

if __name__ == "__main__": app()