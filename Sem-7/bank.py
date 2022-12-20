from random import randint
from errors import UserNotFound, UserAlreadyExists, AccountNotFound, UnsufficientBalance
from account import Account
from user import User

class Bank:
    def __init__(self) -> None:
        self.users = []

    def find_user(self, user_egn: str) -> User:
        for u in self.users:
            if u.egn == user_egn:
                return u

    def add_user(self, names, egn):
        try:
            found_user = self.find_user(egn)

            if type(found_user) == User:
                raise UserAlreadyExists()

            user = User(names, egn)
            self.users.append(user)
        except UserAlreadyExists as e:
            print(e)

    def add_account(self, user_egn, currency, type):
        # user exists?
        try:
            found_user = self.find_user(user_egn)

            if found_user == None:
                raise UserNotFound("User not found")

            # generate iban
            iban = "BG9812"
            for i in range(0, 10):
                iban += str(randint(0, 9))

            # create account object
            account = Account(iban, currency, type)

            # call the user's add_account() method
            found_user.add_account(account)
        except UserNotFound as e:
            print(e)
    def find_account(self, user_egn: str, iban: str) -> Account:
        try:
            found_user = self.find_user(user_egn)

            if found_user == None:
                raise UserNotFound("User not found")
            
            for j in found_user.accounts:
                if j.iban == iban:
                    return j
            raise AccountNotFound("Account not found")
        except UserNotFound as e:
            print(e)
        except AccountNotFound as e:
            print(e)

    def deposit(self, amount, account):
        intAmount = int(amount)
        account.balance += intAmount

    def withdrawal(self, amount, account):
        try:
            intAmount = int(amount)
            if intAmount > account.balance:
                raise UnsufficientBalance
            account.balance -= intAmount
        except UnsufficientBalance as e:
            print(e)
