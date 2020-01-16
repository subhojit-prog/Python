class Account:
    
    def __init__(self, account_no = '', customer_name = '', balance = ''):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def __repr__(self):
        return f"{self.account_no} - {self.customer_name} - {self.balance}"

