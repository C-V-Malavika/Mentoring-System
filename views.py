from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
import csv


def login(request):

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        with open("SDPMS_App/csv/Login.csv") as f:
            csvreader=csv.reader(f)
            for row in csvreader:
                if row[0]=="student" and row[1]==username and row[2]==password:
                    request.session["USER"] = username
                    request.session["PASS"] = password
                    return render(request,"Student Dashboard.html")
                elif row[0]=="mentor" and row[1]==username and row[2]==password:
                    request.session["USER"] = username
                    request.session["PASS"] = password
                    return render(request,"Mentor Dashboard.html")
            else:
                return render(request,"Invalid Login.html")
            
    return render(request,"Login.html")


def forgotpassword(request): 

    if request.method == "GET":

        return render(request,"Forgot Password.html")


def editableforgotpassword(request): 

    from mail import Sending_Mail
    import random

    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[1]==request.POST["email"]:

                    otp_generated=random.randint(10001,99999)  

                    request.session["OTP"] = str(otp_generated)
                    request.session["email"] = request.POST["email"] 
 
                    message="You requested to change password"+"\n"+"Here is the otp"+"\n"+f"{otp_generated}"

                    Sending_Mail(request.POST["email"],message)

                    return render(request,"OTP.html")
                
        return render(request,"Forgot Password.html")
                

def otppage(request):

    if request.method == "POST":

        if request.POST["otp"]==request.session["OTP"]:

            return render(request,"Change Password.html")
        
        return render(request,"OTP.html")


def changepassword(request):
    
    if request.method == "POST":
            
        data=[] 
        newpw=request.POST["newpw"]
        confirmpw=request.POST["confirmpw"]

        if newpw==confirmpw:
                
            with open("SDPMS_App/csv/Login.csv") as f:
                reader=csv.reader(f)
                for row in reader:
                    data.append(row)   

            with open("SDPMS_App/csv/Login.csv","w",newline='') as f:
                writer=csv.writer(f)
                for row in data:
                    if row[1]==request.session["email"]:
                        row[2]=confirmpw
                writer.writerows(data)

            return render(request,"Login.html")
        
        return render(request,"Change Password.html")
                

def dashboard(request):

    if request.method == "POST":

        return render(request,"Dashboard.html")


def studentprofile(request):
    
    class Data:

        def __init__(self,name,aadharnumber,firstname,lastname,email,mobilenumber,bloodgroup,dateofbirth,\
            gender,nationality,religion,differentlyabled,typeofdisability,community,mothertongue,\
            programname,associateddepartment,modeofadmission,admissioncategory,\
            sslcschooladdress,sslcyearofpassing,sslcboardoruniversity,sslcgroup,sslcpercentage,\
            hscschooladdress,hscyearofpassing,hscboardofstudy,hscgroup,hscpercentage,hscmaths,\
            hscphysics,hscchemistry,\
            currentaddress,permanentaddress,\
            fathername,fatheremail,fathermobilenumber,fatherdateofbirth,fatherqualification,fatheroccupation,\
            fatherdesignation,fatherannualincome,\
            mothername,motheremail,mothermobilenumber,motherdateofbirth,motherqualification,motheroccupation,\
            motherdesignation,motherannualincome):
            
            self.name=name
            self.aadharnumber=aadharnumber
            self.firstname=firstname
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
            self.programname=programname
            self.associateddepartment=associateddepartment
            self.modeofadmission=modeofadmission
            self.admissioncategory=admissioncategory
            self.sslcschooladdress=sslcschooladdress
            self.sslcyearofpassing=sslcyearofpassing
            self.sslcboardoruniversity=sslcboardoruniversity
            self.sslcgroup=sslcgroup
            self.sslcpercentage=sslcpercentage
            self.hscschooladdress=hscschooladdress
            self.hscyearofpassing=hscyearofpassing
            self.hscboardofstudy=hscboardofstudy
            self.hscgroup=hscgroup
            self.hscpercentage=hscpercentage
            self.hscmaths=hscmaths
            self.hscphysics=hscphysics
            self.hscchemistry=hscchemistry
            self.currentaddress=currentaddress
            self.permanentaddress=permanentaddress
            self.fathername=fathername
            self.fatheremail=fatheremail
            self.fathermobilenumber=fathermobilenumber
            self.fatherdateofbirth=fatherdateofbirth
            self.fatherqualification=fatherqualification
            self.fatheroccupation=fatheroccupation
            self.fatherdesignation=fatherdesignation
            self.fatherannualincome=fatherannualincome
            self.mothername=mothername
            self.motheremail=motheremail
            self.mothermobilenumber=mothermobilenumber
            self.motherdateofbirth=motherdateofbirth
            self.motherqualification=motherqualification
            self.motheroccupation=motheroccupation
            self.motherdesignation=motherdesignation
            self.motherannualincome=motherannualincome 

    data=[]

    with open("SDPMS_App/csv/student_profiles.csv") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[4]==request.session.get("USER"):
                data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],
                row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],
                row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],
                row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49]))
                     
    if request.method == "POST":
        return render(request,"Student Profile.html",{"data":data})
    

def mentorprofile(request):

    class Data:

        def __init__(self,name,department,email,mobilenumber,landline,yearsofexperience):
            
            self.name=name
            self.department=department
            self.email=email
            self.mobilenumber=mobilenumber
            self.landline=landline
            self.yearsofexperience=yearsofexperience

    data=[]

    with open("SDPMS_App/csv/mentor_profiles.csv") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[2]==request.session.get("USER"):
                data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5]))
                     
    if request.method == "POST":
        return render(request,"Mentor Profile.html",{"data":data})


def mentorship(request):

    if request.method == "POST":
        return render(request,"Student Mentorship Dashboard.html")
    

def mentorstudentlist(request):
    
    class Data:

        def __init__(self,name1,email1,name2,email2,name3,email3,name4,email4,name5,email5,\
        name6,email6,name7,email7,name8,email8,name9,email9,name10,email10):
            
            self.name1=name1
            self.email1=email1
            self.name2=name2
            self.email2=email2
            self.name3=name3
            self.email3=email3
            self.name4=name4
            self.email4=email4
            self.name5=name5
            self.email5=email5
            self.name6=name6
            self.email6=email6
            self.name7=name7
            self.email7=email7
            self.name8=name8
            self.email8=email8
            self.name9=name9
            self.email9=email9
            self.name10=name10
            self.email10=email10

    data=[]

    with open("SDPMS_App/csv/Mentees-Mentor.csv") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[2]==request.session.get("USER"):
                data.append(row[0])
                data.append(row[1])

    data_final=[Data(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],\
    data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19])]

    if request.method == "POST":
        return render(request,"Mentor Student Details.html",{"data_final":data_final})
    

def mentorstudentdetails(request):

    class Data:

        def __init__(self,name,email):

            self.name=name
            self.email=email

    data=[]

    if request.method == "POST":
        with open("SDPMS_App/csv/student_profiles.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if request.POST["button"]==row[4]:
                    request.session["STUDENT"]=request.POST["button"]
                    data.append(Data(row[0],row[4]))
        return render(request,"Mentor Student Mentorship Dashboard.html",{"data":data})
    

def mentorstudentprofile(request):
    
    class Data:

        def __init__(self,name,aadharnumber,firstname,lastname,email,mobilenumber,bloodgroup,dateofbirth,\
            gender,nationality,religion,differentlyabled,typeofdisability,community,mothertongue,\
            programname,associateddepartment,modeofadmission,admissioncategory,\
            sslcschooladdress,sslcyearofpassing,sslcboardoruniversity,sslcgroup,sslcpercentage,\
            hscschooladdress,hscyearofpassing,hscboardofstudy,hscgroup,hscpercentage,hscmaths,\
            hscphysics,hscchemistry,\
            currentaddress,permanentaddress,\
            fathername,fatheremail,fathermobilenumber,fatherdateofbirth,fatherqualification,fatheroccupation,\
            fatherdesignation,fatherannualincome,\
            mothername,motheremail,mothermobilenumber,motherdateofbirth,motherqualification,motheroccupation,\
            motherdesignation,motherannualincome):
            
            self.name=name
            self.aadharnumber=aadharnumber
            self.firstname=firstname
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
            self.programname=programname
            self.associateddepartment=associateddepartment
            self.modeofadmission=modeofadmission
            self.admissioncategory=admissioncategory
            self.sslcschooladdress=sslcschooladdress
            self.sslcyearofpassing=sslcyearofpassing
            self.sslcboardoruniversity=sslcboardoruniversity
            self.sslcgroup=sslcgroup
            self.sslcpercentage=sslcpercentage
            self.hscschooladdress=hscschooladdress
            self.hscyearofpassing=hscyearofpassing
            self.hscboardofstudy=hscboardofstudy
            self.hscgroup=hscgroup
            self.hscpercentage=hscpercentage
            self.hscmaths=hscmaths
            self.hscphysics=hscphysics
            self.hscchemistry=hscchemistry
            self.currentaddress=currentaddress
            self.permanentaddress=permanentaddress
            self.fathername=fathername
            self.fatheremail=fatheremail
            self.fathermobilenumber=fathermobilenumber
            self.fatherdateofbirth=fatherdateofbirth
            self.fatherqualification=fatherqualification
            self.fatheroccupation=fatheroccupation
            self.fatherdesignation=fatherdesignation
            self.fatherannualincome=fatherannualincome
            self.mothername=mothername
            self.motheremail=motheremail
            self.mothermobilenumber=mothermobilenumber
            self.motherdateofbirth=motherdateofbirth
            self.motherqualification=motherqualification
            self.motheroccupation=motheroccupation
            self.motherdesignation=motherdesignation
            self.motherannualincome=motherannualincome 

    data=[]

    with open("SDPMS_App/csv/student_profiles.csv") as f:
        reader=csv.reader(f)
        for row in reader:
            if row[4]==request.session.get("STUDENT"):
                data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],
                row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],
                row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],
                row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49]))
                     
    if request.method == "POST":
        return render(request,"Mentor Student Profile.html",{"data":data})
    

def mentorstudentgoalsandchallenges(request):

    class Data:

        def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,\
                name10,name11,name12,name13,name14,name15,name16,name17):
            
            self.name1=name1
            self.name2=name2
            self.name3=name3
            self.name4=name4
            self.name5=name5
            self.name6=name6
            self.name7=name7
            self.name8=name8
            self.name9=name9
            self.name10=name10
            self.name11=name11
            self.name12=name12
            self.name13=name13
            self.name14=name14
            self.name15=name15
            self.name16=name16
            self.name17=name17

    data=[]    
    data1=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_goals.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("STUDENT"):
                    data1.extend(row)
        with open("SDPMS_App/csv/student_challenges.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("STUDENT"):
                    data1.extend(row)
        
        data.append(Data(data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6],data1[7],data1[8],\
            data1[10],data1[11],data1[12],data1[13],data1[14],data1[15],data1[16],data1[17]))

        return render(request,"Mentor Student Goals and Challenges.html",{"data":data})
    

def editablementorstudentgoalsandchallenges(request):

    class Data:

        def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,\
                name10,name11,name12,name13,name14,name15,name16,name17):
            
            self.name1=name1
            self.name2=name2
            self.name3=name3
            self.name4=name4
            self.name5=name5
            self.name6=name6
            self.name7=name7
            self.name8=name8
            self.name9=name9
            self.name10=name10
            self.name11=name11
            self.name12=name12
            self.name13=name13
            self.name14=name14
            self.name15=name15
            self.name16=name16
            self.name17=name17

    data=[]    
    data1=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_goals.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("STUDENT"):
                    data1.extend(row)
        with open("SDPMS_App/csv/student_challenges.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("STUDENT"):
                    data1.extend(row)
        
        data.append(Data(data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6],data1[7],data1[8],\
            data1[10],data1[11],data1[12],data1[13],data1[14],data1[15],data1[16],data1[17]))

        return render(request,"Editable Mentor Student Goals and Challenges.html",{"data":data})


def storingeditablementorstudentgoalsandchallenges(request):

    if request.method == "POST":

        list_details1=[]
        list_details2=[]
        list_details_final=[]

        with open("SDPMS_App/csv/student_goals.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                list_details1.append(row)

        with open("SDPMS_App/csv/student_challenges.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                list_details2.append(row)

        with open("SDPMS_App/csv/student_goals.csv","w",newline='') as f:
            writer=csv.writer(f)
            for item in range(len(list_details1)):
                if list_details1[item][0]==request.session.get("STUDENT"):            
                    comment1=request.POST["comments1"]
                    comment2=request.POST["comments3"]
                    comment3=request.POST["comments5"]
                    comment4=request.POST["comments7"]
                    comment5=request.POST["comments2"]
                    comment6=request.POST["comments4"]
                    comment7=request.POST["comments6"]
                    comment8=request.POST["comments8"]
                    list_details_final=[request.session.get("STUDENT"),comment1,comment2,comment3,comment4,\
                        comment5,comment6,comment7,comment8]
                    list_details1[item]=list_details_final

            writer.writerows(list_details1)

        with open("SDPMS_App/csv/student_challenges.csv","w",newline='') as f:
            writer=csv.writer(f)
            for item in range(len(list_details2)):
                if list_details2[item][0]==request.session.get("STUDENT"):            
                    comment1=request.POST["comments9"]
                    comment2=request.POST["comments11"]
                    comment3=request.POST["comments13"]
                    comment4=request.POST["comments15"]
                    comment5=request.POST["comments10"]
                    comment6=request.POST["comments12"]
                    comment7=request.POST["comments14"]
                    comment8=request.POST["comments16"]
                    list_details_final=[request.session.get("STUDENT"),comment1,comment2,comment3,comment4,\
                        comment5,comment6,comment7,comment8]
                    list_details2[item]=list_details_final

            writer.writerows(list_details2)

        return render(request,"Mentor Student Mentorship Dashboard.html")
    

def mentorstudentselfassessment(request):

    if request.method == "POST":

        class Data:

            def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13):
                
                self.name1=name1
                self.name2=name2
                self.name3=name3
                self.name4=name4
                self.name5=name5
                self.name6=name6
                self.name7=name7
                self.name8=name8
                self.name9=name9
                self.name10=name10
                self.name11=name11
                self.name12=name12
                self.name13=name13

    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_selfassessment.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("STUDENT"):
                    data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],\
                    row[9],row[10],row[11],row[12]))

        return render(request,"Mentor Student Self Assessment.html",{"data":data})


def mentorstudentachievements(request):

    class Data:

        def __init__(self,achievement):
                
            self.achievement=achievement
                

    data1=[]
    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f1:
            csvreader=csv.reader(f1)
            for row in csvreader:
                if row[0]=="student" and row[1]==request.session["STUDENT"]:
                    filename=f"{request.session['STUDENT']}_achievements.csv"
                    with open(f"SDPMS_App/csv/{filename}") as f2:
                        reader=csv.reader(f2)
                        for row in reader:
                            data1.append(row[0])
                    data.append(Data(data1))
                    
                    return render(request,"Achievements.html",{"data":data})
                

def studentachievement(request):

    class Data:

        def __init__(self,achievement):
                
            self.achievement=achievement
                

    data1=[]
    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f1:
            csvreader=csv.reader(f1)
            for row in csvreader:
                if row[0]=="student" and row[1]==request.session["USER"]:
                    filename=f"{request.session['USER']}_achievements.csv"
                    with open(f"SDPMS_App/csv/{filename}") as f2:
                        reader=csv.reader(f2)
                        for row in reader:
                            data1.append(row[0])
                    data.append(Data(data1))

                    return render(request,"Achievements.html",{"data":data})


def selfassessment(request):

    class Data:

        def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13):
                
            self.name1=name1
            self.name2=name2
            self.name3=name3
            self.name4=name4
            self.name5=name5
            self.name6=name6
            self.name7=name7
            self.name8=name8
            self.name9=name9
            self.name10=name10
            self.name11=name11
            self.name12=name12
            self.name13=name13

    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_selfassessment.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("USER"):
                    data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],\
                    row[9],row[10],row[11],row[12]))

        return render(request,"Self Assessment.html",{"data":data})
    

def editableselfassessment(request):

    class Data:

        def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13):
            
            self.name1=name1
            self.name2=name2
            self.name3=name3
            self.name4=name4
            self.name5=name5
            self.name6=name6
            self.name7=name7
            self.name8=name8
            self.name9=name9
            self.name10=name10
            self.name11=name11
            self.name12=name12
            self.name13=name13

    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_selfassessment.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("USER"):
                    data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],\
                    row[9],row[10],row[11],row[12]))
    
        return render(request,"Self Assessment Editable.html",{"data":data})


def storingeditableselfassessment(request):

    if request.method == "POST":

        list_details=[]
        list_details_final=[]

        with open("SDPMS_App/csv/student_selfassessment.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                list_details.append(row)

        with open("SDPMS_App/csv/student_selfassessment.csv","w",newline='') as f:
            writer=csv.writer(f)
            for item in range(len(list_details)):
                if list_details[item][0]==request.session.get("USER"):            
                    comment1=request.POST["comments1"]
                    comment2=request.POST["comments2"]
                    comment3=request.POST["comments3"]
                    comment4=request.POST["comments4"]
                    comment5=request.POST["comments5"]
                    comment6=request.POST["comments6"]
                    comment7=request.POST["comments7"]
                    comment8=request.POST["comments8"]
                    comment9=request.POST["comments9"]
                    comment10=request.POST["comments10"]
                    comment11=request.POST["comments11"]
                    comment12=request.POST["comments12"]
                    list_details_final=[request.session.get("USER"),comment1,comment2,comment3,comment4,\
                        comment5,comment6,comment7,comment8,comment9,comment10,comment11,comment12]
                    list_details[item]=list_details_final

            writer.writerows(list_details)

        return render(request,"Student Mentorship Dashboard.html")
            

def goalsandchallenges(request):

    class Data:

        def __init__(self,name1,name2,name3,name4,name5,name6,name7,name8,name9,\
                name10,name11,name12,name13,name14,name15,name16,name17):
            
            self.name1=name1
            self.name2=name2
            self.name3=name3
            self.name4=name4
            self.name5=name5
            self.name6=name6
            self.name7=name7
            self.name8=name8
            self.name9=name9
            self.name10=name10
            self.name11=name11
            self.name12=name12
            self.name13=name13
            self.name14=name14
            self.name15=name15
            self.name16=name16
            self.name17=name17

    data=[]    
    data1=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_goals.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("USER"):
                    data1.extend(row)

        with open("SDPMS_App/csv/student_challenges.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[0]==request.session.get("USER"):
                    data1.extend(row)
        
        data.append(Data(data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6],data1[7],data1[8],\
            data1[10],data1[11],data1[12],data1[13],data1[14],data1[15],data1[16],data1[17]))

        return render(request,"Goals and Challenges.html",{"data":data})
    

def newachievement(request):

    if request.method == "POST":

        return render(request,"New Achievement.html")
    
    
def editablenewachievement(request):
    
    from achievement import LinkedStack
    Stack = LinkedStack()
    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/student_profiles.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[4]==request.session.get("STUDENT"):
                    print(request.session.get("STUDENT"))

                    filename=f"SDPMS_App/csv/{request.session['STUDENT']}_achievements.csv"

                    with open(filename) as f:
                        reader=csv.reader(f)
                        for row in reader:
                            data.append(row)
                    data=data[::-1]
                    for row in data:
                        Stack.push(row)

                    Stack.push([request.POST["achievement"]])

                    Stack.CSV(filename)

                    return render(request,"Mentor Student Mentorship Dashboard.html")
                    

def meetingrequest(request):

    if request.method == "POST":

        return render(request,"Meeting Request.html")
    

def editablemeetingrequest(request):

    from mail import Sending_Mail
        
    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[1]==request.session.get("USER"):
                    name=row[3]
                    email=row[1]

        with open("SDPMS_App/csv/Login.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[1]==request.session.get("USER"):
                    date=request.POST["date"]
                    time=request.POST["time"]
                    description=request.POST["description"]
                    choice=request.POST["choice"]

                    message=f"{name}"+" "+"has requested for a meeting today"+"\n"+f"({date})"+" "+"at"+"\n"+f"{time}"+"\n"+"Here is the report of the request"+"\n"+"Description of the issue : "+f"{description}"+"\n"+"Urgency to sort out the issue?: "+f"{choice}"+"\n"
                    
                    Sending_Mail(email,message)

                    return render(request,"Student Mentorship Dashboard.html")


def mentorstudentpreviousmeeting(request):

    class Data:

        def __init__(self,semester,datetime,description,remark,confidentialremark,enteredby,action):

            self.semester=semester
            self.datetime=datetime
            self.description=description
            self.remark=remark
            self.confidentialremark=confidentialremark
            self.enteredby=enteredby
            self.action=action
    
    data=[]

    from meeting import Stack,prev_Meeting_details,Adding_to_stack,Displaying_from_stack

    if request.method == "POST":
        with open("SDPMS_App/csv/Login.csv") as f1:
            csvreader=csv.reader(f1)
            for row in csvreader:
                if row[0]=="student" and row[1]==request.session["STUDENT"]:
                    filename=f"SDPMS_App/csv/{request.session['STUDENT']}_meeting.csv"
                    print(filename)
                    S=Stack(5)
                    list_data=prev_Meeting_details(filename)
                    Adding_to_stack(list_data,S)
                    list_data_pop=Displaying_from_stack(S)
                    for row in list_data_pop:
                        data.append(Data(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

                    return render(request,"Mentor Student Previous Meeting Details.html",{"data":data})


def previousmeeting(request):

    class Data:

        def __init__(self,semester,datetime,description,remark):

            self.semester=semester
            self.datetime=datetime
            self.description=description
            self.remark=remark
    
    data=[]

    from meeting import Stack,prev_Meeting_details,Adding_to_stack,Displaying_from_stack

    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f1:
            csvreader=csv.reader(f1)
            for row in csvreader:
                if row[0]=="student" and row[1]==request.session["USER"]:
                    filename=f"SDPMS_App/csv/{request.session['USER']}_meeting.csv"
                    S=Stack(5)
                    list_data=prev_Meeting_details(filename)
                    Adding_to_stack(list_data,S)
                    list_data_pop=Displaying_from_stack(S)
                    for row in list_data_pop:
                        data.append(Data(row[0],row[1],row[2],row[3]))

                    return render(request,"Meeting.html",{"data":data})


def newmeeting(request):

    class Data:

        def __init__(self,name):

            self.name=name
    
    data=[]

    if request.method == "POST":

        with open("SDPMS_App/csv/Login.csv") as f:
            csvreader=csv.reader(f)
            for row in csvreader:
                if row[0]=="mentor" and row[1]==request.session["USER"]:
                    enteredby="Dr "+row[3]
                    data.append(Data(enteredby))

        return render(request,"New Meeting.html",{"data":data})


def newmeetingdetails(request):

    from meeting import prev_Meeting_details,LoadMeeting_dtls
    from mail import Sending_Mail
        
    if request.method == "POST":

        with open("SDPMS_App/csv/student_profiles.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[4]==request.session.get("STUDENT"):
                    name=row[0]
                    father_email=row[35]

        with open("SDPMS_App/csv/student_profiles.csv") as f:
            reader=csv.reader(f)
            for row in reader:
                if row[4]==request.session.get("STUDENT"):
                    semester=request.POST["semester"]
                    date=request.POST["date"]
                    time=request.POST["time"]
                    description=request.POST["description"]
                    remark=request.POST["remark"]
                    confidentialremark=request.POST["confidentialremark"]
                    enteredby=request.POST["enteredby"]
                    action=request.POST["action"]

                    filename=f"SDPMS_App/csv/{request.session['STUDENT']}_meeting.csv"

                    new_list_details=[semester,date+" "+time,description,remark,confidentialremark,enteredby,action]

                    message=f"{name}"+" "+"has met the mentor today"+"\n"+f"({date})"+" "+"at"+f"{time}"+"\n"+"Here is the report of the meeting"+"\n"+"Semester : "+f"{semester}"+"\n"+"Description : "+f"{description}"+"\n"+"Remark : "+f"{remark}"+"\n"+"Mentor Name : "+f"{enteredby}"
                    
                    Sending_Mail(father_email,message)

                    list_data=prev_Meeting_details(filename)
                    list_data.append(new_list_details)

                    LoadMeeting_dtls(filename,list_data)

                    return render(request,"Mentor Student Mentorship Dashboard.html")
    

def mentortimetable(request):

    if request.method == "POST":
    
        with open("SDPMS_App/csv/Mentees-Mentor.csv") as f:
            csvreader=csv.reader(f)
            for row in csvreader:
                if row[1]==request.session.get("USER") and row[2]=="gayathriks@ssn.edu.in":
                    return render(request,"gayathriks@ssn.edu.in Timetable.html")
                if row[1]==request.session.get("USER") and row[2]=="sripriyan@ssn.edu.in":
                    return render(request,"sripriyan@ssn.edu.in Timetable.html")
