import csv

user = []
userInfo = []

lowLetters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'}
upperLetters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols = {'!', '#', '$', '%', '&', '(', ')', '*', '+'}

while True:

    # Set up data
    def setupData():
        with open("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/User-1.csv", "r") as file:
            csvreader = csv.reader(file)
            for index, values in enumerate(csvreader):
                if index == 0:
                    continue
                else:
                    user.append({'ID':values[0], 'Username':values[1], 'PSW':values[2], 'Question':values[3], 'Answer':values[4]})

        with open("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/User_info-1.csv", "r") as file:
            csvreader = csv.reader(file)
            for index, values in enumerate(csvreader):
                if index == 0:
                    continue
                else:
                    userInfo.append({'ID':values[0], 'Name':values[1], 'Surname':values[2], 'age':values[3], 'passport':values[4], 'adsress':values[5]})

# Id generator
    def idGenerator():
        return 1

# When registered check username if has in database or not
    def checkUsername(username):
        for value in user:
            if username == value['Username']:
                print("This username is exist try again!")
                return False
        print(f'Success! Your username is {username}')
        return True

# Check password
    def checkPasswordStatus(password, confirmedPassword):  
        if password == confirmedPassword:
            passwordCount = len(password)
            numberCount = 0
            letterCount = 0
            lowLetter = 0
            upperLetter = 0
            
            for char in password:
                if char in numbers:
                    numberCount += 1
                if (char in lowLetters) or char in upperLetters:
                    letterCount += 1
                    if char in upperLetters:
                        upperLetter += 1
                    else: 
                        lowLetter += 1
            
            if passwordCount <= 7:
                print("Very Low :(")
                return False
            else: 
                if numberCount >= 4 and letterCount >= 3:
                    if lowLetter >= 3 and upperLetter >= 2:
                        print("Ultra pro max")
                    else:
                        print('Medium')
                return True
        else:
            print("Your password and confirmed password is different")
            return False

# Login
    def login():
        print(user)
    
# Register
    def register():
        while True:
            username = input('\nEnter username: ')
            if checkUsername(username):
                break
        while True:
            password = input('Enter password. It should be more than 7 characters: numbers more than 4, letter more than 3: ')
            confirmedPassword = input('Confirm password: ')
            if checkPasswordStatus(password, confirmedPassword):
                break
        specialQuestion = input("Enter question that is special for entery: ")
        answer = input("Asnwer for the question: ")
        id = idGenerator()
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        age = input("Enter your age: ")
        passport = input("Enter your passport numbers: ")
        address = input("Enter your address: ")
        user.append({'ID':id, 'Username':username, 'PSW':password, 'Question':specialQuestion, 'Answer':answer})
        userInfo.append({'ID':id, 'Name':name, 'Surname':surname, 'age':age, 'passport':passport, 'adsress':address})
 
#  Entery
    firstMove = int(input('What you want to do: \nLogin - 0 \nRegister - 1 \nStop - 2\nOnly number! -> '))
    setupData() # get data from csv files and collect them
    if firstMove == 0:
        login()
    elif firstMove == 1:
        register()
    else:
        break