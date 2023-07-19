def Plot_data():
    import csv

    names=[]
    email=[]
    data=[]

    with open("SDPMS_App/csv/Login.csv") as f1:
        csvreader=csv.reader(f1)
        for row in csvreader:
            email.append(row[1])
            names.append(row[3])

    for item in email:
        filename=f"SDPMS_App/csv/{item}_meeting.csv"
        count=0
        with open(filename) as f1:
            csvreader=csv.reader(f1)
            for row in csvreader:
                count+=1
            data.append(count)
    return names,data

def Plotting(label,data=Plot_data()):

    import matplotlib.pyplot as plt
    
    plt.plot(label,data)
    plt.title('Meeting Report of all the students')
    plt.xlabel('Name of the student')
    plt.ylabel('Number of meetings attenged')
    plt.savefig('Meeting Report.png')



        
    
            