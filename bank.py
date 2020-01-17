from account import Account


class Bank():
    """Bank class that encapsulates all bank functions."""

    accounts = []
    lastAccountNumber = 0
    branchCode = ""

    def __init__(self, code):
        super().__init__()
        self.branchCode = code

    def getAccount(self, account_no):
        """Return account based on account number."""
        for account in self.accounts:
            if account_no == account.account_no:
                return account

    def generateAccountNumber(self):
        """Generate an account number."""
        self.lastAccountNumber += 1
        return self.branchCode + '-' + str(self.lastAccountNumber).zfill(5)

    def createAccount(self, name, amount):
        """Create an account."""
        account_no = self.generateAccountNumber()
        self.accounts.append(Account(account_no, name, amount))
        return account_no

    def deposit(self, account_no, amount):
        """Deposit monies into account."""
        account = self.getAccount(account_no)
        account.balance += amount
        return account.balance

    def withdraw(self, account_no, amount):
        """Withdraw monies from account."""
        account = self.getAccount(account_no)
        if account.balance >= amount:
            account.balance -= amount
            return F"\nyour new balance {account.balance}/- Rs \n"
        else:
            return "insufficient balance"
