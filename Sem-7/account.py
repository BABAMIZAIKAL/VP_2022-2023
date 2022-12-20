from errors import InvalidAccountType, InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")
    ACC_DATA = ("BGN", "GBP", "USD", "EUR")

    def __init__(self, iban, currency, type) -> None:
        try: 
            if type not in Account.ACC_TYPES:
                raise InvalidAccountType("Invalid account Type")
            if currency not in Account.ACC_DATA:
                raise InvalidAccountData("Invalid account currency")
            self.iban = iban
            self.currency = currency
            self.type = type
            self.balance = 0
        except InvalidAccountType as e :
            print(e)
        except InvalidAccountData as e :
            print(e)

    # def get_print(self, useraccounts):
    #     index = useraccounts.index(self)
    #     return f"Account [{index}] -> (IBAN: {self.iban}, currency: {self.currency}, type: {self.type}) [Balance: {self.balance}]"

