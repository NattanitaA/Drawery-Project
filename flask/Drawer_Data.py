#This file was written by Veerut H. and Nattanita A.
import csv

filename = "new_finger_track.csv"
header = ("ID","Name","Item","Public/Private","Availability","Process")
def recall_data():
    global box
    box = []
    with open(filename,'r', newline= "") as file:
        reader = csv.reader(file, delimiter=',')
        i=0
        for line in reader:
            if i == 0: i+=1; continue
            box.append(int(line[4]))
        print(box)
    
    return box

def withdraw_data(name):
    global box
    print(box)
    private_box_access = [0,0]
    print(type(private_box_access))
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if name == line[1]:
                private_box_access[int(line[0])-3]=(int(line[4]))
            print(private_box_access)
        if len(private_box_access) != 0:
            print('dsfs')
            box[2]=0
            box[3]=0
            for i in range(len(private_box_access)):
                box[2+i] = private_box_access[i]
    print('-----')
    print(box)
    return box

def rewrite_data(name, number, dbValue):
    print('------')
    print (dbValue)
    print(name)
    with open(filename,'r', newline= "") as file:

        readData = [row for row in csv.DictReader(file)]
        readData[number-1]['Availability'] = dbValue
        readData[number-1]['Name'] = name

    readHeader = readData[0].keys()

    with open (filename, "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header)
        writer.writeheader()
        writer.writerows(readData)
#    file.close()
#    csvfile.close()
    return 
