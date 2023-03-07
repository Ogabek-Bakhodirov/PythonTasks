import csv
import random

usersInfoDB = {
    'users' : [], 
    'student_info' : [],
    'students_grade' : []
}

adminDB = {'ID':[], 'PSW': []}
studentDB = {'ID':[], 'PSW': []}
# users = {'ID':[], 'PSW': []}
studentGradeDB = {'ID':[], 'MATH':[], 'PROGRAMMING':[], 'DATABASE':[], 'ENGLISH':[]}
studentInfoDB = {'ID':[], 'NAME':[], 'SURNAME':[], 'AGE':[], 'PAYMENTSTATUS':[]}

def copyFromCSV(fileDirection, csvMode, passDataTo):
    # Check direction 
    with open(fileDirection, csvMode) as file:
        csvreader = csv.reader(file)
        for info in csvreader:
            # Check Dictionary direction
            usersInfoDB[passDataTo].append(info)

copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Students_grade.csv", "r", "students_grade")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Student_info.csv", "r", "student_info")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Users.csv", "r", "users")

# Get data from usersInfoDB to Student/Admin
index = 0
while True:
    if len(usersInfoDB['users']) != index:
        user = usersInfoDB['users'][index]
        # Check if Student append to student DB
        if user[0][0] == 's':
            studentDB['ID'].append(user[0])
            studentDB['PSW'].append(user[1])
        # Check if Admin append to admin DB
        elif user[0][0] == 'a':
            adminDB['ID'].append(user[0])
            adminDB['PSW'].append(user[1])
        index += 1
    else:
        index = 0
        break

# Get data from usersInfoDB to StudentGrade db
while True:
    if len(usersInfoDB['students_grade']) != index:
        user = usersInfoDB['students_grade'][index]
        # Check if Student append to student DB
        if user[0][0] == 's':
            studentGradeDB["ID"].append(user[0])
            studentGradeDB["MATH"].append(user[1])
            studentGradeDB["PROGRAMMING"].append(user[2])
            studentGradeDB["DATABASE"].append(user[3])
            studentGradeDB["ENGLISH"].append(user[4])
        index += 1
    else:
        index = 0
        break

# for i in usersInfoDB["students_grade"]:
#     studentGradeDB["ID"].append(i[0])
#     studentGradeDB["MATH"].append(i[1])
#     studentGradeDB["PROGRAMMING"].append(i[2])
#     studentGradeDB["DATABASE"].append(i[3])
#     studentGradeDB["ENGLISH"].append(i[4])


# Get data from usersInfoDB to StudentInfo db
while True:
    if len(usersInfoDB['student_info']) != index:
        user = usersInfoDB['student_info'][index]
        # Check if Student append to student DB
        if user[0][0] == 's':
            studentInfoDB["ID"].append(user[0])
            studentInfoDB["NAME"].append(user[1])
            studentInfoDB["SURNAME"].append(user[2])
            studentInfoDB["AGE"].append(user[3])
            studentInfoDB["PAYMENTSTATUS"].append(user[4])
        index += 1
    else:
        index = 0
        break

# for i in usersInfoDB["student_info"]:
#     studentInfoDB["ID"].append(i[0])
#     studentInfoDB["NAME"].append(i[1])
#     studentInfoDB["SURNAME"].append(i[2])
#     studentInfoDB["AGE"].append(i[3])
#     studentInfoDB["PAYMENTSTATUS"].append(i[4])

# Random ID generator
def randomIDGenerator():
    studentAmount = len(studentDB['ID'])
    studentID = random.sample(range(0, studentAmount), 1)
    print(studentID)
    if studentID[0] < 10:
        return f'st00{studentID[0]}'
    elif studentID < 100:
        return f'st0{studentID[0]}'
    else:
        return f'st{studentID[0]}'

# Check id if unique add to dataBase
def idGenerator():
    studentID = randomIDGenerator()
    if studentID not in  studentDB['ID']:
        print(studentID)
        return studentID
    else:
        idGenerator()
    

# Function for checking student records.
def seeStudentRecords(studentID, isNeedGrades):
    index = 0
    for info in studentDB['ID']:
        if info == studentID:
            print('Student ID: ' +  studentDB['ID'][index])
            print('Student Password: ' + studentDB['PSW'][index])    
            print('Student name: ' + studentInfoDB["NAME"][index])
            print('Student surname: ' + studentInfoDB["SURNAME"][index])
            print('Student age: ' + studentInfoDB["AGE"][index])
            print('Student payment status: ' + studentInfoDB["PAYMENTSTATUS"][index])  
            if isNeedGrades == True:
                print('Math grade: ' + studentGradeDB["MATH"][index])
                print('Programming grade: ' + studentGradeDB["PROGRAMMING"][index])
                print('Database grade: ' + studentGradeDB["DATABASE"][index])
                print('English grade: ' + studentGradeDB["ENGLISH"][index])
            index = 0
            return True
        index += 1 
    print('Student id not found: 404')

# Registration of new student.
def studentRegistration():
    name = input('\nEnter your name: ')
    surname = input('Enter your surname: ')
    age = input('Enter your age: ')
    studentID = 'st000' #idGenerator() fix it
    password = input('Enter your password: ')

    studentDB['ID'].append(studentID)
    studentDB['PSW'].append(password)
    studentInfoDB['ID'].append(studentID)
    studentInfoDB['NAME'].append(name)
    studentInfoDB['SURNAME'].append(surname)
    studentInfoDB['AGE'].append(age)
    studentInfoDB['PAYMENTSTATUS'].append('null')
    studentGradeDB['ID'].append(studentID)
    studentGradeDB['DATABASE'].append('null')
    studentGradeDB['ENGLISH'].append('null')
    studentGradeDB['MATH'].append('null')
    studentGradeDB['PROGRAMMING'].append('null')

    print('\n Your name: '+name+'\n','Your surname: '+surname+'\n','Your age: '+age+'\n',
          'Your student ID: '+studentID+'\n','Your password: '+password+'\n')

    isContinue = int(input('\nWhat do you want to do next: \nSee records -> 0 \nStop -> 1: \nEnter only number: '))
    if isContinue == 0:
        studentID = input("\nEnter your student ID: ")
        seeStudentRecords(studentID, True)
    elif isContinue == 1:
        return True
    else:
        print('\nNot valid number entered !')


def checkUserStatus(userInfo):
    # UserInfo - Student
    if userInfo == 1:
        # Choosen action (Register or See records)
        action = int(input('\nWhat you want to do: \nRegister - 0, \nSee my records - 1: \nEnter only number: '))
        # If action -> See records
        if action == 1:
            studentID = input("Enter your student ID: ")
            seeStudentRecords(studentID)

        elif action == 0:
            studentRegistration()

userInfo = int(input('Who are you:\nStudent - 1 \nAdmin - 0 \nEnter only number: '))
checkUserStatus(userInfo)
