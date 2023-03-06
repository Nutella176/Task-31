class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Adding another method in the Course class that prints the head office location: Cape Town
    def office_location(self):
        print("Head office location: Cape Town")


# Creating a subclass of the Course class named OOPCourse
class OOPCourse(Course):
    # Creating a constructor that initialises default attributes for 'description' and 'trainer'
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # Creating a method that prints what the course is about and the name of the trainer by using the description and trainer attributes
    def trainer_details(self):
        print(
            f"The course is about {self.description} and the trainer is {self.trainer}"
        )

    # Creating a method that prints the ID number of the course: #12345
    def show_course_id(self):
        print(f"The ID number of the course is #12345")


# Creating an object of the subclass which calls contact_details, trainer_details and show_course_id
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
