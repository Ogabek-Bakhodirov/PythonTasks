import csv
import random

usersInfoDB = {
    'users' : [], 
    'student_info' : [],
    'students_grade' : []
}

adminDB = []
studentDB = []
studentGradeDB = [] 
studentInfoDB = [] #{'ID':[], 'NAME':[], 'SURNAME':[], 'AGE':[], 'PAYMENTSTATUS':[]}

def copyFromCSV(fileDirection, passDataTo):
    # Check direction 
    with open(fileDirection, 'r') as file:
        csvreader = csv.reader(file)
        for info in csvreader:
            # Check Dictionary direction
            usersInfoDB[passDataTo].append(info)

copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/Students_grade.csv", "students_grade")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/Student_info.csv", "student_info")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/Users.csv", "users")

# Get data from usersInfoDB to Student/Admin
index = 0
while True:
    if len(usersInfoDB['users']) != index:
        user = usersInfoDB['users'][index]
        # Check if Student append to student DB
        if user[0][0] == 's':
            studentDB.append({'ID':user[0], 'PSW':user[1]})
        # Check if Admin append to admin DB
        elif user[0][0] == 'a':
            adminDB.append({'ID':user[0], 'PSW':user[1]})
        index += 1
    else:
        index = 0
        break

# Get data from usersInfoDB to StudentGrade db
while True:
    if len(usersInfoDB['students_grade']) != index:
        user = usersInfoDB['students_grade'][index]
        if user[0][0] == 's': # Fix: what if user[0][0] == ''
            studentGradeDB.append({"ID":user[0], "MATH":user[1],"PROGRAMMING":user[2],"DATABASE":user[3],"ENGLISH":user[4]})
        index += 1
    else:
        index = 0
        break

# Get data from usersInfoDB to StudentInfo db
while True:
    if len(usersInfoDB['student_info']) != index:
        user = usersInfoDB['student_info'][index]
        if user[0][0] == 's': # Fix: what if user[0][0] == ''
            studentInfoDB.append({'ID':user[0],'NAME':user[1],'SURNAME':user[2],'AGE':user[3],'PAYMENTSTATUS':user[4]})
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
    for i in studentDB:
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
    for value in studentDB:
        if studentID == value['ID']:
            return idGenerator()
    return studentID

# Function for checking student records.
def seeStudentRecords(studentID):
    for index, info in enumerate(studentDB):
        if info["ID"] == studentID:
            print('\nStudent ID: ' + studentDB[index]['ID'] + '\nStudent Password: ' + studentDB[index]['PSW'] + '\nStudent name: ' + studentInfoDB[index]["NAME"])
            print('Student surname: ' + studentInfoDB[index]["SURNAME"] + '\nStudent age: ' + studentInfoDB[index]["AGE"] + '\nStudent payment status: ' + studentInfoDB[index]["PAYMENTSTATUS"])
            print('Math grade: ' + studentGradeDB[index]["MATH"] + '\nProgramming grade: ' + studentGradeDB[index]["PROGRAMMING"])
            print('Database grade: ' + studentGradeDB[index]["DATABASE"] + '\nEnglish grade: ' + studentGradeDB[index]["ENGLISH"])
            return
    print('\nStudent id not found: 404')

# Registration of new student.
def studentRegistration():
    name = input('\nEnter your name: ')
    surname = input('Enter your surname: ')
    age = input('Enter your age: ')
    studentID = idGenerator()
    password = input('Enter your password: ')

    studentDB.append({'ID':studentID, 'PSW':password})
    studentInfoDB.append({'ID':studentID, 'NAME':name, 'SURNAME':surname,'AGE':age, 'PAYMENTSTATUS':'None'})
    studentGradeDB.append({"ID":studentID, "MATH":'0',"PROGRAMMING":'0',"DATABASE":'0',"ENGLISH":'0'})
    studentIdListGenerator()

    print(f'\nYour name: {name}\nYour surname: {surname}\nYour age: {age}\nYour student ID: {studentID}\nYour password: {password}\n')

    isContinue = int(input('\nWhat do you want to do next: \nSee records -> 0 \nStop -> 1: \nEnter only number: '))
    if isContinue == 0:
        studentID = input("\nEnter your student ID: ")
        seeStudentRecords(studentID)
    elif isContinue == 1:
        return True
    else:
        print('\nNot valid number entered !')
    
# Delete student's records
def deleteStudent(studentID):
    for index, student in enumerate(studentInfoDB):
        if studentID in student['ID']:
            # for index, value in enumerate(studentInfoDB):
                # if studentInfoDB[index]['ID'] == studentID:
            del studentDB[index]
            del studentInfoDB[index]
            del studentGradeDB[index]
            print("\nStudent's records deleted succesfully! ")
            studentIdListGenerator()
            return 
    print("\nIncorrect student ID entered! ")

# Change student's grades
def changeGrades(studentID):
    for student in studentGradeDB:
        if studentID in student['ID']:
            # Change student's grade
            index = 0
            for i in studentGradeDB:
                if studentGradeDB[index]['ID'] == studentID:
                    print("\n" + studentInfoDB[index]['NAME'] + " " + studentInfoDB[index]['SURNAME'] + " student ID - " + studentInfoDB[index]['ID'])
                    while True:
                        subject = int(input("\nWhich subject's grade you want to change: \nMath - 1: \nProgramming - 2: \nDatabase - 3: \nEnglish - 4: \nStop - 5 \nEnter only number -> "))
                        newGrade = input("\nEnter new grade: ") # Should fix loop breaking
                        match subject:
                            case 1:
                                studentGradeDB[index]['MATH'] = newGrade
                            case 2:
                                studentGradeDB[index]['PROGRAMMING'] = newGrade
                            case 3:
                                studentGradeDB[index]['DATABASE'] = newGrade
                            case 4:
                                studentGradeDB[index]['ENGLISH'] = newGrade
                            case 5:
                                break
                            case _:
                                print("Not valid value entered!")
                    return 
                index += 1
    print("\nIncorrect student ID entered! ")

# Change student's info
def changeStudentInfo(studentID):
    for student in studentInfoDB:
        if studentID in student['ID']:
            for index, value in enumerate(studentInfoDB):
                if studentID == studentInfoDB[index]['ID']:
                    newValue = input("Update payment status (Paid / Not Paid): ")
                    studentInfoDB[index]['PAYMENTSTATUS'] = newValue
                    return
    print("\nIncorrect student ID entered! ")

# Find failed students
def findFailedStudent():
    failedStudentsIDList = []
    for index in range(len(studentGradeDB)):
        gradeResult = int(studentGradeDB[index]['ENGLISH']) + int(studentGradeDB[index]['DATABASE']) + int(studentGradeDB[index]['MATH']) + int(studentGradeDB[index]['PROGRAMMING'])
        if (int(gradeResult) / 4) < 60:
            failedStudentsIDList.append(studentGradeDB[index]['ID'])
    print(failedStudentsIDList)

# Find high graded students
def findHighGradedStudents():
    highGradedStudentsIDList = []
    for index in range(len(studentGradeDB)):
        gradeResult = int(studentGradeDB[index]['ENGLISH']) + int(studentGradeDB[index]['DATABASE']) + int(studentGradeDB[index]['MATH']) + int(studentGradeDB[index]['PROGRAMMING'])
        if (int(gradeResult) / 4) > 86:
            highGradedStudentsIDList.append(studentGradeDB[index]['ID'])
    print(highGradedStudentsIDList)
 
def checkUserStatus(userInfo):
    # UserInfo - Student
    if userInfo == 1:
        # Choosen action (Register or See records)
        action = int(input('\nWhat you want to do: \nRegister - 0, \nSee my records - 1: \nEnter only number: '))
        # If action -> See records
        if action == 1:
            studentID = input("\nEnter your student ID: ")
            seeStudentRecords(studentID)
        elif action == 0:
            studentRegistration()
        else:
            print("Wrong data")

    # Admin Panel
    elif userInfo == 0:
        while True:
            # Add see students
            nextMove = int(input("\nWhat you want to do: \nDelete student's record - 1. \nChange grades - 2. \nChange student info - 3. \nFind Failed students - 4. \nFind high graded students - 5. \nStop - 6. \nEnter only number -> "))
            if nextMove == 1:
                deletedStudentID = input("\nEnter student id which you want to delete: ")
                deleteStudent(deletedStudentID)
            elif nextMove == 2: 
                studentIDForChangeGrade = input("\nEnter student id which you want to change grade: ")
                changeGrades(studentIDForChangeGrade)
            elif nextMove == 3:
                infoChangedStudentID = input("\nEnter student id which you want to change info: ")
                changeStudentInfo(infoChangedStudentID)
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

# # Write updated data to CSV file
def writeDataToCsv():
    directions = ["/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/New_Student_info.csv",
                  "/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/New_Students_grade.csv",
                  "/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/New_Student.csv",
                  "/Users/ogabekbakhodirov/Documents/Python/PythonTasks/CSVFiles/New_Admins.csv"]
    file_headers = [studentInfoDB[0].keys(), studentGradeDB[0].keys(), studentDB[0].keys(), adminDB[0].keys()]
    row_values = [studentInfoDB, studentGradeDB, studentDB, adminDB]

    for index, value in enumerate(directions):
       with open(directions[index], 'w') as file:
            # Create a CSV dictionary writer and add the student header as field names
            writer = csv.DictWriter(file, fieldnames=file_headers[index])
            # Use writerows() not writerow()
            writer.writeheader()
            writer.writerows(row_values[index])

while True:
    userInfo = int(input('\nWho are you:\nStudent - 1 \nAdmin - 0 \nStop - 2 \nEnter only number: '))
    if userInfo == 2:
        writeDataToCsv()
        break
    checkUserStatus(userInfo)
