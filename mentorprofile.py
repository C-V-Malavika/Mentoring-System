import csv

class Mentor:
    
    def __init__(self, name, department, email, mobile_number, landline, years_of_experience):
        self.name = name
        self.department = department
        self.email = email
        self.mobile_number = mobile_number
        self.landline = landline
        self.years_of_experience = years_of_experience
        self.next = None

class MentorLinkedList:
    
    def __init__(self):
        self.head = None

    # Method to add a new mentor to the linked list
    def add_mentor(self, name, department, email, mobile_number, landline, years_of_experience):
        new_mentor = Mentor(name, department, email, mobile_number, landline, years_of_experience)

        if self.head is None:
            self.head = new_mentor
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_mentor

    # Method to display all mentors in the linked list
    def display_mentors(self):
        current = self.head
        while current:
            print("MY PROFILE:")
            print("Name:", current.name)
            print("Department:", current.department)
            print("Email:", current.email)
            print("Mobile Number:", current.mobile_number)
            print("Landline:", current.landline)
            print("Years of Experience:", current.years_of_experience)

            # Save mentor profile as CSV file
            filename = f"{current.email}_profile.csv"
            self.save_mentor_profile_as_csv(current, filename)
            print(f"Mentor profile saved as {filename}")

            current = current.next

    def save_mentor_profile_as_csv(self, mentor, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Department", "Email", "Mobile Number", "Landline", "Years of Experience"])
            writer.writerow([mentor.name, mentor.department, mentor.email, mentor.mobile_number, mentor.landline, mentor.years_of_experience])

mentor_list = MentorLinkedList()

mentor_list.add_mentor("K.S.Gayathri", "DEPARTMENT OF INFORMATION TECHNOLOGY", "gayathriks@ssn.edu.in", "7894562344", "04567231235", "20 years")
mentor_list.add_mentor("N.Sripriya", "DEPARTMENT OF INFORMATION TECHNOLOGY", "sripriyan@ssn.edu.in", "9778456677", "04455666123", "20 years")

mentor_list.display_mentors()
