# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# page 1 sign in , register, quit
# page 2 sign in username password check from dict if true go page 3 else message
# page 3 registration check there has or not in dict

lowLetters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}
upperLetters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols = {'!', '#', '$', '%', '&', '(', ')', '*', '+'}

userDatabase = {}

print('1. Sign in\n2. Register\n3. Quit\n')
choosenPage = int(input('In which page you want to enter (only number): '))

def userEntry(choosenPage):
    # Check Page Status
    if choosenPage < 4:
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
            username = input('Enter account\' username which you want to quit: ')
            password = input('Enter password: ')
            quitUser(username)
    else: 
        print('Choosen page number out of list')
        
def checkSignIn(username, password):
    # isRegistered = False
    for user in userDatabase:
        if username == user :
            # isRegister = True
            print("Registered")
            isNeedToCheckPassword = int(input('Do you want to check password status (if yes 1 or 0): '))
            if isNeedToCheckPassword == 1:
                checkPasswordStatus(password)
            return True
    print("Not registered")
    isContinue = int(input('Do you want to register (if yes 1 or 0): '))
    if isContinue == 1:
         userEntry(2)
    return False

def registration(username, password):
    userDatabase[username] = password
    print("Successfully registered!")
    choosenPage = int(input('In which page you want to enter (only number): '))
    userEntry(choosenPage)

def quitUser(userName):
    userDatabase.pop(userName)
    print(f'User removed from database\n{userDatabase}')
    
def checkPasswordStatus(password):    
    passwordCount = len(password)
    numberCount = 0
    letterCount = 0
    lowLetter = 0
    upperLetter = 0
    
    for char in password:
        if isExistInList(char, numbers):
            numberCount += 1
        if isExistInList(char, lowLetters) or isExistInList(char, upperLetters):
            letterCount += 1
            if isExistInList(char, upperLetters):
                upperLetter += 1
            else: 
                lowLetter += 1
    
    if passwordCount <= 7:
        print("Very Low :(")
    else: 
        if numberCount >= 4 and letterCount >= 3:
            if lowLetter >= 3 and upperLetter >= 2:
                print("Ultra pro max")
            else:
                print('Medium')
        
    
    print(f'Your password {password}')

def isExistInList(character, list):
    if character in list:
        return True
    else:
        return False

userEntry(choosenPage)

