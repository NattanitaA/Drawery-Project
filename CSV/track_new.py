import csv

filename = "new_finger_track.csv"
header = ("ID","Name","Item","Public/Private","Availability","Time")


with open(filename,'r', newline= "") as file:

    readData = [row for row in csv.DictReader(file)]
    readData[0]['Availability'] = '0'

readHeader = readData[0].keys()

with open (filename, "w", newline = "") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()
    writer.writerows(readData)
               

file.close()
csvfile.close()

