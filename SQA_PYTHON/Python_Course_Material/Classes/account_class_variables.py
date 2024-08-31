

import random

class Account(object):

    minimum_balance = 50

    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current balance is: {self.current_balance}")

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New balance after withdraw: {self.current_balance}")

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New balance after deposit: {self.current_balance}")

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        print(f"Getting balance from db for: {self.user_id}")
        return random.randint(100, 1000)

    def create_new_investment_account(self, balance):
        if balance >= Account.minimum_balance:
            print("Creating new 'Investment' account.")
        else:
            print(f"FAIL. Minimum balance to create investment account is {Account.minimum_balance}")


account1 = Account(9871)
account2 = Account(1234)
print("----")
print("Acct 1 min: ", account1.minimum_balance)
print("Acct 2 min: ", account2.minimum_balance)
Account.minimum_balance = 75
print("----")
print("Acct 1 min: ", account1.minimum_balance)
print("Acct 2 min: ", account2.minimum_balance)

account3 = Account(1111)
print(account3.minimum_balance)
# uncomment below to see it fail because the method is private
# account1.__read_amount_from_database()


#####
"""
print the min accounf fo both objects

make the change on the class
Account.minimum_balance, then print both again (both are updated

now only update acc1, print again and u will see only 1 is updated
## it checks if the instance has the variable if not will update the class

# if we create a third object it will still be 50 because we didn't update the class 

# but if we update the class variable then the new object will have the new value

"""