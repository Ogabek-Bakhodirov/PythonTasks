# dict = {
#     'fruit' : ['apple', 'banana', 'pineapple', 'strawberry', 'peach'], 
#     'fruitPrice' : [3, 4, 3, 5, 6],
#     'drink' : ['cola', 'fanta', 'sprite', 'pepsi', 'dinay'],
#     'drinkPrice' : [6, 5, 7, 4, 3],
#     'veg' : ['spinach', 'carrot', 'beets', 'potato', 'tomato'],
#     'vegPrice' : [4, 5, 6, 3, 3]
# }
# value = ''

# def createMenu(categoryKey, indexValue, amount):
#     if len(dict[categoryKey]) <= indexValue:
#         print('Choosen index out of range')
#     else:
#         product = dict[categoryKey][indexValue]
#         price = dict[f'{categoryKey}Price'][indexValue] * amount
#         if categoryKey == 'drink':
#             value = f'Amount of {product}: {amount} and price is ${price}'
#         else:
#             value = f'{amount} kg {product} is ${price}'
#         print(value)
        
# createMenu('fruit', 3, 3)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# page 1 sign in , register, quit
# page 2 sign in username password check from dict if true go page 3 else message
# page 3 registration check there has or not in dict

userDatabase = {"username" : "password"}

print('1. Sign in\n2. Register\n3. Quit\n')
choosenPage = int(input('In which page you want to enter (only number): '))

def userEntry(choosenPage):
    # Check Page Status
    if choosenPage < 3:
        if choosenPage == 1:
            # Sign in
            username = input('Enter your account\' username: ')
            password = input('Enter your password: ')
            # Call sign in function
            
            checkSignIn(username, password)
            
        elif choosenPage == 2: 
            # Register
            username = input('Enter new account\' username: ')
            password = input('Enter password: ')
            
            # Call Registration
            
            registration(username, password)
            
        elif choosenPage == 3: 
            # Quit
            print(choosenPage)
    else: 
        print('Choosen page number out of list')
        
def checkSignIn(username, password):
    # isRegistered = False
    for user in userDatabase:
        print(user)
        if username == user :
            # isRegister = True
            print("Registered")
            return True
    print("Not registered")
    return False

def registration(username, password):
    userDatabase = {username : password}
    choosenPage = int(input('In which page you want to enter (only number): '))
    userEntry(choosenPage)

userEntry(choosenPage)


