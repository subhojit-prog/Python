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
        x = 10000
        for account_no in range(x, 99999):
            if self.isAccountPresent(account_no):
                x = x+1
        else:
            return str(account_no)

    def addAccount(self, accountsForAdd):
        self.accounts.append(accountsForAdd)
        return self

    def accountDetails(self, account_no):
        account = self.getAccount(account_no)
        return f"{account.customer_name} has balance {account.balance}/- rs"

    def depositor(self, account_no, bal_u):
        account = self.getAccount(account_no)

        pass

    def withdrawler(self, account_no, bal_u):
        pass
