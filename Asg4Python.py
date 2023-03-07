
import csv

studentsInfoDB = {
    'users' : [], 
    'student_info' : [],
    'students_grade' : []
}

users = {'ID':[], 'PSW': []}
studentGrade = {'ID':[], 'MATH':[], 'PROGRAMMING':[], 'DATABASE':[], 'ENGLISH':[]}
studentInfo = {'ID':[], 'NAME':[], 'SURNAME':[], 'AGE':[], 'PAYMENTSTATUS':[]}

def copyFromCSV(fileDirection, csvMode, passDataTo):
    # Check direction 
    with open(fileDirection, csvMode) as file:
        csvreader = csv.reader(file)
        for info in csvreader:
            # Check Dictionary direction
            studentsInfoDB[passDataTo].append(info)

copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Students_grade.csv", "r", "students_grade")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Student_info.csv", "r", "student_info")
copyFromCSV("/Users/ogabekbakhodirov/Documents/Python/PythonTasks/Users.csv", "r", "users")

for i in studentsInfoDB["users"]:
    users["ID"].append(i[0])
    users["PSW"].append(i[1])

for i in studentsInfoDB["students_grade"]:
    studentGrade["ID"].append(i[0])
    studentGrade["MATH"].append(i[1])
    studentGrade["PROGRAMMING"].append(i[2])
    studentGrade["DATABASE"].append(i[3])
    studentGrade["ENGLISH"].append(i[4])

for i in studentsInfoDB["student_info"]:
    studentInfo["ID"].append(i[0])
    studentInfo["NAME"].append(i[1])
    studentInfo["SURNAME"].append(i[2])
    studentInfo["AGE"].append(i[3])
    studentInfo["PAYMENTSTATUS"].append(i[4])

def checkUserStatus(userInfo):
    # UserInfo - Student
    if userInfo == 1:
        # Choosen action (Register or See records)
        action = int(input('What you want to do: Register - 0, See my records - 1: '))
        # If action == 1
        if action == 1:
            studentID = input("Enter your student ID: ")
            index = 0
            for info in users['ID']:
                if info == studentID:
                    print('Student ID: ' +  users['ID'][index])
                    print('Student Password: ' + users['PSW'][index])    
                    print('Math grade: ' + studentGrade["MATH"][index])
                    print('Programming grade: ' + studentGrade["PROGRAMMING"][index])
                    print('Database grade: ' + studentGrade["DATABASE"][index])
                    print('English grade: ' + studentGrade["ENGLISH"][index])
                    print('Student name: ' + studentInfo["NAME"][index])
                    print('Student surname: ' + studentInfo["SURNAME"][index])
                    print('Student age: ' + studentInfo["AGE"][index])
                    print('Student payment status: ' + studentInfo["PAYMENTSTATUS"][index])  
                    return True
                index += 1 
            print('Student id not found: 404')       

userInfo = int(input('Who are you: If Student - 1, If Admin - 0: '))
checkUserStatus(userInfo)
