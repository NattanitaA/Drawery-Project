import csv

filename = "database33.csv"
#header = ["ID", "Name", "Fingerprint"]
with open(filename, 'r') as readfile:
    read = csv.reader(readfile)
    rows = list(read)
    

def writeHead():
    with open(filename, 'w', newline= '') as appendfile:
        append = csv.writer(appendfile, delimiter=',')
        append.writerow(["ID", "Name", "Fingerprint"])

def writeData(name, fingerprintID):
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        lst=[]
        i = 0
        for line in reader:
            if i == 0: i += 1; continue
            lst.append(line[1])
            print(lst)
    ID = len(lst)
    print(ID)
    ID = str(ID+1)
    with open(filename, 'a', newline= '') as appendfile:
        header = ["ID", "Name", "Fingerprint"]
        append=csv.DictWriter(appendfile, fieldnames= header, delimiter=',')
        #next(append)
        #append.writeheader()
        append.writerow({"ID":ID , "Name" : name, "Fingerprint":fingerprintID})
        #append.writerow(newrow)
def findData(searchFingerID):
    with open(filename) as file:
        reader = csv.reader(file, delimiter = ',')
        # a = input()
        # for line in reader:
        #     if a ==
        lstFinger = []
        k=0
        for line in reader:
            if searchFingerID == line[2]:
                print(line[1])
                break


    


# with open(filename,'r', newline= "") as file:
    

print('Done')
#writeHead()
#writeData('elf', '4')
#findData('4')