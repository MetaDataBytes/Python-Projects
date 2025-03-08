from customer import Customer

class Member(Customer):
    def __init__(self, customer_record: list) -> None:
        super().__init__(customer_record=customer_record)
    
    def goodbye(self) -> None:
        """
        PURPOSE: display a goodbye message to the member\n
        ARGUMENT: None\n
        RETURN: None\n
        """
        print(f"Thank you for being a valued member at Justin's Coffee House! Have a wonderful day, {self.get_first_name().title()} {self.get_last_name().title()}!")