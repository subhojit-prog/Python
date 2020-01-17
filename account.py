class Account:
    account_no = ''
    customer_name = ''
    balance = 0

    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def __repr__(self):
        return f"Account NO. -{self.account_no} Acccount holder- {self.customer_name} Availabel Balance- {self.balance}"
