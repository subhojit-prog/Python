from bank import Bank
from account import Account


def main():

    bank = Bank()

    account = Account()

    account_1 = Account("12345", "chintu", 200)
    account_2 = Account("56789", "pintu", 500)

    bank.addAccount(account_1).addAccount(account_2)

    # print(bank.accountCreate('aa', '12'))

    while True:
        valid = input(
            "press 1 for create new account \npress 2 for existing account\npress any key to exit.\n")
        if valid == '1':
            account_name = input("enter your name: \n")
            int_depo = input("enter your initial deposit amount: \n")
            print(
                f"\nyour account no is {bank.accountCreate(account_name, int(int_depo))}\n")
        elif valid == '2':
            account_no = input("enter your account no: \n")
            if bank.getAccount(account_no):
                while True:
                    usrinput = input(
                        '\npress 1 to view existing account balance \npress 2 for deposit or withdrawl money \npress any key to go back.\n')
                    if usrinput == '1':
                        print(f'{bank.accountDetails(account_no)}')
                    elif usrinput == '2':
                        while True:
                            usrinpt = input(
                                '\npress 1 for deposit balance: \npress 2 to withdrawl from account balance \npress any key to go back.\n')
                            if usrinpt == '1':
                                bal_u = int(input("enter amount: \n"))
                                print(
                                    f"\nyour new balance {bank.depositor(account_no, bal_u)}/- Rs \n")
                            elif usrinpt == '2':
                                bal_u = int(input("enter amount: \n"))
                                print(bank.withdrawler(account_no, bal_u))
                            else:
                                break
                    else:
                        break
            else:
                print("account no not valid")
                break
        else:
            exit()


if __name__ == "__main__":
    main()
