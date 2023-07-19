import csv

def username_password(list):
    
    filename = "Login.csv"

    #Open the CSV file in write mode
    with open(filename, 'w', newline='') as file:
        
        writer = csv.writer(file)
   
        header = ['Username','Password']
            
        writer.writerow(header)

        writer.writerows(list)

List_of_uname_pass=[["johndoe2210456@ssn.edu.in","joe23"],
["santhosh2210410@ssn.edu.in","santosh"],
["deepakchahar2210736@ssn.edu.in","deep736"],
["monica2210090@ssn.edu.in","moni0310"],
["sharukhkhan2210345@ssn.edu.in","s2khan"],
["sujithbala2210786@ssn.edu.in","suji2004"],
["danesh2210769@ssn.edu.in","dan769"],
["manjusri2210732@ssn.edu.in","1234"],
["farthima2210007@ssn.edu.in","farthi2004"],
["vithula2210321@ssn.edu.in","vithu321"]]

username_password(List_of_uname_pass)