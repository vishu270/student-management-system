import json
from pathlib import Path


class Student:

    database = "data.json"
    data = []

    if Path(database).exists():
        with open(database, "r") as file:
            try:
                data = json.load(file)
            except:
                data = []

    @staticmethod
    def save():

        with open(Student.database, "w") as file:
            json.dump(Student.data, file, indent=4)


    #--------------------------------------

    @staticmethod
    def get_student(name, roll):

        for student in Student.data:

            if student["name"] == name and student["Rollno"] == roll:
                return student

        return None


    #--------------------------------------

    def create_student(self, info):

        Student.data.append(info)
        Student.save()


    #--------------------------------------

    def update_marks(self, name, roll, marks):

        student = Student.get_student(name, roll)

        if student:

            student["subjects"] = marks

            total = sum(marks.values())

            percentage = (total/500)*100

            student["percentage"] = round(percentage,2)

            Student.save()

            return True

        return False


    #--------------------------------------

    def delete_student(self, name, roll):

        student = Student.get_student(name, roll)

        if student:

            Student.data.remove(student)

            Student.save()

            return True

        return False


    #--------------------------------------

    def topper(self):

        if not Student.data:
            return None

        topper = max(
            Student.data,
            key=lambda x:x["percentage"]
        )

        return topper


    #--------------------------------------

    def all_students(self):

        return Student.data