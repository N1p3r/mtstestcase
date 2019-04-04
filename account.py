class Account:
   def __init__(self, number, balance, status):
       self.number = number
       self.balance = balance
       self.status = status

   def __repr__(self):
       return self.number + " - " + str(int(self.number[:3])) + " " + str(self.balance) + ", " + str("Открыт" if self.status == 1 else "Закрыт")


def get_account_list(accounts):
    return filter(lambda a: a.status == 1 and a.balance > 0 or a.status != 1 and 441 <= int(a.number[0:3]) <= 457, accounts)


filtered_accounts = get_account_list([
   Account("40502840000000000000", 5000000, 1),
   Account("46002840000000000000", 15000000, 1),
   Account("45002840000000000000", 7000000, 2),
   Account("40502840000000000000", 2300000, 1),
   Account("44202840000000000000", 1200000, 0),
   Account("40502840000000000000", 0, 1),
   Account("40502840000000000000", 7500000, 0),
   Account("40502840000000000000", 6000000, 0)
])