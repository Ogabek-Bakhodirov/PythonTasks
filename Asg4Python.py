import csv
import random

usersInfoDB = {
    'users' : [], 
    'student_info' : [],
    'students_grade' : []
}

adminDB = {'ID':[], 'PSW': []}
studentDB = {'ID':[], 'PSW': []}
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
        if user[0][0] == 's': # Fix: what if user[0][0] == ''
            studentGradeDB["ID"].append(user[0])
            studentGradeDB["MATH"].append(user[1])
            studentGradeDB["PROGRAMMING"].append(user[2])
            studentGradeDB["DATABASE"].append(user[3])
            studentGradeDB["ENGLISH"].append(user[4])
        index += 1
    else:
        index = 0
        break

# Get data from usersInfoDB to StudentInfo db
while True:
    if len(usersInfoDB['student_info']) != index:
        user = usersInfoDB['student_info'][index]
        if user[0][0] == 's': # Fix: what if user[0][0] == ''
            studentInfoDB["ID"].append(user[0])
            studentInfoDB["NAME"].append(user[1])
            studentInfoDB["SURNAME"].append(user[2])
            studentInfoDB["AGE"].append(user[3])
            studentInfoDB["PAYMENTSTATUS"].append(user[4])
        index += 1
    else:
        index = 0
        break

# Random ID generator
studentIDList = []

def studentIdListGenerator():
    index = 0
    global studentIDList 
    studentIDList = []
    for i in studentDB['ID']:
        studentIDList.append(index)
        index += 1
    studentIDList.append(index)

studentIdListGenerator()

def removeRandomElementAndReturn(list):
    index = random.sample(range(len(studentIDList)+1), 1)
    if index[0] >= len(studentIDList):
        return removeRandomElementAndReturn(list)
    else:
        value = list[index[0]]
        del list[index[0]]
        return value

# Random ID generator
def randomIDGenerator():
    studentID = removeRandomElementAndReturn(studentIDList)
    if studentID < 10:
        return f'st00{studentID}'
    elif studentID < 100:
        return f'st0{studentID}'
    else:
        return f'st{studentID}'

# Check id if unique add to dataBase
def idGenerator():
    studentID = randomIDGenerator()

    if studentID in studentDB['ID']:
        return idGenerator()
    else:
        return studentID

# Function for checking student records.
def seeStudentRecords(studentID, isNeedGrades):
    index = 0
    for info in studentDB['ID']:
        if info == studentID:
            print('\nStudent ID: ' +  studentDB['ID'][index])
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
    studentID = idGenerator()
    password = input('Enter your password: ')

    studentDB['ID'].append(studentID)
    studentDB['PSW'].append(password)
    studentInfoDB['ID'].append(studentID)
    studentInfoDB['NAME'].append(name)
    studentInfoDB['SURNAME'].append(surname)
    studentInfoDB['AGE'].append(age)
    studentInfoDB['PAYMENTSTATUS'].append('None')
    studentGradeDB['ID'].append(studentID)
    studentGradeDB['DATABASE'].append('0')
    studentGradeDB['ENGLISH'].append('0')
    studentGradeDB['MATH'].append('0')
    studentGradeDB['PROGRAMMING'].append('0')

    studentIdListGenerator()

    print(f'\nYour name: {name}\nYour surname: {surname}\nYour age: {age}\nYour student ID: {studentID}\nYour password: {password}\n')

    isContinue = int(input('\nWhat do you want to do next: \nSee records -> 0 \nStop -> 1: \nEnter only number: '))
    if isContinue == 0:
        studentID = input("\nEnter your student ID: ")
        seeStudentRecords(studentID, True)
    elif isContinue == 1:
        return True
    else:
        print('\nNot valid number entered !')
    
# Delete student's records
def deleteStudent(studentID):
    if studentID in studentInfoDB['ID']:
        # delete student's record
        print("")
    else:
        print("Incorrect student ID entered! ")

# Change student's grades
def changeGrades(studentID, subject):
    if studentID in studentGradeDB['ID']:
        # Change student's grade
        print("")
    else:
        print("Incorrect student ID entered! ")

# Change student's info
def changeStudentInfo(studentID):
    if studentID in studentInfoDB['ID']:
        # Change student's info
        print("")
    else:
        print("Incorrect student ID entered! ")

# Find failed students
def findFailedStudent():
    failedStudentsIDList = []
    for index in range(len(studentGradeDB['ID'])):
        gradeResult = int(studentGradeDB['ENGLISH'][index]) + int(studentGradeDB['DATABASE'][index]) + int(studentGradeDB['MATH'][index]) + int(studentGradeDB['PROGRAMMING'][index])
        if (int(gradeResult) / 4) < 60:
            failedStudentsIDList.append(studentGradeDB['ID'][index])
    
    print(failedStudentsIDList)

# Find high graded students
def findHighGradedStudents():
    highGradedStudentsIDList = []
    for index in range(len(studentGradeDB)):
        gradeResult = int(studentGradeDB['ENGLISH'][index]) + int(studentGradeDB['DATABASE'][index]) + int(studentGradeDB['MATH'][index]) + int(studentGradeDB['PROGRAMMING'][index])
        if (int(gradeResult) / 4) > 86:
            highGradedStudentsIDList.append(studentGradeDB['ID'][index])
    
    print(highGradedStudentsIDList)
 
def checkUserStatus(userInfo):
    # UserInfo - Student
    if userInfo == 1:
        # Choosen action (Register or See records)
        action = int(input('\nWhat you want to do: \nRegister - 0, \nSee my records - 1: \nEnter only number: '))
        # If action -> See records
        if action == 1:
            studentID = input("Enter your student ID: ")
            seeStudentRecords(studentID, True)

        elif action == 0:
            studentRegistration()
        else:
            print("Wrong data")

    elif userInfo == 0:
        while True:
            # Add see students
            nextMove = int(input("\nWhat you want to do: \nDelete student's record - 1. \nChange grades - 2. \nChange student info - 3. \nFind Failed students - 4. \nFind high graded students - 5. \nStop - 6. \nEnter only number -> "))
            if nextMove == 1:
                deletedStudentID = input("Enter student id which you want to delete: ")
            elif nextMove == 2: 
                studentIDForChangeGrade = input("Enter student id which you want to change grade: ")
                subject = int(input("\nWhich subject's grade you want to change: \nMath - 1: \nProgramming - 2: \nDatabase - 3: \nEnglish - 4: \nEnter only number -> "))
            elif nextMove == 3:
                deletedStudentID = input("Enter student id which you want to change info: ")
            elif nextMove == 4:
                print("\nFailed students")
                findFailedStudent()
            elif nextMove == 5:
                print("\nHigh graded students")
                findHighGradedStudents()
            elif nextMove == 6:
                break
            else:
                print("\nWrong data entered")
    else:
        print("Wrong data input!")

while True:
    userInfo = int(input('\nWho are you:\nStudent - 1 \nAdmin - 0 \nStop - 2 \nEnter only number: '))
    if userInfo == 2:
        break
    else:
        checkUserStatus(userInfo)
