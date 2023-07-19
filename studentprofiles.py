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

for i in range(1,21):
# Add student profiles to the array
 if i==1:
  student=per_Student("John Doe K","232345678567","John Doe","K","johndoe2210456@ssn.edu.in","7890765432","B+","23-08-2004","Male","Indian","Christian","Yes","Physical","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Management","General")
  sslc=Sslcdetails("Leo Schools,COIMBATORE","2020","Tamilnadu board","NA","98")
  hsc=Hscdetails("Leo Schools,COIMBATORE","2022","Tamilnadu board","Biology","97","97","90","99")
  address=Address("No.4A,Bommalattam street,Coimbatore","No.4A,Bommalattam street,Coimbatore")
  father=Fatherdetails("Krish","krish@gmail.com","9087340912","15-03-1970","B.Com","Government Officer","Clerk","500000")
  mother=Motherdetails("Ragavi","ragavi@gmail.com","7373987632","05-09-1980","SSLC","Government Officer","Postmaster","650000")

  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

  # Add student profiles to the array
 if i==2:
  student=per_Student("Santhosh Kumar M","232345678890","Santhosh Kumar","M","santhosh2210410@ssn.edu.in","7763087618","O+","23-07-2004","Male","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.E.Computer Science","Computer Science","Counselling","7.5 reservation")
  sslc=Sslcdetails("Kamarajar School,Erode","2020","Tamilnadu board","NA","80")
  hsc=Hscdetails("Kamarajar School,Erode","2022","Tamilnadu board","Computer Science","85","80","70","90")
  address=Address("Street No. 14, Gandhi street Erode","Street No. 14, Gandhi street Erode")
  father=Fatherdetails("Madhvan","madhvan2390@gmail.com","7436091096","15-03-1975","HSC","Government Officer","clerk","500000")
  mother=Motherdetails("Radha","radha567@gmail.com","98714307634","14-03-1979","SSLC","House wife","NA","NA")

  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==3:
  student=per_Student("Deepak Chahar","333456712073","Deepak","Chahar","deepakchahar2210736@ssn.edu.in","9845673043","AB-","23-12-2004","Male","Indian","Hindu","NO","NA","General","Telugu")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Monk Schools, Krishnagiri","2020","Telangana board","NA","98")
  hsc=Hscdetails("Monk Schools, Krishnagiri","2022","Telangana board","Biology","95","97","90","95")
  address=Address("No.234, Priest street Krishnagiri ","No.234, Priest street Krishnagiri ")
  father=Fatherdetails("Murali","muralimurali@gmail.com","723456098","30-06-1970","BE","Mechanical Engineer","Manager","1500000")
  mother=Motherdetails("sumathi","sumathinm@gmail.com","989458582","08-04-1972","M.A.B.Ed","Government Officer","Teacher","1200000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==4:
  student=per_Student("Monica P","232345678234","Monica ","P","monica2210090@ssn.edu.in","9897645321","A+","03-10-2004","Female","Indian","Hindu","No","NA","SC","Tamil")
  admission=Admissiondetails("B.E.Mechanical Engineering","Mechanical","Management","General")
  sslc=Sslcdetails("SBOA School, Salem","2020","Tamilnadu board","NA","98")
  hsc=Hscdetails("SBOA School, Salem","2022","Tamilnadu board","Biology","97","97","90","99")
  address=Address("FLAT NO :87, Saradha apartment,Salem","FLAT NO :87, Saradha apartment,Salem")
  father=Fatherdetails("Prabhakaran","prabha@gmail.com","9090987654","16-08-1970","B.Com","Government officer","Bank manager","1000000")
  mother=Motherdetails("Reema","Reema5@gmail.com","9234567890","25-08-1985","B.E.Chemical Engineering ","Chief Chemical Engineer","Team manager","1256000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)     

 if i==5:
  student=per_Student("Sharukh Khan L","23234567878","Sharukh Khan","L","sharukhkhan2210345@ssn.edu.in","7809999888","A+","28-08-2004","Male","Indian","Muslim","Yes","Physical","BC","Hindi")
  admission=Admissiondetails("B.Tech Cyber security","Computer Science","Counselling","General")
  sslc=Sslcdetails("DAV School Chennai","2020","Tamilnadu board","NA","98")
  hsc=Hscdetails("DAV School Chennai","2022","Tamilnadu board","Biology","92","93","90","98")
  address=Address("Flat no:4, Manju Apartment, Anna nagar, Chrompet","Flat no:4, Manju Apartment, Anna nagar, Chrompet")
  father=Fatherdetails("Lokesh Khan","lokesh23456@gmail.com","8454665789","15-08-1975","SSLC"," Private Employer","Chief Executive Officer","1234000")
  mother=Motherdetails("Shreya Saran","shreyasaran123@gmail.com","7654890995","25-03-1979","HSC","Government Officer","Bank manager","1256000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==6:
  student=per_Student("Sujith Bala V","2323498765678","Sujith Bala","V","sujithbala2210786@ssn.edu.in","9876530130","AB-","28-01-2004","Male","Indian","Hindu","No","NA","ST","Tamil")
  admission=Admissiondetails("B.E.Biomedical Engineering","Biomedical","Counselling","SC/ST category")
  sslc=Sslcdetails("Bagalur School, Hosur","2020","Tamilnadu board","NA","80")
  hsc=Hscdetails("Bagalur School, Hosur","2022","Tamilnadu board","Biology","85","90","85","95")
  address=Address("Plot No:80, Vivekanandar street, Hosur","Plot No:80, Vivekanandar street, Hosur")
  father=Fatherdetails("Vivek S","vivek987@gmail.com","8767890845","31-01-1970","B.Ed","Government Officer","Teacher","100000")
  mother=Motherdetails("Sunitha","suni2102@gmail.com","7890123450","21-02-1973","SSLC","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==7:
  student=per_Student("Danesh R","40089076456","Danesh","R","danesh2210769@ssn.edu.in","7890789750","B+","11-06-2005","Male","Indian","Hindu","No","NA","BC","Telugu")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Velammal School, Chennai","2020","CBSE","NA","97")
  hsc=Hscdetails("Velammal School, Chennai","2022","CBSE","Computere Science","96","99","90","100")
  address=Address("Sri Krishna Colony, Chennai","Sri Krishna Colony, Chennai")
  father=Fatherdetails("Ramesh","ramesh56@gmail.com","9087434007","17-06-1970","BE ","Private Employee","Civil Engineer","1200000")
  mother=Motherdetails("Vedhavathi","vedha@gmail.com","9959522708","03-01-1973","SSLC","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==8:
  student=per_Student("Manju Sri S","331209324356","Manju Sri","S","manjusri2210732@ssn.edu.in","9360820940","O+","23-06-2004","Female","Indian","Hindu","No","NA","BC","Telugu")
  admission=Admissiondetails("B.tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Bagalur School, Hosur","2020","Tamilnadu board","NA","99")
  hsc=Hscdetails("Bagalur School, Hosur","2022","Tamilnadu board","Biology","97","97","100","99")
  address=Address("Plot no:36 Valluvar Nagar, Rayakotta road, Hosur","Plot no:36 Valluvar Nagar, Rayakotta road, Hosur")
  father=Fatherdetails("Suresh S","Suresh15@gmail.com","9894006470","13-12-1970","BE.Mechanical Engineering ","Mechanical Engineer","Senior Manager","2000000")
  mother=Motherdetails("Ragavi","ragavi@gmail.com","9867898487","05-03-1975","MBA","Government Officer","Bank Manager","1230000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==9:
  student=per_Student("Farthima S","4567890145","Farthima","S","farthima2210007@ssn.edu.in","9894006485","A-","01-01-2004","Female","Indian","Muslim","No","NA","BC","Hindi")
  admission=Admissiondetails("B.E Civil Engineering","Civil","Counselling","General")
  sslc=Sslcdetails("Race School, Coimbatore","2020","CBSE","NA","90")
  hsc=Hscdetails("Race School, Coimbatore","2022","CBSE","Biology","95","98","90","96")
  address=Address("No:12, Maharani Avenue, Vadavalli, Coimbatore","No:12, Maharani avenue, Vadavalli, Coimbatore")
  father=Fatherdetails("Sherif","sherif123@gmail.com","9090765438","25-07-1970","CA","Government officer","Auditor","2550000")
  mother=Motherdetails("Rafikka","Rafikka045@gmail.com","9891234567","13-07-1975","B.com","Government officer","Bank employee","900000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

 if i==10:
  student=per_Student("Vithula S","333456712309","Vithula","S","vithula2210321@ssn.edu.in","7989400642","B-","31/03/2003","Female","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Management","General")
  sslc=Sslcdetails("Maharishi Vidhya Mandir, Chennai","2020","CBSE","NA","98")
  hsc=Hscdetails("Maharishi Vidhya Mandir, Chennai","2022","CBSE","Biology","97","97","90","99")
  address=Address("No:09, Lotus apartment, Sholinganallur, Chennai","No:09, Lotus apartment, Sholinganallur, Chennai")
  father=Fatherdetails("Srinivasan","shri01@gmail.com","9865453472","17-06-1975","BE.Computer Science","Software Engineer","Executive","2000000")
  mother=Motherdetails("Dhana","dhana03@gmail.com","9897650987","18-11-1980","B.com","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==11:
  student=per_Student("Maheswari H","659731542003","Maheswari","H","maheswari2210111@ssn.edu.in","9431056725","B+","31/12/2004","Female","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Maharishi Vidhya Mandir, Chennai","2020","CBSE","NA","97")
  hsc=Hscdetails("Maharishi Vidhya Mandir, Chennai","2022","CBSE","Computer Science","96","99","98","97")
  address=Address("No:19, Vindhya apartment, Egmore, Chennai","No:19, Vindhya apartment, Egmore, Chennai")
  father=Fatherdetails("Hariharan","hari896@gmail.com","8593754100","27-07-1973","BE.Computer Science","Software Engineer","Executive","2200000")
  mother=Motherdetails("Gopika","gopika75@gmail.com","8310246988","08-11-1975","CA","Government Officer","Auditor","1900000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==12:
  student=per_Student("Manoj R D","956321014785","Manoj","R D","manoj2210100@ssn.edu.in","8869326650","A+","15/07/2004","Male","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Everwin Vidhyashram, Chennai","2020","CBSE","NA","95")
  hsc=Hscdetails("Everwin Vidhyashram, Chennai","2022","CBSE","Biology","98","99","99","99")
  address=Address("No:63, Modern Valley apartment, Kilpauk, Chennai","No:63, Modern Valley apartment, Kilpauk, Chennai")
  father=Fatherdetails("Dhanush","dhanush125@gmail.com","8953220163","05-03-1974","B.Arch","Architect","Architect","2500000")
  mother=Motherdetails("Kala","kala76@gmail.com","9652147555","18-11-1976","B.com","Government Employee","Clerk","1000000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==13:
  student=per_Student("Kalaivani S","869532010014","Kalaivani","S","kalaivani2210051@ssn.edu.in","9862001455","O+","17/08/2004","Female","Indian","Hindu","No","NA","MBC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("DAV School, Chennai","2020","CBSE","NA","96")
  hsc=Hscdetails("DAV School ,Chennai","2022","CBSE","Computer Science","98","99","100","99")
  address=Address("No:99, Bougainvillea apartment, Kolathur, Chennai","No:99, Bougainvillea apartment, Kolathur, Chennai")
  father=Fatherdetails("Santhosh","santhosh159@gmail.com","8864021302","18-12-1973","MBA","Private Employee","Sales Director","1900000")
  mother=Motherdetails("Lavanya","lavanya02@gmail.com","9684253102","19-03-1975","BE Electrical and Electronics Engineering","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==14:
  student=per_Student("Prajith D","930015248963","Prajith","D","prajith2210687@ssn.edu.in","9513760024","B-","09/09/2004","Male","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Management","General")
  sslc=Sslcdetails("DAV Boys Sr. Sec School, Chennai","2020","CBSE","NA","93")
  hsc=Hscdetails("DAV Boys Sr. Sec School, Chennai","2022","CBSE","Biology","94","95","97","98")
  address=Address("No:79, Paradise apartment, Kolathur, Chennai","No:79, Paradise apartment, Kolathur, Chennai")
  father=Fatherdetails("Dharun","dharun45@gmail.com","9642001358","19-10-1971","BE.Computer Science","Software Engineer","Executive","1800000")
  mother=Motherdetails("Ramya","ramya56@gmail.com","9641032568","18-06-1973","B.com","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)
 
if i==15:
  student=per_Student("Prakshi M","973350168200","Prakshi","M","prakshi2210503@ssn.edu.in","8562036894","B+","29/08/2004","Female","Indian","Hindu","No","NA","MBC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Mahalakshmi Vidhyalaya, Chennai","2020","CBSE","NA","96")
  hsc=Hscdetails("Mahalakshmi Vidhyalaya, Chennai","2022","CBSE","Computer Science","99","100","100","100")
  address=Address("76/89, Bajrang apartment, Pallikaranai, Chennai","76/89, Bajrang apartment, Pallikaranai, Chennai")
  father=Fatherdetails("Madhavan","madhavan12@gmail.com","9658238641","09-04-1974","LLB Hons","Government Employee","Corporate Counsellor","2800000")
  mother=Motherdetails("Rukmini","rukmini86@gmail.com","8695332001","11-06-1976","MA English Literature","Mass Communication","Senior Journalist","3045000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==16:
  student=per_Student("Clara J","668521475699","Clara","J","clara2210295@ssn.edu.in","8853015247","B+","24/05/2004","Female","Indian","Christian","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("CSI Bains School, Chennai","2020","State Board","NA","94")
  hsc=Hscdetails("CSI Bains School, Chennai","2022","State Board","Computer Science","96","99","95","97")
  address=Address("No:47, Rainbow Colony, Annanagar, Chennai","No:47, Rainbow Colony, Annanagar, Chennai")
  father=Fatherdetails("Jen Joseph","jen56@gmail.com","9541203665","14-04-1970","BE","Government Employee","Postal Assisstant","1200000")
  mother=Motherdetails("Alia","alia50@gmail.com","8533029965","19-10-1972","BE","Government Employee","Clerk","900000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==17:
  student=per_Student("Ram Prasad G","956820014753","Ram Prasad","G","ramprasad2210324@ssn.edu.in","9123459687","AB-","05/07/2004","Male","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("SBOA Matric, Chennai","2020","State Board","NA","97")
  hsc=Hscdetails("SBOA Matric, Chennai","2022","State Board","Computer Science","98","98","98","98")
  address=Address("No:49, Hillway Colony, Sholinganallur, Chennai","No:49, Hillway Colony, Sholinganallur, Chennai")
  father=Fatherdetails("Guganeshwar","gugan45@gmail.com","9563002001","15-12-1975","MBA","Private Business","Businessman","2500000")
  mother=Motherdetails("Ragini","ragini73@gmail.com","9632001450","14-06-1977","BE","House wife","NA","NA")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==18:
  student=per_Student("Farina M","962201453302","Farina","M","farina2210868@ssn.edu.in","7698552014","O-","17/07/2004","Female","Indian","Muslim","No","NA","BCM","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Management","General")
  sslc=Sslcdetails("Chennai Public School, Chennai","2020","CBSE","NA","95")
  hsc=Hscdetails("Chennai Public School, Chennai","2022","CBSE","Biology","96","96","97","96")
  address=Address("45/82, Willows apartment, Saidapet, Chennai","45/82, Willows apartment, Saidapet, Chennai")
  father=Fatherdetails("Mohammed Kharif","mohammedkharif45@gmail.com","9630021001","07-09-1972","MBA","Businessman","Private Business","2000000")
  mother=Motherdetails("Fathima","fathima63@gmail.com","8862015411","17-02-1974","M.E","Public Sector","Bank Manager","1500000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==19:
  student=per_Student("Jenifer J","964100257896","Jenifer","J","jenifer2210252@ssn.edu.in","9512425889","AB+","20/08/2004","Female","Indian","Christian","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("St. Mary's School, Chennai","2020","State Board","NA","97")
  hsc=Hscdetails("St. Mary's School, Chennai","2022","State Board","Computer Science","98","99","97","98")
  address=Address("No:10, Jaguar apartment, Mambalam, Chennai","No:10, Jaguar apartment, Mambalam, Chennai")
  father=Fatherdetails("John Samuel","johnsamuel44@gmail.com","8852013002","11-12-1971","M.com","Public Sector","Bank Manager","1700000")
  mother=Motherdetails("Christina","christina447@gmail.com","8625477411","28-01-1973","CA","Private Employee","Auditor","1500000")

  
  temp = StudentDetails(student, admission, sslc, hsc, address, father, mother)
   

  students.append(temp)

if i==20:
  student=per_Student("Tanushree V","456320021478","Tanushree","V","tanushree2210549@ssn.edu.in","8856200132","O+","21/05/2004","Female","Indian","Hindu","No","NA","BC","Tamil")
  admission=Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General")
  sslc=Sslcdetails("Alagappa School, Chennai","2020","State Board","NA","95")
  hsc=Hscdetails("Alagappa School, Chennai","2022","State Board","Computer Science","98","99","97","99")
  address=Address("No:20, Magnum apartment, Choolai, Chennai","No:20, Magnum apartment, Choolai, Chennai")
  father=Fatherdetails("Venkataraman","venkat78@gmail.com","9655474410","14-04-1974","MCA","Database Engineer","Executive","1100000")
  mother=Motherdetails("Padma","padma56@gmail.com","9877441024","17-12-1976","ME","Electrical Engineer","Manager","1300000")

  
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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]
    # Add student objects

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("John Doe K","232345678567","John Doe","K","johndoe2210456@ssn.edu.in","7890765432","B+","23-08-2004","Male","Indian","Christian","Yes","Physical","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Management","General"),
Sslcdetails("Leo Schools,COIMBATORE","2020","Tamilnadu board","NA","98"),
Hscdetails("Leo Schools,COIMBATORE","2022","Tamilnadu board","Biology","97","97","90","99"),
Address("No.4A,Bommalattam street,Coimbatore","No.4A,Bommalattam street,Coimbatore"),
Fatherdetails("Krish","krish@gmail.com","9087340912","15-03-1970","B.Com","Government Officer","Clerk","500000"),
Motherdetails("Ragavi","ragavi@gmail.com","7373987632","05-09-1980","SSLC","Government Officer","Postmaster","650000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Santhosh Kumar M","232345678890","Santhosh Kumar","M","santhosh2210410@ssn.edu.in","7763087618","O+","23-07-2004","Male","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.E.Computer Science","Computer Science","Counselling","7.5 reservation"),
Sslcdetails("Kamarajar School,Erode","2020","Tamilnadu board","NA","80"),
Hscdetails("Kamarajar School,Erode","2022","Tamilnadu board","Computer Science","85","80","70","90"),
Address("Street No. 14, Gandhi street Erode","Street No. 14, Gandhi street Erode"),
Fatherdetails("Madhvan","madhvan2390@gmail.com","7436091096","15-03-1975","HSC","Government Officer","clerk","500000"),
Motherdetails("Radha","radha567@gmail.com","98714307634","14-03-1979","SSLC","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Deepak Chahar","333456712073","Deepak","Chahar","deepakchahar2210736@ssn.edu.in","9845673043","AB-","23-12-2004","Male","Indian","Hindu","NO","NA","General","Telugu"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Monk Schools, Krishnagiri","2020","Telangana board","NA","98"),
Hscdetails("Monk Schools, Krishnagiri","2022","Telangana board","Biology","95","97","90","95"),
Address("No.234, Priest street Krishnagiri ","No.234, Priest street Krishnagiri "),
Fatherdetails("Murali","muralimurali@gmail.com","723456098","30-06-1970","BE","Mechanical Engineer","Manager","1500000"),
Motherdetails("sumathi","sumathinm@gmail.com","989458582","08-04-1972","M.A.B.Ed","Government Officer","Teacher","1200000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Monica P","232345678234","Monica ","P","monica2210090@ssn.edu.in","9897645321","A+","03-10-2004","Female","Indian","Hindu","No","NA","SC","Tamil"),
Admissiondetails("B.E.Mechanical Engineering","Mechanical","Management","General"),
Sslcdetails("SBOA School, Salem","2020","Tamilnadu board","NA","98"),
Hscdetails("SBOA School, Salem","2022","Tamilnadu board","Biology","97","97","90","99"),
Address("FLAT NO :87, Saradha apartment,Salem","FLAT NO :87, Saradha apartment,Salem"),
Fatherdetails("Prabhakaran","prabha@gmail.com","9090987654","16-08-1970","B.Com","Government officer","Bank manager","1000000"),
Motherdetails("Reema","Reema5@gmail.com","9234567890","25-08-1985","B.E.Chemical Engineering ","Chief Chemical Engineer","Team manager","1256000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Sharukh Khan J","23234567878","Sharukh Khan","J","sharukhkhan2210345@ssn.edu.in","7809999888","A+","28-08-2004","Male","Indian","Muslim","Yes","Physical","BC","Hindi"),
Admissiondetails("B.Tech Cyber security","Computer Science","Counselling","General"),
Sslcdetails("DAV School Chennai","2020","Tamilnadu board","NA","98"),
Hscdetails("DAV School Chennai","2022","Tamilnadu board","Biology","92","93","90","98"),
Address("Flat no:4, Manju Apartment, Anna nagar, Chrompet","Flat no:4, Manju Apartment, Anna nagar, Chrompet"),
Fatherdetails("Lokesh Khan","lokesh23456@gmail.com","8454665789","15-08-1975","SSLC"," Private Employer","Chief Executive Officer","1234000"),
Motherdetails("Shreya Saran","shreyasaran123@gmail.com","7654890995","25-03-1979","HSC","Government Officer","Bank manager","1256000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]   

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Sujith Bala V","2323498765678","Sujith Bala","V","sujithbala2210786@ssn.edu.in","9876530130","AB-","28-01-2004","Male","Indian","Hindu","No","NA","ST","Tamil"),
Admissiondetails("B.E.Biomedical Engineering","Biomedical","Counselling","SC/ST category"),
Sslcdetails("Bagalur School, Hosur","2020","Tamilnadu board","NA","80"),
Hscdetails("Bagalur School, Hosur","2022","Tamilnadu board","Biology","85","90","85","95"),
Address("Plot No:80, Vivekanandar street, Hosur","Plot No:80, Vivekanandar street, Hosur"),
Fatherdetails("Vivek S","vivek987@gmail.com","8767890845","31-01-1970","B.Ed","Government Officer","Teacher","100000"),
Motherdetails("Sunitha","suni2102@gmail.com","7890123450","21-02-1973","SSLC","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]       

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Danesh R","40089076456","Danesh","R","danesh2210769@ssn.edu.in","7890789750","B+","11-06-2005","Male","Indian","Hindu","No","NA","BC","Telugu"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Velammal School, Chennai","2020","CBSE","NA","97"),
Hscdetails("Velammal School, Chennai","2022","CBSE","Computere Science","96","99","90","100"),
Address("Sri Krishna Colony, Chennai","Sri Krishna Colony, Chennai"),
Fatherdetails("Ramesh","ramesh56@gmail.com","9087434007","17-06-1970","BE ","Private Employee","Civil Engineer","1200000"),
Motherdetails("Vedhavathi","vedha@gmail.com","9959522708","03-01-1973","SSLC","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Manju Sri S","331209324356","Manju Sri","S","manjusri2210732@ssn.edu.in","9360820940","O+","23-06-2004","Female","Indian","Hindu","No","NA","BC","Telugu"),
Admissiondetails("B.tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Bagalur School, Hosur","2020","Tamilnadu board","NA","99"),
Hscdetails("Bagalur School, Hosur","2022","Tamilnadu board","bio","97","97","100","99"),
Address("Plot no:36 Valluvar Nagar, Rayakotta road, Hosur","Plot no:36 Valluvar Nagar, Rayakotta road, Hosur"),
Fatherdetails("Suresh S","Suresh15@gmail.com","9894006470","13-12-1970","BE.Mechanical Engineering ","Mechanical Engineering","Senior Manager","2000000"),
Motherdetails("Ragavi","ragavi@gmail.com","9867898487","05-03-1975","MBA","Government Officer","Bank Manager","1230000"))]


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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome]

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Farthima S","4567890145","Farthima","S","farthima2210007@ssn.edu.in","9894006485","A-","01-01-2004","Female","Indian","Muslim","No","NA","BC","Hindi"),
Admissiondetails("B.E Civil Engineering","Civil","Counselling","General"),
Sslcdetails("Race School, Coimbatore","2020","CBSE","NA","90"),
Hscdetails("Race School, Coimbatore","2022","CBSE","Biology","95","98","90","96"),
Address("No:12, Maharani Avenue, Vadavalli, Coimbatore","No:12, Maharani avenue, Vadavalli, Coimbatore"),
Fatherdetails("Sherif","sherif123@gmail.com","9090765438","25-07-1970","CA","Government officer","Auditor","2550000"),
Motherdetails("Rafikka","Rafikka045@gmail.com","9891234567","13-07-1975","B.com","Government officer","Bank employee","900000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Vithula S","333456712309","Vithula","S","vithula2210321@ssn.edu.in","7989400642","B-","31/03/2003","Female","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Management","General"),
Sslcdetails("MVM School, Chennai","2020","CBSE","NA","98"),
Hscdetails("MVM School ,Chennai","2022","CBSE","Biology","97","97","90","99"),
Address("No:09, Lotus apartment, Sholinganallur, Chennai","No:09, Lotus apartment, Sholinganallur, Chennai"),
Fatherdetails("Srinivasan","shri01@gmail.com","9865453472","17-06-1975","BE.Computer Science","Software Engineer","Executive","2000000"),
Motherdetails("Dhana","dhana03@gmail.com","9897650987","18-11-1980","B.com","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Maheswari H","659731542003","Maheswari","H","maheswari2210111@ssn.edu.in","9431056725","B+","31/12/2004","Female","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Maharishi Vidhya Mandir, Chennai","2020","CBSE","NA","97"),
Hscdetails("Maharishi Vidhya Mandir, Chennai","2022","CBSE","Computer Science","96","99","98","97"),
Address("No:19, Vindhya apartment, Egmore, Chennai","No:19, Vindhya apartment, Egmore, Chennai"),
Fatherdetails("Hariharan","hari896@gmail.com","8593754100","27-07-1973","BE.Computer Science","Software Engineer","Executive","2200000"),
Motherdetails("Gopika","gopika75@gmail.com","8310246988","08-11-1975","CA","Government Officer","Auditor","1900000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Manoj R D","956321014785","Manoj","R D","manoj2210100@ssn.edu.in","8869326650","A+","15/07/2004","Male","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Everwin Vidhyashram, Chennai","2020","CBSE","NA","95"),
Hscdetails("Everwin Vidhyashram, Chennai","2022","CBSE","Biology","98","99","99","99"),
Address("No:63, Modern Valley apartment, Kilpauk, Chennai","No:63, Modern Valley apartment, Kilpauk, Chennai"),
Fatherdetails("Dhanush","dhanush125@gmail.com","8953220163","05-03-1974","B.Arch","Architect","Architect","2500000"),
Motherdetails("Kala","kala76@gmail.com","9652147555","18-11-1976","B.com","Government Employee","Clerk","1000000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Kalaivani S","869532010014","Kalaivani","S","kalaivani2210051@ssn.edu.in","9862001455","O+","17/08/2004","Female","Indian","Hindu","No","NA","MBC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("DAV School, Chennai","2020","CBSE","NA","96"),
Hscdetails("DAV School ,Chennai","2022","CBSE","Computer Science","98","99","100","99"),
Address("No:99, Bougainvillea apartment, Kolathur, Chennai","No:99, Bougainvillea apartment, Kolathur, Chennai"),
Fatherdetails("Santhosh","santhosh159@gmail.com","8864021302","18-12-1973","MBA","Private Employee","Sales Director","1900000"),
Motherdetails("Lavanya","lavanya02@gmail.com","9684253102","19-03-1975","BE Electrical and Electronics Engineering","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Prajith D","930015248963","Prajith","D","prajith2210687@ssn.edu.in","9513760024","B-","09/09/2004","Male","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Management","General"),
Sslcdetails("DAV Boys Sr. Sec School, Chennai","2020","CBSE","NA","93"),
Hscdetails("DAV Boys Sr. Sec School, Chennai","2022","CBSE","Biology","94","95","97","98"),
Address("No:79, Paradise apartment, Kolathur, Chennai","No:79, Paradise apartment, Kolathur, Chennai"),
Fatherdetails("Dharun","dharun45@gmail.com","9642001358","19-10-1971","BE.Computer Science","Software Engineer","Executive","1800000"),
Motherdetails("Ramya","ramya56@gmail.com","9641032568","18-06-1973","B.com","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Prakshi M","973350168200","Prakshi","M","prakshi2210503@ssn.edu.in","8562036894","B+","29/08/2004","Female","Indian","Hindu","No","NA","MBC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Mahalakshmi Vidhyalaya, Chennai","2020","CBSE","NA","96"),
Hscdetails("Mahalakshmi Vidhyalaya, Chennai","2022","CBSE","Computer Science","99","100","100","100"),
Address("76/89, Bajrang apartment, Pallikaranai, Chennai","76/89, Bajrang apartment, Pallikaranai, Chennai"),
Fatherdetails("Madhavan","madhavan12@gmail.com","9658238641","09-04-1974","LLB Hons","Government Employee","Corporate Counsellor","2800000"),
Motherdetails("Rukmini","rukmini86@gmail.com","8695332001","11-06-1976","MA English Literature","Mass Communication","Senior Journalist","3045000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Clara J","668521475699","Clara","J","clara2210295@ssn.edu.in","8853015247","B+","24/05/2004","Female","Indian","Christian","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("CSI Bains School, Chennai","2020","State Board","NA","94"),
Hscdetails("CSI Bains School, Chennai","2022","State Board","Computer Science","96","99","95","97"),
Address("No:47, Rainbow Colony, Annanagar, Chennai","No:47, Rainbow Colony, Annanagar, Chennai"),
Fatherdetails("Jen Joseph","jen56@gmail.com","9541203665","14-04-1970","BE","Government Employee","Postal Assisstant","1200000"),
Motherdetails("Alia","alia50@gmail.com","8533029965","19-10-1972","BE","Government Employee","Clerk","900000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Ram Prasad G","956820014753","Ram Prasad","G","ramprasad2210324@ssn.edu.in","9123459687","AB-","05/07/2004","Male","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("SBOA Matric, Chennai","2020","State Board","NA","97"),
Hscdetails("SBOA Matric, Chennai","2022","State Board","Computer Science","98","98","98","98"),
Address("No:49, Hillway Colony, Sholinganallur, Chennai","No:49, Hillway Colony, Sholinganallur, Chennai"),
Fatherdetails("Guganeshwar","gugan45@gmail.com","9563002001","15-12-1975","MBA","Private Business","Businessman","2500000"),
Motherdetails("Ragini","ragini73@gmail.com","9632001450","14-06-1977","BE","House wife","NA","NA"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Farina M","962201453302","Farina","M","farina2210868@ssn.edu.in","7698552014","O-","17/07/2004","Female","Indian","Muslim","No","NA","BCM","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Management","General"),
Sslcdetails("Chennai Public School, Chennai","2020","CBSE","NA","95"),
Hscdetails("Chennai Public School, Chennai","2022","CBSE","Biology","96","96","97","96"),
Address("45/82, Willows apartment, Saidapet, Chennai","45/82, Willows apartment, Saidapet, Chennai"),
Fatherdetails("Mohammed Kharif","mohammedkharif45@gmail.com","9630021001","07-09-1972","MBA","Businessman","Private Business","2000000"),
Motherdetails("Fathima","fathima63@gmail.com","8862015411","17-02-1974","M.E","Public Sector","Bank Manager","1500000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Jenifer J","964100257896","Jenifer","J","jenifer2210252@ssn.edu.in","9512425889","AB+","20/08/2004","Female","Indian","Christian","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("St. Mary's School, Chennai","2020","State Board","NA","97"),
Hscdetails("St. Mary's School, Chennai","2022","State Board","Computer Science","98","99","97","98"),
Address("No:10, Jaguar apartment, Mambalam, Chennai","No:10, Jaguar apartment, Mambalam, Chennai"),
Fatherdetails("John Samuel","johnsamuel44@gmail.com","8852013002","11-12-1971","M.com","Public Sector","Bank Manager","1700000"),
Motherdetails("Christina","christina447@gmail.com","8625477411","28-01-1973","CA","Private Employee","Auditor","1500000"))]

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
                student.motherdetails.qualification, student.motherdetails.occupation, student.motherdetails.designation, student.motherdetails.annualincome] 

            # Write the student data as a row in the CSV file
            writer.writerow(student_data)
        
        file.close()

# Create an array of student objects
students = [StudentDetails(per_Student("Tanushree V","456320021478","Tanushree","V","tanushree2210549@ssn.edu.in","8856200132","O+","21/05/2004","Female","Indian","Hindu","No","NA","BC","Tamil"),
Admissiondetails("B.Tech Information Technology","Information Technology","Counselling","General"),
Sslcdetails("Alagappa School, Chennai","2020","State Board","NA","95"),
Hscdetails("Alagappa School, Chennai","2022","State Board","Computer Science","98","99","97","99"),
Address("No:20, Magnum apartment, Choolai, Chennai","No:20, Magnum apartment, Choolai, Chennai"),
Fatherdetails("Venkataraman","venkat78@gmail.com","9655474410","14-04-1974","MCA","Database Engineer","Executive","1100000"),
Motherdetails("Padma","padma56@gmail.com","9877441024","17-12-1976","ME","Electrical Engineer","Manager","1300000"))]

# Call the function to write student profiles to individual CSV files
write_student_profiles_to_csv(students)