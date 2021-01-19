import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import pdb
import sys

def checknumber(phoneNumberStr):
    # if (driver.check_number_status(phoneNumberStr + '@c.us').status == 200):
    if (driver.check_number_status(phoneNumberStr).status == 200):
        return True
    else:
        return False

def createListOfNumbers():
        file = open("numbers.txt","a")
        for i in range(8913345,8913399):
            number = "97252" + str(i) + '@c.us'
            print(number + " " + str(checknumber(number)))
            file.write('\n' + number + " " + str(checknumber(number))) 

        

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print("Checking for more messages")
    createListOfNumbers()
   


# #### works on CMD
# import time
# from webwhatsapi import WhatsAPIDriver
# from webwhatsapi.objects.message import Message
# import pdb
# import sys

# def checknumber(phoneNumberStr):
#     # if (driver.check_number_status(phoneNumberStr + '@c.us').status == 200):
#     if (driver.check_number_status(phoneNumberStr).status == 200):
#         return True
#     else:
#         return False

# def createListOfNumbers():
#         for i in range(8913345,8913349):
#             number = "97252" + str(i) + '@c.us'
#             print(number + " " + str(checknumber(number)))

# file = open("numbers.txt","w")

# driver = WhatsAPIDriver()
# print("Waiting for QR")
# driver.wait_for_login()

# print("Bot started")

# while True:
#     time.sleep(3)
#     print("Checking for more messages")
#     pdb.set_trace()
#     createListOfNumbers()

##########
#  
# import csv

# with open('thefile.csv', 'rb') as f:
#   data = list(csv.reader(f))

# import collections
# counter = collections.defaultdict(int)
# for row in data:
#     counter[row[0]] += 1


# writer = csv.writer(open("/path/to/my/csv/file", 'w'))
# for row in data:
#     if counter[row[0]] >= 4:
#         writer.writerow(row)

