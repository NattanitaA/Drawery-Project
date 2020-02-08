#written by Veerut H. 61011356
from flask import Flask, redirect, url_for, request, render_template, jsonify, request
import ast, json, os, webbrowser, csv
from time import sleep
from enrollm1 import enroll
from checkm1 import check
from weight_check import *
from start_3 import *
from Drawer_Data import *
from Username_Data import *
import time


#go_home()
return_home_inter()
prepare_pos()
box = recall_data()
box = []
public_box = []
private_box = []
data = '0'
withdrawdata = '0'
fingerAuth = 0
returnBoxState = 0
interrupt = 0
#check = (-1)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')
    
@app.route('/withdraw_or_deposit')
def WithdrawOrDeposit():
    if fingerAuth:
        return render_template('WithdrawOrDeposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/deposit_available')
def available():
    if fingerAuth == 1:
        return render_template('Deposit_Avaible.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/deposit_public_available')
def public_available():
    if fingerAuth == 1:
        return render_template('Deposit_Public_Available.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/deposit_private_available')
def private_available():
    if fingerAuth == 1:
        return render_template('Deposit_Private_Available.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/check_finger')
def checkFinger():
    return render_template('fingerprint.html')

@app.route('/enroll_finger')
def enroll_finger_():
    return render_template('fingerprint_register.html')

@app.route('/no_finger_found')
def noFinger():
    return render_template('regis_adminpass.html')

@app.route('/return_item_deposit')
def ReturnItem():
    if fingerAuth == 1:
        return render_template('return_drawer_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/return_item_withdraw')
def ReturnItemWithdraw():
    if fingerAuth:
        return render_template('return_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/return_item_private')
def ReturnItemPrivate():
    if fingerAuth:
        return render_template('return_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_item_deposit')
def InterrupItemDeposit():
    if fingerAuth:
        return render_template('interrupt_drawer_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_withdraw')
def InterrupItemWithdraw():
    if fingerAuth:
        return render_template('interrupt_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_private')
def InterrupItemPrivate():
    if fingerAuth:
        return render_template('interrupt_drawer_private.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_item_return_deposit')
def InterrupItemReturnDeposit():
    if fingerAuth:
        return render_template('interrupt_drawer_return_deposit.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_return_withdraw')
def InterrupItemReturnWithdraw():
    if fingerAuth:
        return render_template('interrupt_drawer_return_withdraw.html')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_item_return_private')
def InterrupItemReturnPrivate():
    if fingerAuth:
        return render_template('interrupt_drawer_return_private.html')
    else:
        return redirect(url_for('home'))

@app.route('/withdrawal')
def withdrawal():
    global box
#    recall_data()
    box = recall_data()
    box = withdraw_data(Username)
    if fingerAuth:
        if box != [0,0,0,0]:
            return render_template('Withdraw_Available.html')
        else:
            return render_template('NoAvailableForEveryDrawer.html')
        return ('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/public_or_private')
def PublicOrPrivate():
    box = recall_data()
#    print(box)
    if fingerAuth:    
        if box == [1,1,1,1]:
            return render_template('NoAvailableForEveryDrawer.html')
        else:
            return render_template('Private_public.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/name_deposit', methods = ['GET','POST'])
def nameDeposit():
    res = ''
    box = recall_data()
    if fingerAuth:
        if request.method == 'POST':
            name = request.form['FirstName']
            res += name       
            return render_template('Deposit_Avaible.html')
        if request.method == 'GET':
            return json.dumps(box)
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_dp')
def check_dp():
    box = recall_data()
    public_box = [box[0],box[1]]
    if fingerAuth:
        if public_box != [1,1]:
            return render_template('Deposit_Public_Available.html')  
        else:
            return render_template('NoAvailibleDrawer.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_public_deposit', methods = ['GET','POST'])
def public_deposit():
    box = recall_data()
    public_box = [box[0],box[1]]
    if fingerAuth:
        if request.method == 'GET':
            return json.dumps(public_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/box_check_pp')
def check_pp():
    box = recall_data()
    private_box = [box[2],box[3]]
    if fingerAuth:
        if private_box != [1,1]:
            return render_template('get_drawer_private.html')
        else:
            return render_template('NoAvailibleDrawer.html')
    else:
        return redirect(url_for('home'))

@app.route('/get_drawer_private', methods = ['POST'])
def getDrawerPrivate():
    global t1getprv
    box = recall_data()
    private_box = [box[2],box[3]]
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'POST':
            if private_box[0] == 0:
                t1getprv = time.time()
                go_to_locker(3)
                t2 = time.time()
                print('private box run time: ', t2-t1getprv)
                return render_template('place_item_private.html') #return page GUI
    #            
            elif private_box[1] == 0:
                t1getprv = time.time()
                go_to_locker(4)
                t2 = time.time()
                print('private box run time: ', t2-t1getprv)
                return render_template('place_item_private.html') #return page GUI
        return('error')
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer_private', methods = ['POST'])
def returnDrawerPrivate():
    global fingerAuth
    global Username
    global returnBoxState
    global interrupt
    global t1prv
    box = recall_data()
    private_box = [box[2],box[3]]
#    private_box = [0,0]
    if fingerAuth == 1:
        if request.method == 'POST':
            if private_box[0] == 0:
                t1prv = time.time() 
                returnpos_to_locker(3)
                if not interrupt:
                    sleep(1)
                    go_home()
                    sleep(1)
                    prepare_pos()
                    rewrite_data(Username, 3,'1')
                    box = recall_data()
                    returnBoxState = 0
                    fingerAuth = 0
                    t2 = time.time()
                    print('return private box runtime: ', t2-t1prv)
                    return redirect(url_for('home'))
                    # return render_template('welcome.html')
                
            elif private_box[1] == 0:
                t1prv = time.time()
                returnpos_to_locker(4)
                if not interrupt:
                    sleep(1)
                    go_home()
                    sleep(1)
                    prepare_pos()
                    rewrite_data(Username, 4,'1')
                    box = recall_data()
                    returnBoxState = 0
                    fingerAuth = 0
                    t2 = time.time()
                    print('return private box runtime: ', t2-t1prv)
                    return redirect(url_for('home'))
                    # return render_template('welcome.html')
        return ('error')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_private', methods=['POST','GET'])
def interrupt_drawers_private():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            t2 = time.time()
            print('private box interrupt runtime: ', t2 - t1getprv)
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return_private', methods=['POST'])
def interrupt_drawers_return_private():
    global interrupt
    global returnBoxState
    if fingerAuth:
        if request.method == 'POST':
            interrupt = 1
            inter()
            interrupt = 0
            returnBoxState = 0
            t2 = time.time()
            print('return private box interrupt runtime: ', t2-t1prv)
            return render_template('place_item_private.html')
    else:
        return redirect(url_for('home'))


@app.route('/box_check_private_deposit', methods = ['GET','POST'])
def private_deposit():
    box = recall_data()
    private_box = [box[2],box[3]]
    if fingerAuth:
        if request.method == 'GET':        
            return json.dumps(private_box)
    else:
        return redirect(url_for('home'))
    
@app.route('/name_withdrawal', methods = ['GET'])
def nameWithdrawal():
    global box
    box = recall_data()
    box = withdraw_data(Username)
    print(box)
    if fingerAuth:
        if request.method == 'GET':
            return json.dumps(box)
    else:
        return redirect(url_for('home'))
    
@app.route('/register', methods = ['POST'])
def enroll_():
    global fingerData
    global register_name
    if request.method == 'POST':
        fingerData = enroll()
        if fingerData != (-1):
            print(fingerData)
            writeUsernameData(register_name, fingerData)
            return redirect(url_for('home'))
        else:
                return render_template('regest_fail.html')
    return ('error')

@app.route('/check', methods = ['GET','POST'])
def check_():
    global check_tim
    global fingerAuth
    global Username
    if request.method == 'POST':
        check_tim = check()
        if check_tim != (-1):
            fingerAuth = 1
            Username = findUsernameData(str(check_tim))
            print(Username)
            return render_template('WithdrawOrDeposit.html')
        else:
            return render_template('regis_adminpass.html')
    return ('error')

@app.route('/admin_password', methods = ['POST'])
def adminPassword():
    SetPassword = '12345'
    if request.method == 'POST':
        GetPassword = request.form['Password']
        print (GetPassword)
        if GetPassword == SetPassword:
            return render_template('register.html')
        else:
            return redirect(url_for('noFinger'))
    
@app.route('/register_name', methods = ['POST'])
def getRegisterName():
    global register_name
    if request.method == 'POST':
        register_name = request.form['FirstName']
        print (register_name)
        return render_template('fingerprint_register.html')
    
@app.route('/weight_check_private', methods = ['POST'])
def check_weight_private():
    global returnBoxState
    if fingerAuth:
        if request.method == 'POST':
            if checkWeight():
                if not returnBoxState:
                    returnBoxState = 1
#                    return render_template('return_drawer_private.html')
                    return redirect(url_for('ReturnItemPrivate'))
                else:
                    return('')
    else:
        return redirect(url_for('home'))
    
@app.route('/buttonpressed_private', methods = ['POST'])
def button_pressed_private():
    global returnBoxState
    if fingerAuth == 1:
        if request.method == 'POST':
            if not returnBoxState:
                #checkWeight(0)
                #weightInter()
                returnBoxState = 1
#                return render_template('return_drawer_private.html')
                return redirect(url_for('ReturnItemPrivate'))
            else:
                return('')
    else:
        return redirect(url_for('home'))
    
@app.route('/weight_check_withdraw', methods = ['POST'])
def check_weight_withdraw():
    global returnBoxState
    if fingerAuth:
        if request.method == 'POST':
            if checkWeight():
                if not returnBoxState:
                    returnBoxState = 1
#                    return render_template('return_drawer_withdraw.html')
                    return redirect(url_for('ReturnItemWithdraw'))
                else:
                    return('')
    else:
        return redirect(url_for('home'))
    
@app.route('/buttonpressed_withdraw', methods = ['POST'])
def button_pressed_withdraw():
    global returnBoxState
    if fingerAuth == 1:
        if request.method == 'POST':
            if not returnBoxState:
                #weightInter()
                returnBoxState = 1
                return redirect(url_for('ReturnItemWithdraw'))
#                return render_template('return_drawer_withdraw.html.html')
            else:
                return ('')
    else:
        return redirect(url_for('home'))

@app.route('/weight_check_deposit', methods = ['POST'])
def check_weight_deposit():
    global returnBoxState
    if fingerAuth:
        if request.method == 'POST':
            if checkWeight():
                if not returnBoxState:
                    returnBoxState = 1
                    return redirect(url_for('ReturnItem'))
#                    return render_template('return_drawer_private.html')
                else:
                    return ('')
    else:
        return redirect(url_for('home'))
    
@app.route('/buttonpressed_deposit', methods = ['POST'])
def button_pressed_deposit():
    global returnBoxState
    if fingerAuth == 1:
        if request.method == 'POST':
            if not returnBoxState:
                #weightInter()
                returnBoxState = 1
                return redirect(url_for('ReturnItem'))
#                return render_template('return_drawer_private.html')
            else:
                return('')
    else:
        return redirect(url_for('home'))
    
@app.route('/getDataPublic', methods = ['POST'])
def get_data():
    if fingerAuth == 1:
        if request.method == 'POST':
            global data
            data = request.form['data']
            print(type(data))
            print(data)
            return render_template('get_drawer_deposit.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/get_drawer', methods=['POST'])
def get_drawers():
    global data
    global t1getpub
    print(data)
    print(type(data))
    if fingerAuth == 1:
        if request.method == 'POST':
            t1getpub = time.time()
            data = int(data)
            go_to_locker(data)
            t2 = time.time()
            print('get public box runtime: ', t2-t1getpub)
            return render_template('Place_item.html')  
        return(str(data))
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer', methods=['POST'])
def return_drawers():
    global data
    global fingerAuth
    global Username
    global returnBoxState
    global t1returnpub
    print(data)
    print(type(data))
    if fingerAuth == 1:
        if request.method == 'POST':
            t1returnpub = time.time()
            data = int(data)
            print(data)
            returnpos_to_locker(data)
            if not interrupt:
                sleep(1)
                go_home()
                sleep(1)
                prepare_pos()
                rewrite_data('' ,data , '1')
                box = recall_data()
                fingerAuth = 0
                returnBoxState = 0
                t2 = time.time()
                print('return public box runtime: ',t2-t1returnpub)
                return redirect(url_for('home'))
#            return render_template('welcome.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/interrupt_drawer', methods=['POST','GET'])
def interrupt_drawers():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            returnBoxState = 0
            t2 = time.time()
            print('get public box interrupt runtime: ', t2-t1getpub)
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return', methods=['POST'])
def interrupt_drawers_return():
    global interrupt
    global returnBoxState
    if fingerAuth:
        if request.method == 'POST':
            interrupt = 1
            inter()
            interrupt = 0
            returnBoxState = 0
            t2 = time.time()
            print('return public box interrupt runtime: ', t2-t1returnpub)
            return render_template('Place_item.html')
    else:
        return redirect(url_for('home'))

@app.route('/getWithdrawData', methods=['POST'])
def get_withdraw_data():
    if fingerAuth == 1:
        if request.method == 'POST':
            global withdrawdata
            withdrawdata=request.form['withdrawdata']
            print(withdrawdata)
            return render_template('get_drawer_withdraw.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/getWithdrawDrawer', methods=['POST'])
def get_withdraw_drawer():
    global t1getwithdraw
    global withdrawdata
    print(withdrawdata)
    if fingerAuth == 1:
        if request.method == 'POST':
            t1getwithdraw = time.time()
            withdrawdata = int(withdrawdata)
            go_to_locker(withdrawdata)
            t2 = time.time()
            print("get withdraw box runtime: ", t2-t1getwithdraw)
            return render_template('place_item_withdraw.html')
    else:
        return redirect(url_for('home'))
    
@app.route('/return_drawer_withdraw', methods=['POST'])
def return_drawers_withdraw():
    global fingerAuth
    global withdrawdata
    global Username
    global returnBoxState
    global interrupt
    global t1returnwithdraw
    print(withdrawdata)
    print(type(withdrawdata))
    if fingerAuth == 1:
        if request.method == 'POST':
            t1returnwithdraw = time.time()
            withdrawdata = int(withdrawdata)
            print(withdrawdata)
            returnpos_to_locker(withdrawdata)
            if not interrupt:
                sleep(1)
                go_home()               
                sleep(1)
                prepare_pos()
                rewrite_data('',withdrawdata,'0')
                box = recall_data()
                fingerAuth = 0
                returnBoxState = 0
                t2 = time.time()
                print("return withdraw box runtime: ", t2-t1returnwithdraw)
                return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_withdraw', methods=['POST','GET'])
def interrupt_drawers_withdraw():
    if fingerAuth:
        if request.method == 'POST':
            inter()
            t2 = time.time()
            print('get withdraw box interrupt runtime: ', t2-t1getwithdraw)
            return redirect(url_for('WithdrawOrDeposit'))
        return('wow')
    else:
        return redirect(url_for('home'))

@app.route('/interrupt_drawer_return_withdraw', methods=['POST'])
def interrupt_drawers_return_withdraw():
    global returnBoxState
    global interrupt
    if fingerAuth:
        if request.method == 'POST':
            interrupt = 1
            inter()
            interrupt = 0
            returnBoxState = 0
            t2 = time.time()
            print('return withdraw box interrupt runtime: ', t2-t1returnwithdraw)
            return render_template('place_item_withdraw.html')
    else:
        return redirect(url_for('home'))

#if __name__=="__main__":
#    app.run(ssl_context="adhoc")
        
        
        


