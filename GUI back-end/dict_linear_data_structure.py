import csv
# import time
import datetime


def stat_Data(x, status, box, y, z):
    # y = time.localtime()
    y = datetime.datetime.now()
    z = datetime.datetime.now()
    z.strftime("%Y-%m-%d %H:%M")
    y.strftime("%Y-%m-%d %H:%M")

    id = 1
    myFile1 = open('drawery.csv', 'r')
    with myFile1:
        csv_reader = csv.reader(myFile1, delimiter=',')
        # print(list(csv_reader))
        temp = list(csv_reader)
        # print(temp)
        if len(temp) > 1:
            print('------')
            print(type(temp))
            print(len(temp))
            print(temp[-1][0])
            print('-----')
            if len(temp) == 1:
                id = 1
            else:
                id = int(temp[-1][0]) + 1

    myFile1.close()

    myData = [[id, x, status, box, y, z]]

    myFile = open('drawery.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

    print("Writing complete")
    myFile.close()


def read_stat_Data():
    filename = ('drawery.csv')
    lst_name = []
    global data
    data = {}
    lst_data = []
    with open(filename, 'r', newline="") as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for line in reader:
            if i == 0: i += 1; continue
            lst_data.append(line)
            if line[1] not in lst_name:
                lst_name.append(line[1])
        # print(lst)
        for i in lst_name:
            # print("name:", i)
            for j in lst_data:
                if i in j:
                    data.update(data_create_form(i))
        # print(data)
        for j in lst_data:
            # print(j)
            # print(lst_name)
            # for i in lst_name:
            for i in lst_name:
                if i in j:
                    pass
                    # print("HELLO")
                    data.update(data_update(i, j[2], j[3], j[4], j[5]))
    # print(data)
    return data
    # for i in lst_data:
    #    print(i)
    #    for j in lst_name:
    # for j in range(len(i)):
    # print(i[j])


def data_update(name, W_D, box_x, t1, t2):
    W_D_num = 0
    W_D_str = 'W'
    global data
    if W_D == 'deposit':
        W_D_num = 1
        W_D_str = 'D'
    box_xx = int(box_x[-1]) - 1
    t11 = t1.split('.')
    t22 = t2.split('.')
    # print(t11)
    data[name][box_xx][box_x][W_D_num][W_D_str].append(t11[0])
    data[name][box_xx][box_x][W_D_num][W_D_str].append(t22[0])
    return data


def data_create_form(name):
    return {name: [
        {'box1': [{"W": []}
            , {"D": []}
                  ]
         },
        {'box2': [{"W": []}
            , {"D": []}
                  ]
         },
        {'box3': [{"W": []}
            , {"D": []}
                  ]
         },
        {'box4': [{"W": []}
            , {"D": []}
                  ]
         }
    ]
    }


def read_stat_box_Data():
    W_D_num = 0
    W_D_str = 'W'
    filename = ('drawery.csv')
    lst_name = ['box1', 'box2', 'box3', 'box4']
    global data_box
    data_box = {'box1': [{'W': []}, {'D': []}],
                'box2': [{'W': []}, {'D': []}],
                'box3': [{'W': []}, {'D': []}],
                'box4': [{'W': []}, {'D': []}]}
    # data_box['box1'][0]['W'].append
    lst_data = []
    with open(filename, 'r', newline="") as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for line in reader:
            if i == 0: i += 1; continue
            lst_data.append(line)
        # print(lst)
        for i in lst_name:
            # print("name:",i)
            for j in lst_data:
                W_D_num = 0
                W_D_str = 'W'
                if i in j:
                    if j[2] == 'deposit':
                        W_D_num = 1
                        W_D_str = 'D'
                    t1 = j[4]
                    # print(t1)
                    t11 = t1.split('.')
                    t2 = j[5]
                    t22 = t2.split('.')

                    data_box[i][W_D_num][W_D_str].append({j[1]: [t11[0], t22[0]]})
                    # data.update(data_create_form(i))
        # print(data)
    # print(data_box)
    return data_box


# stat_Data('dear','withdraw','box1',y = datetime.datetime.now(),z = datetime.datetime.now())
# read_stat_box_Data()