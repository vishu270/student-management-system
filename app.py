import streamlit as st
from student import Student


obj = Student()

st.title("Student Management System")


menu = st.sidebar.selectbox(

    "Select",

    [

        "Create Student",
        "View Student",
        "Enter Marks",
        "Delete Student",
        "Topper",
        "All Students"

    ]

)


#=========================================

if menu=="Create Student":

    st.header("Create Student")


    name = st.text_input("Name")
    roll = st.number_input("Roll No",1)
    gender = st.selectbox(

        "Gender",

        ["Male","Female","Other"]

    )

    contact = st.text_input("Contact Number")


    if st.button("Create"):

        data = {

            "name":name,
            "Rollno":roll,
            "Gender":gender,
            "contact_no.":contact,

            "subjects":{

                "Maths":0,
                "Physics":0,
                "Python":0,
                "Java":0,
                "Chemistry":0

            },

            "percentage":0

        }


        obj.create_student(data)

        st.success("Student Added Successfully")


#=====================================

elif menu=="View Student":

    name = st.text_input("Name")
    roll = st.number_input("Roll Number",1)

    if st.button("Search"):

        student = Student.get_student(name,roll)

        if student:

            st.write(student)

        else:
            st.error("Student Not Found")


#====================================

elif menu=="Enter Marks":

    name = st.text_input("Name")
    roll = st.number_input("Roll",1)


    maths = st.number_input("Maths",0,100)
    physics = st.number_input("Physics",0,100)
    python = st.number_input("Python",0,100)
    java = st.number_input("Java",0,100)
    chemistry = st.number_input("Chemistry",0,100)


    if st.button("Submit Marks"):


        marks = {

            "Maths":maths,
            "Physics":physics,
            "Python":python,
            "Java":java,
            "Chemistry":chemistry

        }


        if obj.update_marks(name,roll,marks):

            st.success("Marks Updated")

        else:

            st.error("Student Not Found")


#====================================

elif menu=="Delete Student":

    name = st.text_input("Name")
    roll = st.number_input("Roll No",1)


    if st.button("Delete"):

        if obj.delete_student(name,roll):

            st.success("Deleted Successfully")

        else:

            st.error("Student Not Found")


#====================================

elif menu=="Topper":

    topper = obj.topper()


    if topper:

        st.subheader("Topper Student")

        st.write("Name :",topper["name"])
        st.write("Roll :",topper["Rollno"])
        st.write(
            "Percentage :",
            topper["percentage"]
        )


#=====================================

elif menu=="All Students":

    st.write(obj.all_students())