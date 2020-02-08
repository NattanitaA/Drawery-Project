"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.
https://github.com/bastianraschke/pyfingerprint/issues/48
"""
 
import time
from pyfingerprint.pyfingerprint import PyFingerprint
 
def enroll():
    ## Enrolls new finger

    try:
        finger = PyFingerprint('/dev/ttyUSB0')

        print('Waiting for finger...')
        print(finger.readImage())
        ## Wait for finger to read
        while ( finger.readImage() == False ):
            pass
        
        
        ## Converts read image to characteristics and stores it in charbuffer 1
        finger.convertImage(0x01)

     
        ## Checks if finger is already enrolled
        result = finger.searchTemplate()
        print(result)
        positionNumber = result[0]
     
        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            return (-1)
            exit(0)
        #return True
    
        print('Remove finger...')
        time.sleep(2)
     
        print('Waiting for same finger again...')
     
        ## Wait for finger to read again
        while ( finger.readImage() == False ):
            pass
     
        ## Converts read image to characteristics and stores it in charbuffer 2
        finger.convertImage(0x02)
     
        ## Compares the charbuffers
        if ( finger.compareCharacteristics() == 0 ):
            
            raise Exception('Fingers do not match')
            return (-1)
        ## Creates a template
        finger.createTemplate()
     
        ## Saves template at new position number
        positionNumber = finger.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))
        return (positionNumber)
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        return (-1)
        exit(1)
        