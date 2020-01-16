from account import Account


class Bank():
    accounts = []

    def getAccount(self, account_no):
        for account in self.accounts:
            if account_no == account.account_no:
                return account

    def isAccountPresent(self, account_no):
        account_noS = str(account_no)
        if self.getAccount(account_noS):
            return True
        else:
            return False

    def accountNoGen(self):
        x = 12345
        for account_no in range(x, 99999):
            if self.isAccountPresent(account_no):
                x += 1
            else:
                return str(account_no)

    def accountCreate(self, name, amount):
        account_no = self.accountNoGen()
        self.accounts.append(Account(account_no, name, amount))
        return account_no

    def addAccount(self, accountForAdd):
        self.accounts.append(accountForAdd)
        return self

    def accountDetails(self, account_no):
        account = self.getAccount(account_no)
        return f"{account.customer_name} has balance {account.balance}/- dinar"

    def depositor(self, account_no, amount):
        account = self.getAccount(account_no)
        account.balance += amount
        return account.balance

    def withdrawler(self, account_no, amount):
        account = self.getAccount(account_no)
        if account.balance >= amount:
            account.balance -= amount
            return F"\nyour new balance {account.balance}/- Rs \n"
        else:
            return "insufficient balance"
