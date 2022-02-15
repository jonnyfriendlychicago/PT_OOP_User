class User:
    # class attributes get defined in the class     
    # bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
    # have this method decrease the user's balance by the amount specified
        self.account_balance -= amount

    def display_user_balance(self): 
        self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
    #have this method print the user's name and account balance to the terminal, e.g. "User: Guido van Rossum, Balance: $150

    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        other_user.balance_display = print(f"User: {other_user.name}, Balance: ${other_user.account_balance}")
    #have this method decrease the user's balance by the amount and add that amount to other other_user's balance

a1 = User("Lucky Day", "lucky@3amigos.com")
a2 = User("Dusty Bottoms", "dusty@3amigos.com")
a3 = User("Ned Nederlander", "ned@3amigos.com")

print(a1.name)
print(a2.name)
print(a3.name)

a1.make_deposit(33)
a1.make_deposit(33)
a1.make_deposit(33)
a1.make_withdrawal(20)
a1.display_user_balance()

a2.make_deposit(50)
a2.make_deposit(50)
a2.make_withdrawal(25)
a2.make_withdrawal(25)
a2.display_user_balance()

a3.make_deposit(79)
a3.make_withdrawal(40)
a3.make_withdrawal(20)
a3.make_withdrawal(20)
a3.display_user_balance() 


a1.transfer_money(a3, 19)


# michael = User()
# anna = User()


""" initial values from exercises
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

guido.make_withdrawal(100)
guido.display_user_balance()

print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

"""