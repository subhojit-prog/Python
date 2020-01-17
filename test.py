from account import Account
class Bank():
    accounts = []

    def getAccount(self, account_no):
        for account in self.accounts:
            if account_no == account.account_no:
                return account

    def accountExists(self, account_no):
        account_noS = str(account_no)
        if self.getAccount(account_noS):
            return True
        else:
            return False

    def generateAccountNumber(self):
        x = 10000
        for account_no in range(x, 99999):
            if self.accountExists(account_no):
                x += 1
            else:
                return str(account_no)

    def createAccount(self, name, amount, account_no = ""):
        account_no = self.generateAccountNumber()
        self.accounts.append(Account(account_no, name, amount))
        return self.accounts


graminBank = Bank()

print(graminBank.createAccount("aa", 20))


#   while True:########
#         valid = input(
#             "press 1 for create new account \npress 2 for existing account\npress any key to exit.\n")
#         if valid == '1':
#             account_name = input("enter your name: \n")
#             int_depo = input("enter your initial deposit amount: \n")
#             print(
#                 f"\nyour account no is {bank.createAccount(account_name, int(int_depo))}\n")
#         elif valid == '2':########
#             account_no = input("enter your account no: \n")
#             if bank.getAccount(account_no):
#                 while True:########
#                     usrinput = input(
#                         '\npress 1 to view existing account balance \npress 2 for deposit or withdrawl money \npress any key to go back.\n')
#                     if usrinput == '1':
#                         print(f'{bank.accountDetails(account_no)}')
#                     elif usrinput == '2':
#                         while True:########
#                             usrinpt = input(
#                                 '\npress 1 for deposit balance: \npress 2 to withdrawl from account balance \npress any key to go back.\n')
#                             if usrinpt == '1':
#                                 bal_u = int(input("enter amount: \n"))
#                                 print(
#                                     f"\nyour new balance {bank.deposit(account_no, bal_u)}/- Rs \n")
#                             elif usrinpt == '2':
#                                 bal_u = int(input("enter amount: \n"))
#                                 print(bank.withdraw(account_no, bal_u))
#                             else:
#                                 break
#                     else:
#                         break
#             else:
#                 print("account no not valid")
#                 break
#         else:
#             exit()