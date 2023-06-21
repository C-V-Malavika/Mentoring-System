


import json

class per_Student:
    def __init__(self, name, aadharnumber, firstname,lastname,email,mobilenumber,bloodgroup,dateofbirth,gender,nationality,religion,differentlyabled,typeofdisability,community,mothertongue):
        self.name = name
        self.aadharnumber = aadharnumber
        self.firstname = firstname
        self.lastname=lastname
        self.email=email
        self.mobilenumber=mobilenumber
        self.bloodgroup=bloodgroup
        self.dateofbirth=dateofbirth
        self.gender=gender
        self.nationality=nationality
        self.religion=religion
        self.differentlyabled=differentlyabled
        self.typeofdisability=typeofdisability
        self.community=community
        self.mothertongue=mothertongue

class Admissiondetails:
    def __init__(self,programname,associateddepartment,modeofadmission,admissioncategory):
        self.programname=programname
        self.associateddepartment=associateddepartment
        self.modeofadmission=modeofadmission
        self.admissioncategory=admissioncategory

class Sslcdetails:
    def __init__(self,schooladdress,yearofpassing,boardoruniversity,group,percentage):
        self.schooladdress=schooladdress
        self.yearofpassing=yearofpassing
        self.boardoruniversity=boardoruniversity
        self.group=group
        self.percentage=percentage


class Hscdetails:
    def __init__(self,schooladdress,yearofpassing,boardofstudy,group,percentage,maths,physics,chemistry):
        self.schooladdress=schooladdress
        self.yearofpassing=yearofpassing
        self.boardofstudy=boardofstudy
        self.group=group
        self.percentage=percentage
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry

class Address:
    def __init__(self,currentaddress,permanentaddress):
        self.currentaddress=currentaddress
        self.permanentaddress=permanentaddress

class Fatherdetails:
    def __init__(self,name,email,mobilenumber,dateofbirth,qualification,occupation,designation,annualincome):
        self.name=name
        self.email=email
        self.mobilenumber=mobilenumber
        self.dateofbirth=dateofbirth
        self.qualification=qualification
        self.occupation=occupation
        self.designation=designation
        self.annualincome=annualincome

class Motherdetails:  
    def __init__(self,name,email,mobilenumber,dateofbirth,qualification,occupation,designation,annualincome):
        self.name=name
        self.email=email
        self.mobilenumber=mobilenumber
        self.dateofbirth=dateofbirth
        self.qualification=qualification
        self.occupation=occupation
        self.designation=designation
        self.annualincome=annualincome 

class StudentDetails:
   def __init__(self, personaldetails, admissiondetails, sslcdetails, hscdetails, address, fatherdetails, motherdetails):
    self.personaldetails = personaldetails
    self.admissiondetails = admissiondetails
    self.sslcdetails = sslcdetails
    self.hscdetails = hscdetails
    self.address = address
    self.fatherdetails = fatherdetails
    self.motherdetails = motherdetails

# Create an array to store student objects
students = []
for i in range(1,11):
# Add student profiles to the array
 if i==1:
  student=per_Student("John Doe K", 232345678567, "John Doe","K","johndoe223456@ssn.edu.in","7890765432","b+","23/08/2004","male","indian","christian","yes","leg","bc","tamil")
  admission=Admissiondetails("B.tech Information technology","Information Technology","Management","General")
  sslc=Sslcdetails("no36,leocolony,COIMBATORE","2020","Tamilnadu board","NA","98")
  hsc=Hscdetails("no36,leocolony,COIMBATORE","2022","Tamilnadu board","bio","97","97","90","99")
  address=Address("4a,bommalattam street,Coimbatore","4a,bommalattam street,Coimbatore")
  father=Fatherdetails("Krish","xcvbnm#+@gmail.com","9087340912","5-3-1970","SSLC","Governmnt officer","Clerk","500000")
  mother=Motherdetails("Ragavi","xcvbnm#+@gmail.com","7373987632","5-09-198","SSLC","Governmnt officer","postmaster","650000")

  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

  # Add student profiles to the array
 if i==2:
  student=per_Student("Santhosh Kumar M", 232345678890, "Santhosh Kumar","M","Santhosh223456@ssn.edu.in","7763087618","o+","23/07/2004","male","indian","hindu","no","NA","bc","tamil")
  admission=Admissiondetails("B.E.Computer science","computer science","counselling","7.5 reservation")
  sslc=Sslcdetails("no334,kamarajarcolony,Erode","2020","Tamilnadu board","NA","80")
  hsc=Hscdetails("no334,kamarajarcolony,Erode","2022","Tamil board","computer science","85","80","70","90")
  address=Address("street no 14,gandhi street Erode","street no 14,gndhi street Erode")
  father=Fatherdetails("Madhvan","madhvan2390#+@gmail.com","7436091096","15-3-1975","HSC","Governmnt officer","clerk","500000")
  mother=Motherdetails("Radha","radha567#+@gmail.com","98714307634","5-3-1980","SSLC","house wife","NA","NA")

  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==3:
  student=per_Student("Deepak chahar", 333456712073, "deppak","chahar","deepakchahar2236@ssn.edu.in","9845673043","AB-VE","23/12/2004","male","indian","hindu","no","NA","bc","telugu")
  admission=Admissiondetails("B.tech Information technology","Information Technology","counselling","General")
  sslc=Sslcdetails("no36,monk street , krishnagiri","2020","Telangana board","NA","98")
  hsc=Hscdetails("no36,monk street , krishnagiri","2022","Telangana board","bio","95","97","90","95")
  address=Address("no 234, priest street krishnagiri ","no 234, priest street krishnagiri")
  father=Fatherdetails("Murali","muralimurali@gmail.com","723456098","30-06-1969","BE mechanical engineeing ","mechanical engineer","manager","1500000")
  mother=Motherdetails("sumathi","sumathinm#+@gmail.com","989458582","5-3-1975","M.A.B.ed","Governmnt officer","Teacher","1200000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==4:
  student=per_Student("Monica P", 232345678234, "Monica ","P","monica90@ssn.edu.in","9897645321","A+","03/10/2004","Female","indian","Indian","no","NA","bc","tamil")
  admission=Admissiondetails("B.E.Mechanical engineering","Mechanical","Management","General")
  sslc=Sslcdetails("mannar salai,Mettur, Salem","2020","Tamilnadu board","NA","98")
  hsc=Hscdetails("mannar salai,Mettur, Salem","2022","Tamilnadu board","bio","97","97","90","99")
  address=Address("FLAT NO :87,Saradha apartment,Salem","FLAT NO :87,Saradha apartment,Salem")
  father=Fatherdetails("Prabhakaran","prabh#@gmail.com","9090987654","5-5-1970","b.com","Governmnt officer","Bank manager","1000000")
  mother=Motherdetails("Reema","Reema5+@gmail.com","9234567890","25-08-1985","B.E.Chemical engineering ","Chief chemical engineer","Team manager","1256000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)     

 if i==5:
  student=per_Student("Sharukh Khan J", 23234567878, "Sharukh Khan","J","sharukhkhan2210345@ssn.edu.in","7809999888","A+ve","28/08/2004","male","indian","Muslim","yes","hand","bc","Hindi")
  admission=Admissiondetails("B.tech Cyber security","Computer Science","counselling","General")
  sslc=Sslcdetails("Varisu street,mettiyoli nagar,Chrompet,Chennai","2020","board","NA","98")
  hsc=Hscdetails("Varisu street,mettiyoli nagar,Chrompet,Chennai","2022","Tamilnadu board","bio","92","93","90","98")
  address=Address("Flat no:4,Manju Apartrment,Anna nagar,Chrompet","Flat no:4,Anna nagar,Chrompet")
  father=Fatherdetails("Lokesh khan","lokesh23456@gmail.com","8454665789","15-8-1965","SSLC"," private employer","chief executive officer","123456000")
  mother=Motherdetails("Shreya Saran","shreyasaran123@gmail.com","7654890995","25-3-1970","HSC","Governmnt officer","Bank manager","123456000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==6:
  student=per_Student("Sujith Bala v", 2323498765678, "Sujith Bala ","V","sujithbala6786@ssn.edu.in","9876530130","AB-ve","28/01/2004","male","indian","Hindu","no","NA","SC","tamil")
  admission=Admissiondetails("B.E.Biomediical Engineering ","Biomedical","Counselling","SC/ST category")
  sslc=Sslcdetails("No:7,Bagalur Hudco,Hosur","2020","Tamilnadu board","NA","80")
  hsc=Hscdetails("No:7,Bagalur Hudco,Hosur","2022","board","bio","85","90","85","95")
  address=Address("plot no:80,vivekanandar street ,Hosur","plot no:80,vivekanandar street,Hosur")
  father=Fatherdetails("Vivek S","vivek987@gmail.com","87678909845","31-01-1970","B.Ed","Government employee","Teacher","1000000")
  mother=Motherdetails("Sunitha","NA","7890123450","21-02-1973","SSLC","House wife ","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==7:
  student=per_Student("Danesh M", 40089076456, "Danesh","M","danesh2210769@ssn.edu.in","7890789750","B+","11/06/2005","male","Indian","Hindu","No","NA","Bc","Telugu")
  admission=Admissiondetails("B.tech Information technology","Information Technology","counselling","General")
  sslc=Sslcdetails("NGO's colony,Puttur","2020","AP board","NA","97")
  hsc=Hscdetails("NGO's colony,Puttur","2022","AP board","MPC","96","99","90","100")
  address=Address("Sri krishna Colony , Puttur","Sri krishna Colony , Puttur")
  father=Fatherdetails("Ramesh","ramesh56+@gmail.com","9087434007","17-06-1970","BE ","private employee","civil engineer","1200000")
  mother=Motherdetails("vedhavathi","vedha@gmail.com","9959522708","3-01-1973","SSLC","house wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==8:
  student=per_Student("Manju Sri S ", 331209324, "Manju Sri ","S","manjusri2210732@ssn.edu.in","9360820940","O+","23/06/2004","Female","indian","Hindu","No","NA","bc","telugu")
  admission=Admissiondetails("B.tech Information technology","Information Technology","counselling","General")
  sslc=Sslcdetails("phase 2, Bagalur hudco , HOsur","2020","Tamilnadu board","NA","99")
  hsc=Hscdetails("Phase 2 , Bagalur hudco , Hosur","2022","Tamilnadu board","bio","97","97","100","99")
  address=Address("Plot no:36 valluvar Nagar , Rayakotta road ,Hosur","Plot no:36 valluvar Nagar , Rayakotta road ,Hosur")
  father=Fatherdetails("Suresh S ","Suresh15@gmail.com","9894006470","13-12-1970","BE.Mechanical Engineering ","Mechanical ENgineer","Senior Manager","2000000")
  mother=Motherdetails("Rag","xcvbnm#+@gmail.com","1234567","5-3-1990","SSLC","Governmnt officer","Bank manager","123456000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==9:
  student=per_Student("Farthima S", 4567890145, "Farthima","S","Farthmia600112@ssn.edu.in","9894006485","A-ve","01/01/2004","Female","indian","Muslim","no","NA","BC","Hindi")
  admission=Admissiondetails("B.E Civil Engineering","Civil","Counselling","General")
  sslc=Sslcdetails("No:12,Race course,Coimbatore","2020","board","NA","90")
  hsc=Hscdetails("No:12,Race course,Coimbatore","2022","board","bio","95","98","90","96")
  address=Address("No:12,Maharani avenue,Vadavalli,Coimbatore","No:12,Maharani avenue,Vadavalli,Coimbatore")
  father=Fatherdetails("Sherif","sherif123@gmail.com","9090765438","25-07-1970","CA","Governmnt officer","Auditor","2550000")
  mother=Motherdetails("Rafikka","Rafikka045@gmail.com","9891234567","13-07-1975","B.com","Governmnt officer","Bank employee","900000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==10:
  student=per_Student("Vithula S", 333456712309, "Vithula","S","vithula316@ssn.edu.in","7989400642","B-ve","31/03/2003","Female","indian","Hindu","No","NA","Bc","Tamil")
  admission=Admissiondetails("B.tech Information technology","Information Technology","Management","General")
  sslc=Sslcdetails("89,Phase1,chrompet ,Chennai","2020","CBSE","NA","98")
  hsc=Hscdetails("89,Phase1,chrompet ,Chennai","2022","board","bio","97","97","90","99")
  address=Address("no:09,lotus apartment,Sholinganallur,Chennai","no:09,lotus apartment,Sholinganallur,Chennai")
  father=Fatherdetails("Srinivasan ","shri00@gmail.com","986545342","17-06-1975","BE.Computer Science","Software Engineer","Executive","2000000")
  mother=Motherdetails("Dhana","dhana03@gmail.com","9897650987","18-11-1980","B.com","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)
  
 
#students.append(Student("Mike Johnson", 19, "C"))
# Convert student profiles to a dictionary
student_dict = {}
for i, student in enumerate(students):
    info = {} 
    info['personal_info'] = {
        "name": student.personaldetails.name,
        "aadharnumber": student.personaldetails.aadharnumber,
        "firstname": student.personaldetails.firstname,
        "lastname": student.personaldetails.lastname,
        "email": student.personaldetails.email,
        "mobilenumber": student.personaldetails.mobilenumber,
        "bloodgroup": student.personaldetails.bloodgroup,
        "dateofbirth": student.personaldetails.dateofbirth,
        "gender": student.personaldetails.gender,
        "nationality": student.personaldetails.nationality,
        "religion": student.personaldetails.religion,
        "differentlyabled": student.personaldetails.differentlyabled,
        "typeofdisability": student.personaldetails.typeofdisability,
        "community": student.personaldetails.community,
        "mothertongue": student.personaldetails.mothertongue
    }

    if student.admissiondetails:
        info['admission_details'] = {
            'programname': student.admissiondetails.programname,
            'associateddepartment': student.admissiondetails.associateddepartment,
            'modeofadmission': student.admissiondetails.modeofadmission,
            'admissioncategory': student.admissiondetails.admissioncategory
        }

    if student.sslcdetails:
        info["sslc_details"]={
            'schooladdress':student.sslcdetails.schooladdress,
            'yearofpassing':student.sslcdetails.yearofpassing,
            'boardoruniversity':student.sslcdetails.boardoruniversity,
            'group':student.sslcdetails.group,
            'percentage':student.sslcdetails.percentage

        }

    if student.hscdetails:
        info["hscdetails"]={
            'schooladdress': student.hscdetails.schooladdress,
            'yearofpassing':student.hscdetails.yearofpassing,
            'boardofstudy':student.hscdetails.boardofstudy,
            'group':student.hscdetails.group,
            'percentage':student.hscdetails.percentage,
            'maths':student.hscdetails.maths,
            'physics':student.hscdetails.physics,
            'chemistry':student.hscdetails.chemistry


        }
    if student.address:
        info["address"]={
            "currentaddress":student.address.currentaddress,
            "permanentaddress":student.address.permanentaddress
        }
    student_dict[student.personaldetails.email] = info

    if student.fatherdetails:
     info["father"] = {
        "name": student.fatherdetails.name,
        "email": student.fatherdetails.email,
        "mobilenumber": student.fatherdetails.mobilenumber,
        "dateofbirth": student.fatherdetails.dateofbirth,
        "qualification": student.fatherdetails.qualification,
        "occupation": student.fatherdetails.occupation,
        "designation": student.fatherdetails.designation,
        "annualincome": student.fatherdetails.annualincome
    }

    if student.motherdetails:
     info["mother"] = {
        "name": student.motherdetails.name,
        "email": student.motherdetails.email,
        "mobilenumber": student.motherdetails.mobilenumber,
        "dateofbirth": student.motherdetails.dateofbirth,
        "qualification": student.motherdetails.qualification,
        "occupation": student.motherdetails.occupation,
        "designation": student.motherdetails.designation,
        "annualincome": student.motherdetails.annualincome
    }


# Save student profiles to a file
with open('student_profiles.json', 'w') as file:
    json.dump(student_dict, file)

# Load student profiles from the file
with open('student_profiles.json', 'r') as file:
    loaded_dict = json.load(file)

# Accessing and printing student profiles from the loaded dictionary
for key, value in loaded_dict.items():
    print(f"email: {key}")
    personal_info = value['personal_info']
    
    admission_details = value.get('admission_details', {})
    sslc_details=value.get('sslc_details',{})
    hsc_details=value.get('hsc_details',{})
    address=value.get('address',{})
    father=value.get('father',{})
    mother=value.get('mother',{})
      # Use .get() to handle missing key
    print(f"Name as in aadhar: {personal_info['name']}")
    print(f"aadharnumber: {personal_info['aadharnumber']}")
    print(f"firstname: {personal_info['firstname']}")
    print(f"lastname: {personal_info['lastname']}")
    print(f"mobilenumber: {personal_info['mobilenumber']},/n")
    print(f"bloodgroup: {personal_info['bloodgroup']},/n")
    print(f"dateofbirth: {personal_info['dateofbirth']}")
    print(f"gender: {personal_info['gender']}")
    print(f"Nationality: {personal_info['nationality']}")
    print(f"Differentlyabled: {personal_info['differentlyabled']}")
    print(f"Type of disability: {personal_info['typeofdisability']}")
    print(f"community category: {personal_info['community']}")
    print(f"Religion: {personal_info['religion']}")
    print(f"Mother tongue: {personal_info['mothertongue']}")
    print(f"programname: {admission_details.get('programname', '')}")
    print(f"associateddepartment: {admission_details.get('associateddepartment', '')}")
    print(f"modeofadmission: {admission_details.get('modeofadmission', '')}")
    print(f"admissioncategory: {admission_details.get('admissioncategory','')}")
    print(f"school address:{sslc_details.get('schooladdress','')}")
    print(f"year of passing:{sslc_details.get('yearofpassing','')}")
    print(f"board or university:{sslc_details.get('boardoruniversity','')}")
    print(f"group:{sslc_details.get('group','')}")
    print(f"percentage:{sslc_details.get('percentage','')}")
    print(f"school address:{hsc_details.get('schooladdress','')}")
    print(f"year of passing:{hsc_details.get('yearofpassing','')}")
    print(f"board or university:{hsc_details.get('boardofstudy','')}")
    print(f"group:{hsc_details.get('group','')}")
    print(f"percentage:{hsc_details.get('percentage','')}")
    print(f"maths:{hsc_details.get('maths','')}")
    print(f"physics:{hsc_details.get('physics','')}")
    print(f"chemistry:{hsc_details.get('chemistry','')}")
    print(f"current address:{address.get('currentaddress','')}")
    print(f"permanent address:{address.get('permanentaddress','')}")
    print(f"father name:{father.get('name','')}")
    print(f"email:{father.get('email','')}")
    print(f"mobilenumber:{father.get('mobilenumber','')}")
    print(f"date of birth:{father.get('dateofbirth','')}")
    print(f"qualification:{father.get('qualification','')}")
    print(f"occupation:{father.get('occupation','')}")
    print(f"designation:{father.get('designation','')}")
    print(f"annaulincome:{father.get('annualincome','')}")
    print(f"mother name:{mother.get('name','')}")
    print(f"email:{mother.get('email','')}")
    print(f"mobilenumber:{mother.get('mobilenumber','')}")
    print(f"date of birth:{mother.get('dateofbirth','')}")
    print(f"qualification:{mother.get('qualification','')}")
    print(f"occupation:{mother.get('occupation','')}")
    print(f"designation:{mother.get('designation','')}")
    print(f"annaulincome:{mother.get('annualincome','')}")
   
    print()

import csv
def write_student_profiles_to_csv(students, filename):
    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                  'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                  'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                  'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                  'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                  'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                  'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                  'Father Occupation', 'Father Designation', 'Father Annual Income',
                  'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                  'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
        writer.writerow(header)

        # Write each student's profile as a row in the CSV file
        for student in students:
            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)

            students = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]
    # Add student objects he]

filename = 'student_profiles.csv'

write_student_profiles_to_csv(students, filename)


import csv



def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("John Doe K", 232345678567, "John Doe","K","johndoe223456@ssn.edu.in","7890765432","b+","23/08/2004","male","indian","christian","yes","leg","bc","tamil"),
  Admissiondetails("B.tech Information technology","Information Technology","Management","General"),
  Sslcdetails("no36,leocolony,COIMBATORE","2020","Tamilnadu board","NA","98"),
  Hscdetails("no36,leocolony,COIMBATORE","2022","Tamilnadu board","bio","97","97","90","99"),
  Address("4a,bommalattam street,Coimbatore","4a,bommalattam street,Coimbatore"),
  Fatherdetails("Krish","xcvbnm#+@gmail.com","9087340912","5-3-1970","SSLC","Governmnt officer","Clerk","500000"),
  Motherdetails("Ragavi","xcvbnm#+@gmail.com","7373987632","5-09-198","SSLC","Governmnt officer","postmaster","650000"))]

# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Santhosh Kumar M", 232345678890, "Santhosh Kumar","M","Santhosh223456@ssn.edu.in","7763087618","o+","23/07/2004","male","indian","hindu","no","NA","bc","tamil"),
  Admissiondetails("B.E.Computer science","computer science","counselling","7.5 reservation"),
  Sslcdetails("no334,kamarajarcolony,Erode","2020","Tamilnadu board","NA","80"),
  Hscdetails("no334,kamarajarcolony,Erode","2022","Tamil board","computer science","85","80","70","90"),
  Address("street no 14,gandhi street Erode","street no 14,gndhi street Erode"),
  Fatherdetails("Madhvan","madhvan2390#+@gmail.com","7436091096","15-3-1975","HSC","Governmnt officer","clerk","500000"),
  Motherdetails("Radha","radha567#+@gmail.com","98714307634","5-3-1980","SSLC","house wife","NA","NA"))]

# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Deepak chahar", 333456712073, "deppak","chahar","deepakchahar2236@ssn.edu.in","9845673043","AB-VE","23/12/2004","male","indian","hindu","no","NA","bc","telugu"),
  Admissiondetails("B.tech Information technology","Information Technology","counselling","General"),
  Sslcdetails("no36,monk street , krishnagiri","2020","Telangana board","NA","98"),
  Hscdetails("no36,monk street , krishnagiri","2022","Telangana board","bio","95","97","90","95"),
  Address("no 234, priest street krishnagiri ","no 234, priest street krishnagiri"),
  Fatherdetails("Murali","muralimurali@gmail.com","723456098","30-06-1969","BE mechanical engineeing ","mechanical engineer","manager","1500000"),
  Motherdetails("sumathi","sumathinm#+@gmail.com","989458582","5-3-1975","M.A.B.ed","Governmnt officer","Teacher","1200000"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Monica P", 232345678234, "Monica ","P","monica90@ssn.edu.in","9897645321","A+","03/10/2004","Female","indian","Indian","no","NA","bc","tamil"),
  Admissiondetails("B.E.Mechanical engineering","Mechanical","Management","General"),
  Sslcdetails("mannar salai,Mettur, Salem","2020","Tamilnadu board","NA","98"),
  Hscdetails("mannar salai,Mettur, Salem","2022","Tamilnadu board","bio","97","97","90","99"),
  Address("FLAT NO :87,Saradha apartment,Salem","FLAT NO :87,Saradha apartment,Salem"),
  Fatherdetails("Prabhakaran","prabh#@gmail.com","9090987654","5-5-1970","b.com","Governmnt officer","Bank manager","1000000"),
  Motherdetails("Reema","Reema5+@gmail.com","9234567890","25-08-1985","B.E.Chemical engineering ","Chief chemical engineer","Team manager","1256000"))]

  


# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Sharukh Khan J", 23234567878, "Sharukh Khan","J","sharukhkhan2210345@ssn.edu.in","7809999888","A+ve","28/08/2004","male","indian","Muslim","yes","hand","bc","Hindi"),
  Admissiondetails("B.tech Cyber security","Computer Science","counselling","General"),
  Sslcdetails("Varisu street,mettiyoli nagar,Chrompet,Chennai","2020","board","NA","98"),
  Hscdetails("Varisu street,mettiyoli nagar,Chrompet,Chennai","2022","Tamilnadu board","bio","92","93","90","98"),
  Address("Flat no:4,Manju Apartrment,Anna nagar,Chrompet","Flat no:4,Anna nagar,Chrompet"),
  Fatherdetails("Lokesh khan","lokesh23456@gmail.com","8454665789","15-8-1965","SSLC"," private employer","chief executive officer","123456000"),
  Motherdetails("Shreya Saran","shreyasaran123@gmail.com","7654890995","25-3-1970","HSC","Governmnt officer","Bank manager","123456000"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Sujith Bala v", 2323498765678, "Sujith Bala ","V","sujithbala6786@ssn.edu.in","9876530130","AB-ve","28/01/2004","male","indian","Hindu","no","NA","SC","tamil"),
  Admissiondetails("B.E.Biomediical Engineering ","Biomedical","Counselling","SC/ST category"),
  Sslcdetails("No:7,Bagalur Hudco,Hosur","2020","Tamilnadu board","NA","80"),
  Hscdetails("No:7,Bagalur Hudco,Hosur","2022","board","bio","85","90","85","95"),
  Address("plot no:80,vivekanandar street ,Hosur","plot no:80,vivekanandar street,Hosur"),
  Fatherdetails("Vivek S","vivek987@gmail.com","87678909845","31-01-1970","B.Ed","Government employee","Teacher","1000000"),
  Motherdetails("Sunitha","NA","7890123450","21-02-1973","SSLC","House wife ","NA","NA"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Danesh M", 40089076456, "Danesh","M","danesh2210769@ssn.edu.in","7890789750","B+","11/06/2005","male","Indian","Hindu","No","NA","Bc","Telugu"),
  Admissiondetails("B.tech Information technology","Information Technology","counselling","General"),
  Sslcdetails("NGO's colony,Puttur","2020","AP board","NA","97"),
  Hscdetails("NGO's colony,Puttur","2022","AP board","MPC","96","99","90","100"),
  Address("Sri krishna Colony , Puttur","Sri krishna Colony , Puttur"),
  Fatherdetails("Ramesh","ramesh56+@gmail.com","9087434007","17-06-1970","BE ","private employee","civil engineer","1200000"),
  Motherdetails("vedhavathi","vedha@gmail.com","9959522708","3-01-1973","SSLC","house wife","NA","NA"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Manju Sri S ", 331209324, "Manju Sri ","S","manjusri2210732@ssn.edu.in","9360820940","O+","23/06/2004","Female","indian","Hindu","No","NA","bc","telugu"),
  Admissiondetails("B.tech Information technology","Information Technology","counselling","General"),
  Sslcdetails("phase 2, Bagalur hudco , HOsur","2020","Tamilnadu board","NA","99"),
  Hscdetails("Phase 2 , Bagalur hudco , Hosur","2022","Tamilnadu board","bio","97","97","100","99"),
  Address("Plot no:36 valluvar Nagar , Rayakotta road ,Hosur","Plot no:36 valluvar Nagar , Rayakotta road ,Hosur"),
  Fatherdetails("Suresh S ","Suresh15@gmail.com","9894006470","13-12-1970","BE.Mechanical Engineering ","Mechanical ENgineer","Senior Manager","2000000"),
  Motherdetails("Rag","xcvbnm#+@gmail.com","1234567","5-3-1990","SSLC","Governmnt officer","Bank manager","123456000"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Farthima S", 4567890145, "Farthima","S","Farthmia600112@ssn.edu.in","9894006485","A-ve","01/01/2004","Female","indian","Muslim","no","NA","BC","Hindi"),
  Admissiondetails("B.E Civil Engineering","Civil","Counselling","General"),
  Sslcdetails("No:12,Race course,Coimbatore","2020","board","NA","90"),
  Hscdetails("No:12,Race course,Coimbatore","2022","board","bio","95","98","90","96"),
  Address("No:12,Maharani avenue,Vadavalli,Coimbatore","No:12,Maharani avenue,Vadavalli,Coimbatore"),
  Fatherdetails("Sherif","sherif123@gmail.com","9090765438","25-07-1970","CA","Governmnt officer","Auditor","2550000"),
  Motherdetails("Rafikka","Rafikka045@gmail.com","9891234567","13-07-1975","B.com","Governmnt officer","Bank employee","900000"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)


write_student_profiles_to_csv(students)

def write_student_profiles_to_csv(students):
    # Write each student's profile as a separate CSV file
    for student in students:
        # Define the filename based on student name or any unique identifier
        filename = f"{student.personaldetails.email}_profile.csv"

        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            header = ['Name', 'Aadhar Number', 'First Name', 'Last Name', 'Email', 'Mobile Number', 'Blood Group', 'Date of Birth',
                      'Gender', 'Nationality', 'Religion', 'Differently Abled', 'Type of Disability', 'Community', 'Mother Tongue',
                      'Program Name', 'Associated Department', 'Mode of Admission', 'Admission Category', 'SSLC School Address',
                      'SSLC Year of Passing', 'SSLC Board or University', 'SSLC Group', 'SSLC Percentage',
                      'HSC School Address', 'HSC Year of Passing', 'HSC Board of Study', 'HSC Group', 'HSC Percentage',
                      'HSC Maths', 'HSC Physics', 'HSC Chemistry', 'Current Address', 'Permanent Address',
                      'Father Name', 'Father Email', 'Father Mobile Number', 'Father Date of Birth', 'Father Qualification',
                      'Father Occupation', 'Father Designation', 'Father Annual Income',
                      'Mother Name', 'Mother Email', 'Mother Mobile Number', 'Mother Date of Birth', 'Mother Qualification',
                      'Mother Occupation', 'Mother Designation', 'Mother Annual Income']
            
            writer.writerow(header)

            # Extract the data from the student object
            student_data = [student.personaldetails.name, student.personaldetails.aadharnumber, student.personaldetails.firstname, student.personaldetails.lastname, student.personaldetails.email, student.personaldetails.mobilenumber,
                student.personaldetails.bloodgroup, student.personaldetails.dateofbirth, student.personaldetails.gender, student.personaldetails.nationality, student.personaldetails.religion,
                student.personaldetails.differentlyabled, student.personaldetails.typeofdisability, student.personaldetails.community, student.personaldetails.mothertongue,
                student.admissiondetails.programname, student.admissiondetails.associateddepartment,
                student.admissiondetails.modeofadmission, student.admissiondetails.admissioncategory,
                student.sslcdetails.schooladdress, student.sslcdetails.yearofpassing, student.sslcdetails.boardoruniversity,
                student.sslcdetails.group, student.sslcdetails.percentage,
                student.hscdetails.schooladdress, student.hscdetails.yearofpassing, student.hscdetails.boardofstudy,
                student.hscdetails.group, student.hscdetails.percentage, student.hscdetails.maths, student.hscdetails.physics,
                student.hscdetails.chemistry, student.address.currentaddress, student.address.permanentaddress,
                student.fatherdetails.name, student.fatherdetails.email, student.fatherdetails.mobilenumber, student.fatherdetails.dateofbirth,
                student.fatherdetails.qualification, student.fatherdetails.occupation, student.fatherdetails.designation, student.fatherdetails.annualincome,
                student.motherdetails.name, student.motherdetails.email, student.motherdetails.mobilenumber, student.motherdetails.dateofbirth,
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation]

            

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Vithula S", 333456712309, "Vithula","S","vithula316@ssn.edu.in","7989400642","B-ve","31/03/2003","Female","indian","Hindu","No","NA","Bc","Tamil"),
  Admissiondetails("B.tech Information technology","Information Technology","Management","General"),
  Sslcdetails("89,Phase1,chrompet ,Chennai","2020","CBSE","NA","98"),
  Hscdetails("89,Phase1,chrompet ,Chennai","2022","board","bio","97","97","90","99"),
  Address("no:09,lotus apartment,Sholinganallur,Chennai","no:09,lotus apartment,Sholinganallur,Chennai"),
  Fatherdetails("Srinivasan ","shri00@gmail.com","986545342","17-06-1975","BE.Computer Science","Software Engineer","Executive","2000000"),
  Motherdetails("Dhana","dhana03@gmail.com","9897650987","18-11-1980","B.com","House wife","NA","NA"))]



# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)
