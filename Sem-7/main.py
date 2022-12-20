from bank import Bank
from errors import InvalidUserData, InvalidMenuChoice, UserNotFound, InvalidDepositOrWithdrawAmount
from user import User

class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("2. Create an account for an existing user")
        print("3. List all users")
        print("4. List all accounts for an existing user")
        print("5. Deposit money to a user account")
        print("6. Withdraw money from a user account")
        print("7. Exit")

    def run(self):
        bank = Bank()

        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    names = input("Enter the user's names (alpha-only): ")
                    fname, lname = names.split(" ")
                    if len(names) < 4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidUserData("Invalid names")

                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")

                    bank.add_user(names, egn)
                elif choice == "2":
                    # second command
                    print("second command\n")
                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")
                    currency = input("currency: ")
                    type = input("type: ")

                    bank.add_account(user_egn=egn, currency=currency, type=type)
                elif choice == "3":
                    for u in bank.users:
                        print(u.get_print())
                elif choice == "4":
                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")
                    found_user = bank.find_user(egn)

                    if found_user == None:
                        raise UserNotFound("User not found")
                    found_user.get_print()
                elif choice == "5":
                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")
                    iban = input("iban: ") 
                    found_account = bank.find_account(user_egn=egn, iban=iban)
                    amount = input("amount: ")
                    if not amount.isdigit():
                        raise InvalidDepositOrWithdrawAmount("Invalid deposit amount, must be only digits")
                    if amount < 0:
                        raise InvalidDepositOrWithdrawAmount("Invalid deposit amount, cant be negative number")
                    bank.deposit(amount=amount, account=found_account)
                elif choice == "6":
                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")
                    iban = input("iban: ") 
                    found_account = bank.find_account(user_egn=egn, iban=iban)
                    amount = input("amount: ")
                    if not amount.isdigit():
                        raise InvalidDepositOrWithdrawAmount("Invalid withdraw amount, must be only digits")
                    if amount < 0:
                        raise InvalidDepositOrWithdrawAmount("Invalid withdraw amount, cant be negative number")
                    bank.withdrawal(amount=amount, account=found_account)
                elif choice == "7":
                    print("Goodbye\n")
                    break
                else:
                    raise InvalidMenuChoice("Error: Invalid choice")
            except InvalidDepositOrWithdrawAmount as e:
                print(e)
            except InvalidUserData as e:
                print(e)
            except UserNotFound as e:
                print(e)
            except Exception as ex:
                print(f"Error: There was an error while executing the command:\n{str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
