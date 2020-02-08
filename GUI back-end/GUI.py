import tkinter as tk
from dict_linear_data_structure import *
from tkinter import font
 
root = tk.Tk()
HEIGHT = int(root.winfo_screenheight())
WIDTH = int(root.winfo_screenwidth())
data = read_stat_Data()
data_box_form = read_stat_box_Data()
# data_box_form = {"box1":[{"W":[{'name':[1,2]},{'name2':[3,4]}]},{"D":[{'name':[3,4]}]}],}
print(data)
print(data_box_form)


def find_cmd(user_in):
    lst_word = user_in.split(" ")
    # try :
    name = lst_word[0].lower()
    try:
        for i in range(len(lst_word)):
            if i==0:
                    if "box" in lst_word[i].lower():
                        print(len(data_box_form[lst_word[0].lower()][0]["W"]))
                        if len(data_box_form[lst_word[0].lower()][0]) == 0:
                            final_str = ' '
                            final_str2 = ' '
                            final_str3 = ' '
                            final_str4 = ' '


                        # for i in range(len (data_box_form[lst_word[0].lower()][0]["W"])):
                        elif len(data_box_form[lst_word[0].lower()][0]) > 0:
                            if len(data_box_form[lst_word[0].lower()][0]["W"]) != 0:
                                final_str = "withdraw = \n  {0} ".format(str(data_box_form[lst_word[0].lower()][0]["W"][-1]))
                            else: final_str = 'withdraw ='
                            final_str2 = ' '
                            final_str4 = ' '
                            if len(data_box_form[lst_word[0].lower()][1]["D"])!=0:
                                final_str3 = "deposit = \n  {0}" .format(str(data_box_form[lst_word[0].lower()][1]["D"][-1]))
                            else: final_str3 = 'withdraw ='
                    else:
                        data_w = data[name][0]['box1'][0]["W"]
                        data_d = data[name][0]['box1'][1]["D"]
                        data_w2 = data[name][1]['box2'][0]["W"]
                        data_d2 = data[name][1]['box2'][1]["D"]
                        data_w3 = data[name][2]['box3'][0]["W"]
                        data_d3 = data[name][2]['box3'][1]["D"]
                        data_w4 = data[name][3]['box4'][0]["W"]
                        data_d4 = data[name][3]['box4'][1]["D"]
                        final_str = "box {0} withdraw =  {1} \n      deposit  = {2}".format("1", data_w, data_d)
                        final_str2 = "box {0} withdraw = {1} \n      deposit  = {2}".format("2", data_w2, data_d2)
                        final_str3 = "box {0} withdraw = {1} \n      deposit  = {2}".format("3", data_w3, data_d3)
                        final_str4 = "box {0} withdraw = {1} \n      deposit  = {2}".format("4", data_w4, data_d4)


            elif i == 1 and not lst_word[i]== "":
                if lst_word[i].upper() == "W" or lst_word[i].lower() == "withdraw":
                    final_str = "box {0} withdraw = {1}".format("1",data_w)
                    final_str2 = "box {0} withdraw = {1}".format("2",data_w2)
                    final_str3 = "box {0} withdraw = {1}".format("3",data_w3)
                    final_str4 = "box {0} withdraw = {1}".format("4",data_w4)

                elif lst_word[i].upper() == "D" or lst_word[i].lower() == "deposit":
                    final_str = "box {0} deposit = {1}".format("1",data_d)
                    final_str2 = "box {0} deposit = {1}".format("2",data_d2)
                    final_str3 = "box {0} deposit = {1}".format("3",data_d3)
                    final_str4 = "box {0} deposit = {1}".format("4",data_d4)
                elif "box" in lst_word[i].lower():
                    # print("this :",data[lst_word[0]][0][lst_word[1]])
                    if lst_word[1].lower() == 'box1':
                        final_str2 = " "
                        final_str4 = " "
                        final_str3 = " "
                    elif lst_word[1].lower() == 'box2':
                        final_str = " "
                        final_str3 = " "
                        final_str4 = " "
                    elif lst_word[1].lower() == 'box3':
                        final_str = " "
                        final_str2 = " "
                        final_str4 = " "
                    elif lst_word[1].lower() == 'box4':
                        final_str = " "
                        final_str2 = " "
                        final_str3 = " "
                    else :
                        final_str = "ERROR"
                        final_str2 = " "
                        final_str3 = " "
                        final_str4 = " "
                else:

                    final_str = "ERROR"
                    final_str2 = " "
                    final_str3 = " "
                    final_str4 = " "

            label['text'] = final_str
            label2['text'] = final_str2
            label3['text'] = final_str3
            label4['text'] = final_str4
    except :
        final_str = "ERROR 404"
        final_str2 = ' '
        label['text'] = final_str
        label2['text'] = final_str2
        label3['text'] = final_str2
        label4['text'] = final_str2
    #
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='mac-wallpaper-1920x1080-4.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1 ,relwidth=0.75,relheight=0.1,anchor='n')

user_in = tk.Entry(frame,font=50,bg='#F0F8FF')
user_in.place(relwidth=0.65, relheight=1)

button = tk.Button(frame,text="ENTER NAME",font=40,command=lambda: find_cmd(user_in.get()))
button.place(relx=0.7,relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.6, anchor='n')

label = tk.Label(lower_frame,font=('Courier',14),anchor='nw',justify='left',bd=4,bg='#F0F8FF')
label.place(relwidth=0.5, relheight=0.5)

label2 = tk.Label(lower_frame,font=('Courier',14),anchor='nw',justify='left',bd=4,bg='#F0F8FF')
label2.place(relwidth=0.5, relheight=0.5,relx=0.5,rely=0)

label3 = tk.Label(lower_frame,font=('Courier',14),anchor='nw',justify='left',bd=4,bg='#F0F8FF')
label3.place(relwidth=0.5, relheight=0.5,relx=0,rely=0.5)

label4 = tk.Label(lower_frame,font=('Courier',14),anchor='nw',justify='left',bd=4,bg='#F0F8FF')
label4.place(relwidth=0.5, relheight=0.5,relx=0.5,rely=0.5)

root.bind("<Return>",lambda event: find_cmd(user_in.get()))
root.mainloop()