import base64
import sys
import random
keyA = int(input("Please enter the product key from Part A [6 digits]"))
keyB = int(input("Please enter the product key from Part B [1 digits]"))
Name = input("How do we call you?")
keyEnd = keyA+keyB
def Error(x):
    if x==1:
        print("You are not authorized to use Bites N1 service")
        sys.exit()
    if x==2:
        print("Incorrect serial number")
if keyA == 111111 or keyA == 222222 or keyA == 333333 or keyA == 444444 or keyA == 555555 or keyA == 666666:
    Error(2)
if keyEnd%8 == 0:
    encodestr = base64.b64encode('Service permission: N1;'.encode('utf-8'))
    invalid_obfuscated_code = random.randint(1111111111111,999999999999999999)
    EName = base64.b64encode(Name.encode('utf-8'))
    print(invalid_obfuscated_code,encodestr,EName)
if keyEnd%7 == 0:
    Error(1)
if keyEnd%6 == 0:
    print("All service pass (N3) does not need to be authenticated again.")
else:
    
    pass
        
    
