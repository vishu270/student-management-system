    # student management system
import numpy as np
from pathlib import Path   
import random 
import string
import json




class Student:
        database = "data.json"
        data=[]

        
        try:
            if Path(database).exists():
                with open(database,'r') as fs:
                    data = json.load(fs)
            else:
                print("file not found")
        except Exception as err:
            print(f" error occured {err}")
                    

        @staticmethod
        def __update():
            with open(Student.database, 'w') as fs:
                fs.write(json.dumps(Student.data))

    
        def createstudent(self):
            info = {
                "name" : input("Enter the student name:").strip(),
                "Rollno": int(input("Enter the roll no. of student:")),
                "Gender" : input("Enter gender:"),
                "contact_no." : int(input("Enter the contact no.:")),
                "subjects": {
                        "Maths": 0,
                        "Physics": 0,
                        "Python": 0,
                        "Java": 0,
                        "Chemistry": 0
                        },
                "percentage":0
            }

            Student.data.append(info)
            Student.__update()



        def viewstudentprofile(self):
            name = input("Enter the student name:").strip()
            Rollno = int(input("Enter the Roll NO.:"))

            userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]

            if not userdata:
                print("invaild detail")
            else:
                print(Student.data)





        def entermarks(self):
            name = input("Enter the student name:").strip()
            Rollno = int(input("Enter the Roll NO.: "))
      
            userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]

            if not userdata:
                print("invalid student detail or rollno.")
            else:
                for subject in userdata[0]["subjects"]:
                    marks = int(input(f"Enter {subject} marks:"))
                    userdata[0]["subjects"] [subject] = marks
                    Student.__update()
            print("marks are enter successfull")


        def viewmarks(self):
             name = input("Enter the student name:").strip()
             Rollno = int(input("Enter the Roll NO.:"))
            
             userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]

             if not userdata:
                print("invaild detail")
             else:
                print(userdata[0]["subjects"]) 


        def updatestudent(self):
             name = input("Enter the student name:").strip()
             Rollno = int(input("Enter the Roll NO.: "))
        
             userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]


             if not userdata:
                print("invaild detail")
             else:
                print("you cant update your subject")

                print("Enter what you want to update")
                newdata={
                         "name": input("Enter updated name:"),
                         "Rollno" : int(input("Enter the updated Rollno.:")),
                         "contact_no.": int(input("Enter the Updated **Contact no.:")),
                         "Gender":input("Enter the gender :")
                        }
                
                if newdata["name"] =="":
                    newdata["name"] == userdata[0]["name"] 
                                 
                if newdata["Rollno"] =="":
                    newdata["Rollno"] == userdata[0]["Rollno"] 
                
                if newdata["contact_no."] =="":
                    newdata["contact_no."] == userdata[0]["contact_no."]
                
                if newdata["Gender"] =="":
                    newdata["Gender"] == userdata[0]["Gender"]
                
                
                newdata["subjects"] = userdata[0]["subjects"]

                print(newdata)
                for i in newdata:
                    if newdata[i] == userdata[0][i]:
                        continue
                    else:
                        userdata[0][i] = newdata[i]

                Student.__update()

                print("student updated successfully : )")
                

        def delete(self):
             name = input("Enter the student name:").strip()
             Rollno = int(input("Enter the Roll NO.: "))
                    
             userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]
            
            
             if not userdata:
                print("invaild detail")
             else:
                 Student.data.pop()

                 Student.__update()

             print("student remove successfully")


               

                                            

        def percentage(self):
             total_marks= 500

             name = input("Enter the student name:").strip()
             Rollno = int(input("Enter the Roll NO.: "))
                    
             userdata = [i for i in Student.data if i["name"] == name and i["Rollno"] == Rollno ]
            
            
             if not userdata:
                print("invaild detail")
             else:
                sum = 0
                for subject in userdata[0]["subjects"]:
                   marks =  userdata[0]["subjects"] [subject] 
                   print(marks)
                   sum = sum + marks
                print(sum)

                percent = (sum / total_marks)*100

                print(percent)

                userdata[0]["percentage"]=percent
                Student.__update()
                print("percentage update hogai hai")

        def Topper(self):
            highest_percentage = 0
            topper_student = None

            for student in Student.data:

              if student["percentage"] > highest_percentage:
                 highest_percentage = student["percentage"]
                 topper_student = student

            print("\nTOPPER STUDENT")
            print("-------------------")
            print("Name :", topper_student["name"])
            print("Roll No :", topper_student["Rollno"])
            print("Percentage :", topper_student["percentage"])





        
        
    
        
    


print("Welcome to the student management system")   
print("Enter your choice: ")
print("1. Create student profile")
print("2. View student profile")
print("3. Enter subject marks")
print("4. View student marks")
print("5. Update student profile")
print("6. Delete student profile" )
print("7. getting a percentage of marks")
print("8. getting a Topper student")


check = int(input("Enter your choice:"))

user = Student()

if check == 1:
    user.createstudent()

if check == 2:
    user.viewstudentprofile()

if check == 3:
    user.entermarks()

if check == 4:
    user.viewmarks()

if check == 5:
    user.updatestudent()


if check == 6:
    user.delete()

if check == 7:
    user.percentage()

if check == 8 :
    user.Topper()