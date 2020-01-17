from bank import Bank
from account import Account


def main():
    """Console function for the Bank."""

    def createNewAccount(bank):
        account_name = input("enter your name: \n")
        int_depo = input("enter your initial deposit amount: \n")
        print(
            f"\nyour account no is {bank.createAccount(account_name, int(int_depo))}\n")

    def viewExistingAccount(bank):
        account_no = input("enter your account no: \n")
        if bank.getAccount(account_no):
            accountOperations(bank, account_no)
        else:
            print("account no not valid")

    def accountOperations(bank, account_no):
        while True:
            usrinput = input(
                '\npress 1 to view existing account balance \npress 2 for deposit or withdrawl money \npress any key to go back.\n')
            if usrinput == '1':
                print(bank.getAccount(account_no))
            elif usrinput == '2':
                while True:
                    usrinpt = input(
                        '\npress 1 for deposit balance: \npress 2 to withdrawl from account balance \npress any key to go back.\n')
                    if usrinpt == '1':
                        deposit(bank, account_no)
                    elif usrinpt == '2':
                        withdraw(bank, account_no)
                    else:
                        break
            else:
                break

    def deposit(bank, account_no):
        bal_u = int(input("enter amount: \n"))
        print(f"\nyour new balance {bank.deposit(account_no, bal_u)}/- Rs \n")

    def withdraw(bank, account_no):
        bal_u = int(input("enter amount: \n"))
        print(bank.withdraw(account_no, bal_u))

    bank = Bank('IXB')

    while True:
        menu = """
        Press 1 to create a new account.
        Press 2 for existing accounts.
        """
        valid = input(menu)
        if valid == '1':
            createNewAccount(bank)
            continue
        elif valid == '2':
            viewExistingAccount(bank)
            continue
        else:
            exit()
        break

    
if __name__ == "__main__":
    main()